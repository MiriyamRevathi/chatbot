document.addEventListener("DOMContentLoaded", () => {
    const analyzeBtn = document.getElementById("btn-analyze-nlp");
    const input = document.getElementById("nlp-input");
    const resultsBox = document.getElementById("nlp-results");

    if (analyzeBtn) {
        analyzeBtn.addEventListener("click", async () => {
            const text = input.value.trim();
            if (!text) return;

            try {
                const data = await APIClient.post("/api/nlp/analyze", { text });
                resultsBox.style.display = "grid";

                document.getElementById("res-tokens").textContent = data.tokens.join(", ");
                document.getElementById("res-intent").innerHTML = `<strong>${data.intent.intent}</strong> (${Math.round(data.intent.confidence * 100)}% confidence)`;
                document.getElementById("res-sentiment").innerHTML = `<strong>${data.sentiment.sentiment}</strong> (Score: ${data.sentiment.score})`;
                document.getElementById("res-entities").innerHTML = data.entities.map(e => `<span class="badge badge-role">${e.type}: ${e.entity}</span>`).join(" ");
            } catch (err) {
                ToastNotification.show(err.message, "danger");
            }
        });
    }
});
