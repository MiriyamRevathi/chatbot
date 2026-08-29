document.addEventListener("DOMContentLoaded", () => {
    console.log("ChatFlow Application Initialized.");
    if (document.getElementById("intent-chart-container")) {
        SVGCharts.renderBarChart("intent-chart-container", {
            "greeting": 45, "billing": 32, "technical": 28, "refund": 15, "help": 22
        });
    }
});
