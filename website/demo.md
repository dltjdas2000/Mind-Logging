---
layout: default
title: Demo Chatbot
permalink: /demo/
---

# Mind-Logging

We can help you keep a diary and manage stress.

<!-- 캘린더 배치 -->
<div id="calendar" style="margin: 20px 0; text-align: center;">
    <h3>Select a Date</h3>
    <input type="date" id="selectedDate" style="padding: 5px; border: 1px solid #ccc; border-radius: 4px;">
</div>

# Welcome to the AI Chatbot Page

This is a simple chatbot interface powered by Flask and Hugging Face.

<!-- 챗봇 인터페이스 -->
<div id="chatbot">
    <div id="chatLog" style="border: 1px solid #ccc; padding: 10px; height: 400px; overflow-y: scroll;">
        <!-- 대화 내용이 여기에 추가됩니다 -->
    </div>
    <textarea id="userInput" placeholder="Type your message..." style="width: 100%; height: 50px;"></textarea>
    <button onclick="sendMessage()">Send</button>
</div>

<script src="{{ '/assets/demo.js' | relative_url }}"></script>