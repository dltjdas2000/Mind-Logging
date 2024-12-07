// 날짜 정보 추적 및 관리
let selectedDate = new Date().toLocaleDateString("en-CA");

// 초기 인사말 표시
window.onload = function () {
    const calendar = document.getElementById("selectedDate");
    const chatLog = document.getElementById("chatLog");

    // 사용자의 로컬 시간을 기준으로 캘린더 기본값 설정
    calendar.value = selectedDate;

    // 초기 인사말 추가
    const welcomeMessage = `<div style="text-align: left; margin: 10px;">
                                <span style="background-color: #f0f0f0; padding: 10px; border-radius: 10px; display: inline-block;">
                                    Hello! Let's record today's events. What would you like to share?
                                </span>
                            </div>`;
    chatLog.innerHTML += welcomeMessage;

    // 캘린더 변경 이벤트 리스너 추가
    calendar.addEventListener('change', function() {
        selectedDate = this.value;
        console.log(`Selected date changed to: ${selectedDate}`);
    });
};

// 엔터키로 메시지 전송 기능 추가
document.addEventListener('DOMContentLoaded', function() {
    const inputField = document.getElementById("userInput");
    inputField.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            sendMessage();
        }
    });
});

// 메시지 전송 시 사용자 입력 처리
async function sendMessage() {
    const inputField = document.getElementById("userInput");
    const chatLog = document.getElementById("chatLog");

    if (!inputField.value.trim()) {
        alert("Please enter a message!");
        return;
    }

    const userMessage = inputField.value.trim();

    // 사용자 메시지 출력
    const userBubble = `<div style="text-align: right; margin: 10px;">
                            <span style="background-color: #d1f7c4; padding: 10px; border-radius: 10px; display: inline-block;">
                                ${userMessage}
                            </span>
                        </div>`;
    chatLog.innerHTML += userBubble;

    inputField.value = ""; // 입력 필드 초기화
    chatLog.scrollTop = chatLog.scrollHeight; // 스크롤 아래로 이동

    try {
        // 서버로 날짜와 함께 사용자 메시지 전송
        const response = await fetch("http://localhost:5001/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ 
                message: userMessage,
                date: selectedDate  // 선택된 날짜 함께 전송
            }),
        });

        // 네트워크 오류 처리
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // 챗봇 응답 출력
        const botBubble = `<div style="text-align: left; margin: 10px;">
                                <span style="background-color: #f0f0f0; padding: 10px; border-radius: 10px; display: inline-block;">
                                    ${data.reply}
                                </span>
                           </div>`;
        chatLog.innerHTML += botBubble;
        chatLog.scrollTop = chatLog.scrollHeight; // 스크롤 아래로 이동
    } catch (error) {
        console.error("Error communicating with server:", error);
        
        // 사용자에게 오류 메시지 표시
        const errorBubble = `<div style="text-align: left; margin: 10px; color: red;">
                                <span style="background-color: #ffeeee; padding: 10px; border-radius: 10px; display: inline-block;">
                                    Sorry, there was a problem connecting to the server. Please try again.
                                </span>
                             </div>`;
        chatLog.innerHTML += errorBubble;
    }
}