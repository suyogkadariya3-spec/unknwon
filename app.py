import streamlit as str_lit
import streamlit.components.v1 as web_comps

# Configure the browser tab title and layout
str_lit.set_page_config(
    page_title="TIME_STAMP_BURST", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Isolated Time-Burst Illusion payload
time_burst_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚨 TIME_STAMP_BURST 🚨</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body, html { width: 100%; height: 100%; background-color: #000; overflow: hidden; font-family: 'Courier New', Courier, monospace; user-select: none; }
        #fullscreen-prompt { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: #000; z-index: 10000; display: flex; flex-direction: column; justify-content: center; align-items: center; cursor: pointer; border: 4px solid #00ffaa; color: #00ffaa; }
        .pulse-text { font-size: 28px; font-weight: bold; letter-spacing: 2px; animation: pulse 0.4s infinite alternate; text-align: center; }
        @keyframes pulse { 0% { transform: scale(0.95); opacity: 0.7; text-shadow: 0 0 5px #00ffaa; } 100% { transform: scale(1.05); opacity: 1; text-shadow: 0 0 20px #00ffaa; } }
        canvas { width: 100vw; height: 100vh; display: block; }
        #strobe-layer { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 999; opacity: 0.12; mix-blend-mode: difference; }
    </style>
</head>
<body>
    <div id="fullscreen-prompt" onclick="initiateIllusion()">
        <div class="pulse-text">⚠️ WARNING: TIMELINE DISRUPTION ⚠️</div>
        <p style="font-size: 11px; color: #ff0055; margin-top: 15px; letter-spacing: 1px;">[ CLICK TO FORCE OVERRIDE ]</p>
    </div>
    <div id="strobe-layer"></div>
    <canvas id="time-canvas"></canvas>

    <script>
        const canvas = document.getElementById('time-canvas');
        const ctx = canvas.getContext('2d');
        const strobe = document.getElementById('strobe-layer');
        let frame = 0, isRunning = false;

        function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
        window.addEventListener('resize', resize);

        function generateRandomTime() {
            const y = Math.floor(Math.random() * 1200) + 1800;
            const m = String(Math.floor(Math.random() * 12) + 1).padStart(2, '0');
            const d = String(Math.floor(Math.random() * 28) + 1).padStart(2, '0');
            const h = String(Math.floor(Math.random() * 24)).padStart(2, '0');
            const mn = String(Math.floor(Math.random() * 60)).padStart(2, '0');
            const s = String(Math.floor(Math.random() * 60)).padStart(2, '0');
            const ms = String(Math.floor(Math.random() * 999)).padStart(3, '0');
            return `${y}/${m}/${d} ${h}:${mn}:${s}.${ms}`;
        }

        function animate() {
            if (!isRunning) return;
            frame++;

            // Rapid strobe interference line matrix layers
            if (frame % 3 === 0) strobe.style.backgroundColor = Math.random() > 0.5 ? '#fff' : '#00ffff';
            else if (frame % 3 === 1) strobe.style.backgroundColor = '#ff0055';
            else strobe.style.backgroundColor = 'transparent';

            // Motion trail alpha layering effect
            ctx.fillStyle = 'rgba(0, 0, 0, 0.12)'; 
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Explode randomized timeline array values across arbitrary grid coordinates
            ctx.fillStyle = Math.random() > 0.88 ? '#ff0055' : '#00ffaa'; 
            ctx.font = 'bold ' + (Math.floor(Math.random() * 10) + 12) + 'px monospace';
            
            for(let i = 0; i < 8; i++) {
                ctx.fillText(generateRandomTime(), Math.random() * (canvas.width - 200), Math.random() * canvas.height);
            }

            requestAnimationFrame(animate);
        }

        function initiateIllusion() { 
            document.getElementById('fullscreen-prompt').style.display = 'none'; 
            isRunning = true; 
            resize(); 
            animate(); 
        }
    </script>
</body>
</html>
"""

# Render the isolated code block natively across deployment viewport borders
web_comps.html(time_burst_html, height=900, scrolling=False)
