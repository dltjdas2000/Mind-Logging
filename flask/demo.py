from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration, pipeline
import random
import json
import os
from datetime import datetime
import subprocess

# Flask app initialization
app = Flask(__name__)
CORS(app)

# Default model initialization (starting with base model)
model_name = "facebook/blenderbot-400M-distill"  # Default BlenderBot model
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")


class MentalHealthDiary:
    def __init__(self):
        self.user_info = {}  # Store user information (name and age)
        self.conversation_log = []  # Store conversation logs
        self.logs_dir = os.path.join(os.path.dirname(__file__), 'conversation_logs')
        os.makedirs(self.logs_dir, exist_ok=True)
        self.model_finetuned = False  # Track if Fine-Tuned model is available
        self.initial_question_asked = False  # Track if the initial question has been processed
        self.used_responses = set()  # Track used responses to avoid repetition

    def analyze_sentiment(self, user_input):
        """Analyze the sentiment of the user input."""
        result = sentiment_analyzer(user_input)
        return result[0]["label"]  # "POSITIVE" or "NEGATIVE"

    def check_loneliness(self, user_input):
        """Check if the user input indicates loneliness."""
        loneliness_keywords = ["alone", "lonely", "loneliness"]
        return any(keyword in user_input.lower() for keyword in loneliness_keywords)

    def generate_response(self, sentiment, user_input, is_initial_question):
        """Generate a response that considers the context of previous conversation and avoids repetition."""
        # Normalize user input for processing
        user_input_lower = user_input.lower().strip()

        # Handle specific predefined questions
        predefined_responses = {
            "who are you?": "I'm Penko, your friendly mental health companion.",
            "who r u?": "I'm Penko, here to support you whenever you need."
        }
        if user_input_lower in predefined_responses:
            return predefined_responses[user_input_lower]

        # Handle loneliness-related inputs
        if self.check_loneliness(user_input):
            loneliness_responses = [
                "You're not alone. I'm here for you whenever you need someone to talk to.",
                "I understand it can feel tough, but remember, Penko is always here to support you.",
                "Feeling lonely is hard, but you're not by yourself—I'm here to help.",
                "Whenever you feel this way, just know I'm right here for you."
            ]
            unused_responses = [resp for resp in loneliness_responses if resp not in self.used_responses]

            if unused_responses:
                response = random.choice(unused_responses)
            else:
                response = random.choice(loneliness_responses)  # Fallback to reuse if all responses are used

            self.used_responses.add(response)
            return response

        # Combine conversation history for context
        conversation_history = "\n".join([entry["user_input"] for entry in self.conversation_log])
        user_input_with_context = f"{conversation_history}\n{user_input}"

        # Handle initial question based on sentiment
        if is_initial_question:
            # Sentiment-based empathy for initial question
            empathy_responses = {
                "POSITIVE": [
                    "That's wonderful to hear! What else made your day great?",
                    "I'm so happy for you! Could you share more?",
                    "That sounds amazing. Tell me more!"
                ],
                "NEGATIVE": [
                    "That sounds difficult. How are you managing?",
                    "I'm here for you. Would you like to share more?",
                    "It seems challenging. Let me know if you'd like to talk about it."
                ],
                "NEUTRAL": [
                    "I'm here to listen. Feel free to share more.",
                    "That sounds interesting. Tell me more!",
                    "Got it. Let me know if there's more you'd like to discuss."
                ]
            }
            possible_responses = empathy_responses.get(sentiment, ["I'm here to support you."])
            unused_responses = [resp for resp in possible_responses if resp not in self.used_responses]

            if unused_responses:
                response = random.choice(unused_responses)
            else:
                response = random.choice(possible_responses)  # Fallback to reuse if all responses are used

            self.used_responses.add(response)
            return response

        # Generate dynamic responses using Blenderbot with conversation context
        inputs = tokenizer(user_input_with_context, return_tensors="pt")
        reply_ids = model.generate(**inputs)
        model_response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

        # Avoid repeating generated responses
        if model_response in self.used_responses:
            model_response += " Would you like to explore this further?"

        self.used_responses.add(model_response)
        return model_response

    def save_conversation(self):
        """Save the entire conversation log to a file."""
        if not self.conversation_log:
            return "No conversation to save."

        today = datetime.now().strftime("%Y-%m-%d")
        log_file = os.path.join(self.logs_dir, f"{today}_diary.json")
        try:
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_log, f, ensure_ascii=False, indent=4)
            self.conversation_log = []  # Clear the log after saving
            return f"Conversation saved"
        except Exception as e:
            return f"Error saving conversation: {e}"

    def retrain_model(self):
        print("Starting model retraining...")
        try:
            # retrain_blenderbot.py 스크립트 실행
            subprocess.run(["python", "retrain_blenderbot.py"], check=True)
            print("Model retrained successfully!")

            # 재학습된 모델 다시 로드
            global tokenizer, model
            tokenizer = BlenderbotTokenizer.from_pretrained("blenderbot-finetuned")
            model = BlenderbotForConditionalGeneration.from_pretrained("blenderbot-finetuned")
            self.model_finetuned = True  # Mark as fine-tuned
            print("Fine-Tuned model reloaded successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error during retraining: {e}")

    def process_user_input(self, user_input):
        if user_input.lower() == "exit":
            return self.save_conversation()

        if not self.initial_question_asked:
            sentiment = self.analyze_sentiment(user_input)
            ai_response = self.generate_response(sentiment, user_input, is_initial_question=True)
            self.initial_question_asked = True
        else:
            ai_response = self.generate_response(None, user_input, is_initial_question=False)

        self.conversation_log.append({"timestamp": datetime.now().isoformat(),
                                       "user_input": user_input,
                                       "ai_response": ai_response})

        # Retrain model after 5 interactions
        if len(self.conversation_log) >= 5 and not self.model_finetuned:
            self.retrain_model()

        return ai_response


mental_health_diary = MentalHealthDiary()


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "").strip()

    if not user_input:
        if not mental_health_diary.user_info:
            return jsonify({"reply": "Hello! I'm PENGCO. What's your name and age?"})
        else:
            return jsonify({"reply": "How was your day today? Feel free to share your thoughts."})

    if user_input.lower() == "reset":
        mental_health_diary.user_info = {}
        mental_health_diary.initial_question_asked = False
        mental_health_diary.used_responses.clear()
        return jsonify({"reply": "Your profile has been reset. What's your name and age?"})

    if not mental_health_diary.user_info:
        try:
            name, age = user_input.split(" ")
            mental_health_diary.user_info = {"name": name.capitalize(), "age": int(age)}
            return jsonify({"reply": f"Thank you {name.capitalize()}. You're {age} years old, right? If this is incorrect, type 'reset'. If it's correct, type 'yes'."})
        except ValueError:
            return jsonify({"reply": "Please provide your name and age in the format: 'Name Age'."})

    if user_input.lower() == "yes":
        name = mental_health_diary.user_info.get("name")
        return jsonify({"reply": f"Great to meet you, {name}! How was your day today? Feel free to share."})

    response = mental_health_diary.process_user_input(user_input)
    return jsonify({"reply": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
