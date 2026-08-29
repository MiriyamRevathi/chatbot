document.addEventListener("DOMContentLoaded", () => {
    const trainBtn = document.getElementById("btn-train-model");
    if (trainBtn) {
        trainBtn.addEventListener("click", async () => {
            const name = document.getElementById("model-name-input").value.trim() || "Custom Model";
            const algo = document.getElementById("model-algo-select").value;

            try {
                ToastNotification.show("Training model on dataset...", "info");
                const res = await APIClient.post("/api/models/train", { algorithm: algo, name });
                ToastNotification.show(`Model '${res.model.name}' trained successfully! F1: ${(res.model.f1_score * 100).toFixed(1)}%`, "success");
                setTimeout(() => window.location.reload(), 1500);
            } catch (err) {
                ToastNotification.show(err.message, "danger");
            }
        });
    }
});
