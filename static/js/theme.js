document.addEventListener("DOMContentLoaded", () => {
    const toggleBtn = document.getElementById("theme-toggle");
    const currentTheme = localStorage.getItem("chatflow-theme") || "dark";
    document.documentElement.setAttribute("data-theme", currentTheme);

    if (toggleBtn) {
        toggleBtn.textContent = currentTheme === "dark" ? "🌙" : "☀️";
        toggleBtn.addEventListener("click", () => {
            const theme = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
            document.documentElement.setAttribute("data-theme", theme);
            localStorage.setItem("chatflow-theme", theme);
            toggleBtn.textContent = theme === "dark" ? "🌙" : "☀️";
        });
    }
});
