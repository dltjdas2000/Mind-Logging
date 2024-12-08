---
layout: default
title: contact
permalink: /contact/
---

# CONTACT 
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
<br>
If you have any questions to developers,     
feel free to contact us using the methods below

<div style="margin-top: 20px;">
    <p>
        <img id="emailIcon1" src="../assets/images/50px_mailbox.png" alt="Mailbox" style="cursor: pointer; width: 40px; height: 40px;">
        <strong>Seongmin Lee: dltjdas@gmail.com</strong>
        <span id="copyMessage1" style="display: none; color: green; font-weight: bold; margin-left: 10px;">Email copied!</span>
    </p>
    <p>
        <img id="emailIcon2" src="../assets/images/50px_mailbox.png" alt="Mailbox" style="cursor: pointer; width: 40px; height: 40px;">
        <strong>Hyejin Kwon: jinnnneee@gmail.com</strong>
        <span id="copyMessage2" style="display: none; color: green; font-weight: bold; margin-left: 10px;">Email copied!</span>
    </p>
    <p>
        <img id="emailIcon3" src="../assets/images/50px_mailbox.png" alt="Mailbox" style="cursor: pointer; width: 40px; height: 40px;">
        <strong>Hyunsu Kim: kimsu0509@gmail.com</strong>
        <span id="copyMessage3" style="display: none; color: green; font-weight: bold; margin-left: 10px;">Email copied!</span>
    </p>
</div>

<script>
    function copyEmail(email, messageId) {
        navigator.clipboard.writeText(email).then(() => {
            const message = document.getElementById(messageId);
            message.style.display = "inline"; 
            setTimeout(() => {
                message.style.display = "none"; 
            }, 3000);
        }).catch(err => {
            console.error("Failed to copy email:", err);
        });
    }

    document.getElementById("emailIcon1").addEventListener("click", function() {
        copyEmail("dltjdas@gmail.com", "copyMessage1");
    });

    document.getElementById("emailIcon2").addEventListener("click", function() {
        copyEmail("jinnnneee@gmail.com", "copyMessage2");
    });

    document.getElementById("emailIcon3").addEventListener("click", function() {
        copyEmail("kimsu0509@gmail.com", "copyMessage3");
    });
</script>