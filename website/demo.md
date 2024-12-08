---
layout: default
title: Demo Chatbot
permalink: /demo/
---

## Welcome to the AI Chatbot Demo Page

<div class="center-image">
  <img src="../assets/images/pengco.png" alt="pengco" />
</div>
<style>
  .center-image {
    display: flex;
    justify-content: center; 
    align-items: center; 
  }
</style>

<!-- 캘린더 배치 -->
<div id="calendar" style="margin: 20px 0; text-align: center;">
    <p>You can select a date for journaling.</p>
    <input type="date" id="selectedDate" style="padding: 5px; border: 1px solid #ccc; border-radius: 4px;">
</div>

This is a demo version of a chat for journaling.

<!-- 챗봇 인터페이스 -->
<div id="chatbot">
    <div id="chatLog" style="border: 1px solid #ccc; padding: 10px; height: 400px; overflow-y: scroll;">
        <!-- 대화 내용이 여기에 추가됩니다 -->
    </div>
    <textarea id="userInput" placeholder="Type your message..." style="width: 100%; height: 50px;"></textarea>
    <button onclick="sendMessage()">Send</button>
</div>

<script src="{{ '/assets/demo.js' | relative_url }}"></script>