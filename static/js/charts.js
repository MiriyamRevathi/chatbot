class SVGCharts {
    static renderBarChart(containerId, data) {
        const container = document.getElementById(containerId);
        if (!container) return;
        let html = '<div style="display:flex; gap:12px; align-items:flex-end; height:180px;">';
        const maxVal = Math.max(...Object.values(data)) || 1;
        for (const [key, val] of Object.entries(data)) {
            const h = Math.round((val / maxVal) * 150);
            html += `<div style="text-align:center; flex:1;">
                <div style="background:#3b82f6; height:${h}px; border-radius:4px;"></div>
                <div style="font-size:11px; margin-top:4px;">${key}</div>
            </div>`;
        }
        html += '</div>';
        container.innerHTML = html;
    }
}
