document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("chat-input");
    const sendBtn = document.getElementById("btn-send-chat");
    const messagesBox = document.getElementById("chat-messages");
    const newChatBtn = document.getElementById("btn-new-chat");

    if (newChatBtn) {
        newChatBtn.addEventListener("click", async () => {
            const res = await APIClient.post("/api/conversations", { title: "New Chat" });
            window.location.href = `/chat/${res.conversation.id}`;
        });
    }

    const sendMessage = async () => {
        if (!input) return;
        const text = input.value.trim();
        if (!text) return;

        const pathParts = window.location.pathname.split("/");
        const convId = pathParts[pathParts.length - 1] !== "chat" ? pathParts[pathParts.length - 1] : null;

        // Append user bubble
        const userBubble = document.createElement("div");
        userBubble.className = "message-bubble message-user";
        userBubble.innerHTML = `<div class="message-sender">User</div><div class="message-text">${text}</div>`;
        messagesBox.appendChild(userBubble);
        input.value = "";
        messagesBox.scrollTop = messagesBox.scrollHeight;

        try {
            const data = await APIClient.post("/api/chat", { conversation_id: convId, message: text });
            const botMsg = data.result.message;

            const botBubble = document.createElement("div");
            botBubble.className = "message-bubble message-bot";
            botBubble.innerHTML = `
                <div class="message-sender">Bot</div>
                <div class="message-text">${botMsg.text}</div>
                <div class="message-meta">
                    <span class="meta-tag">Intent: ${data.result.intent}</span>
                    <span class="meta-tag">Sentiment: ${data.result.sentiment}</span>
                    <span class="meta-tag">Confidence: ${Math.round(data.result.confidence * 100)}%</span>
                </div>
            `;
            messagesBox.appendChild(botBubble);
            messagesBox.scrollTop = messagesBox.scrollHeight;
        } catch (err) {
            ToastNotification.show(err.message, "danger");
        }
    };

    if (sendBtn) sendBtn.addEventListener("click", sendMessage);
    if (input) {
        input.addEventListener("keydown", (e) => {
            if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
    }
});
