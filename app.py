
from flask import Flask, jsonify, render_template_string
import random
import time

app = Flask(__name__)

start_time = time.time()

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HYDROGEN | Clean Energy Project</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', sans-serif;
    background: #07111f;
    color: #eaf6ff;
    overflow-x: hidden;
}

html {
    scroll-behavior: smooth;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 22px 8%;
    background: rgba(7,17,31,0.95);
    border-bottom: 1px solid #18334b;
    position: sticky;
    top: 0;
    z-index: 10;
}

.logo {
    font-size: 23px;
    font-weight: 800;
    letter-spacing: 3px;
    color: #54d9ff;
}

nav a {
    color: #c4d9e9;
    text-decoration: none;
    margin-left: 28px;
    font-size: 14px;
    transition: 0.3s;
}

nav a:hover {
    color: #54d9ff;
}

.hero {
    min-height: 90vh;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 70px 9%;
    gap: 40px;
    background:
    radial-gradient(circle at 75% 50%, #123b60 0%, transparent 40%),
    linear-gradient(120deg,#07111f,#0b1d30);
}

.hero-text {
    max-width: 570px;
}

.tag {
    color: #55dfff;
    letter-spacing: 4px;
    font-size: 12px;
    font-weight: bold;
}

h1 {
    font-size: clamp(42px,6vw,75px);
    line-height: 1.08;
    margin: 22px 0;
}

h1 span {
    color: #53d9ff;
}

.hero p {
    color: #a9bed0;
    line-height: 1.8;
    font-size: 16px;
}

.btn {
    display: inline-block;
    margin-top: 30px;
    padding: 14px 28px;
    border-radius: 30px;
    background: #38c9f4;
    color: #061321;
    font-weight: bold;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: 0.3s;
}

.btn:hover {
    background: white;
    transform: translateY(-3px);
    box-shadow: 0 0 25px #38c9f477;
}

/* TITANIUM VESSEL */

.visual {
    width: 390px;
    max-width: 100%;
    height: 450px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

.vessel {
    position: relative;
    width: 230px;
    height: 330px;
    border: 5px solid #9db8cb;
    border-radius: 65px 65px 45px 45px;
    background: linear-gradient(
        90deg,
        #253e52,
        #9cb5c6 22%,
        #233c52 50%,
        #a3bdce 80%,
        #263e52
    );
    box-shadow:
        0 0 35px #39c9ff55,
        inset 0 0 25px #07111f;
    overflow: hidden;
}

.liquid {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 72%;
    background: linear-gradient(
        180deg,
        #0d9cc477,
        #075b9caa
    );
    border-top: 3px solid #6ceaff;
}

.electrode {
    position: absolute;
    top: 48px;
    width: 9px;
    height: 200px;
    border-radius: 5px;
    z-index: 3;
    box-shadow: 0 0 12px currentColor;
}

.positive {
    left: 65px;
    background: #ff6767;
    color: #ff6767;
}

.negative {
    right: 65px;
    background: #54eaff;
    color: #54eaff;
}

.electrode-label {
    position: absolute;
    font-size: 13px;
    font-weight: bold;
    z-index: 4;
}

.pos-label {
    left: 35px;
    top: 18px;
    color: #ff8585;
}

.neg-label {
    right: 35px;
    top: 18px;
    color: #55e8ff;
}

.bubble {
    position: absolute;
    bottom: 15px;
    width: 9px;
    height: 9px;
    border: 1px solid #a8f5ff;
    border-radius: 50%;
    background: #a5efff55;
    animation: rise 3s infinite ease-in;
    z-index: 5;
}

@keyframes rise {
    0% {transform: translateY(0) scale(.6);opacity:0;}
    20% {opacity:1;}
    100% {transform:translateY(-220px) scale(1.4);opacity:0;}
}

.vessel-top {
    position: absolute;
    top: 45px;
    width: 125px;
    height: 18px;
    border-radius: 8px;
    background: #a9c2d3;
    border: 3px solid #d6e8f4;
    z-index: 5;
}

.vessel-name {
    position: absolute;
    bottom: 35px;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: bold;
    color: white;
    z-index: 6;
    text-shadow: 0 1px 5px black;
}

.section {
    padding: 90px 9%;
}

.section-title {
    text-align: center;
    font-size: 36px;
    margin-bottom: 15px;
}

.subtitle {
    text-align: center;
    color: #91a9bc;
    margin-bottom: 50px;
    line-height: 1.7;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
    gap: 22px;
}

.card {
    padding: 30px;
    border: 1px solid #23435c;
    border-radius: 18px;
    background: linear-gradient(145deg,#10263b,#0a1828);
    transition: .3s;
}

.card:hover {
    transform: translateY(-7px);
    border-color: #4ad8ff;
    box-shadow: 0 10px 30px #0005;
}

.icon {
    font-size: 32px;
    margin-bottom: 18px;
}

.card h3 {
    margin-bottom: 13px;
    color: #55dfff;
}

.card p {
    color: #a8bdce;
    line-height: 1.7;
    font-size: 14px;
}

/* SIMULATOR */

.simulator {
    background: #0b1c2c;
    border-top: 1px solid #1c3b54;
    border-bottom: 1px solid #1c3b54;
}

.dashboard {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
}

.panel {
    padding: 30px;
    background: #10273c;
    border: 1px solid #294a62;
    border-radius: 18px;
}

.panel h3 {
    margin-bottom: 25px;
    color: #57dcff;
}

.stat {
    display: flex;
    justify-content: space-between;
    padding: 17px 0;
    border-bottom: 1px solid #29465b;
    color: #adc2d1;
}

.stat strong {
    color: white;
}

.control {
    margin-top: 25px;
}

input[type=range] {
    width: 100%;
    accent-color: #42d5ff;
    margin: 20px 0;
}

.status {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 20px;
    background: #3b252b;
    color: #ff9c9c;
    font-size: 12px;
}

.status.on {
    background: #123e38;
    color: #6af5c4;
}

button:disabled {
    opacity: .5;
    cursor: not-allowed;
    transform: none;
}

.process {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 15px;
    margin-top: 30px;
}

.process-step {
    padding: 20px;
    border: 1px solid #31536b;
    border-radius: 14px;
    text-align: center;
    min-width: 145px;
    background: #10273c;
}

.arrow {
    color: #55dfff;
    font-size: 25px;
}

.spec-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

.spec-table td {
    padding: 17px;
    border-bottom: 1px solid #29465b;
}

.spec-table td:first-child {
    color: #59ddff;
}

footer {
    text-align: center;
    padding: 40px;
    background: #050d17;
    color: #8299aa;
    font-size: 13px;
    line-height: 1.8;
}

.safety {
    margin: 30px auto 0;
    max-width: 900px;
    padding: 18px;
    border: 1px solid #795c34;
    border-radius: 12px;
    background: #2a241a;
    color: #ffdda5;
    font-size: 13px;
    line-height: 1.7;
}

@media(max-width:800px) {
    nav {
        padding: 18px 5%;
    }

    nav a {
        margin-left: 10px;
        font-size: 12px;
    }

    .hero {
        flex-direction: column;
        text-align: center;
        padding: 65px 6%;
    }

    .dashboard {
        grid-template-columns: 1fr;
    }

    .visual {
        transform: scale(.85);
    }

    .section {
        padding: 65px 6%;
    }
}
</style>
</head>

<body>

<nav>
    <div class="logo">H₂ / ENERGY</div>
    <div>
        <a href="#about">About</a>
        <a href="#working">Working</a>
        <a href="#simulation">Simulation</a>
        <a href="#specs">Specs</a>
    </div>
</nav>

<section class="hero">
    <div class="hero-text">
        <div class="tag">NEXT GENERATION ENERGY CONCEPT</div>

        <h1>THE FUTURE<br>IS <span>HYDROGEN.</span></h1>

        <p>
            Exploring clean energy through an innovative
            hydrogen generation working model. A titanium
            vessel, positive and negative electrodes, and
            the science of electrolysis come together
            to demonstrate the potential of hydrogen energy.
        </p>

        <a href="#working" class="btn">EXPLORE THE MODEL →</a>
    </div>

    <div class="visual">
        <div class="vessel">
            <div class="vessel-top"></div>
            <div class="electrode positive"></div>
            <div class="electrode negative"></div>
            <div class="electrode-label pos-label">+</div>
            <div class="electrode-label neg-label">−</div>
            <div class="liquid"></div>
            <div class="vessel-name">TITANIUM</div>
            <div id="bubbles"></div>
        </div>
    </div>
</section>

<section class="section" id="about">
    <h2 class="section-title">About The Project</h2>
    <p class="subtitle">
        An educational demonstration of hydrogen production
        through the electrolysis of water.
    </p>

    <div class="cards">
        <div class="card">
            <div class="icon">⚙️</div>
            <h3>Titanium Vessel</h3>
            <p>
                The vessel represents the main enclosure
                of the experimental model. Material
                compatibility and corrosion resistance
                depend on the actual design and operating conditions.
            </p>
        </div>

        <div class="card">
            <div class="icon">➕</div>
            <h3>Positive Electrode</h3>
            <p>
                The anode is the positive electrode.
                During electrolysis, oxidation occurs
                at this electrode.
            </p>
        </div>

        <div class="card">
            <div class="icon">➖</div>
            <h3>Negative Electrode</h3>
            <p>
                The cathode is the negative electrode.
                During electrolysis, reduction occurs
                at this electrode.
            </p>
        </div>

        <div class="card">
            <div class="icon">💧</div>
            <h3>Water Electrolysis</h3>
            <p>
                Electrical energy drives the separation
                of water into hydrogen and oxygen.
            </p>
        </div>
    </div>
</section>

<section class="section simulator" id="simulation">
    <h2 class="section-title">Interactive Model</h2>
    <p class="subtitle">
        Explore a conceptual simulation of the electrolysis process.
        This dashboard does not control physical equipment.
    </p>

    <div class="dashboard">

        <div class="panel">
            <h3>MODEL CONTROL</h3>

            <div>
                System Status:
                <span class="status" id="status">SIMULATION OFF</span>
            </div>

            <div class="control">
                <p>Simulation intensity</p>
                <input type="range" min="1" max="10"
                       value="5" id="intensity">
                <p>Intensity: <strong id="intensityValue">5</strong>/10</p>
            </div>

            <button class="btn" id="startButton"
                    onclick="toggleSimulation()">
                START SIMULATION
            </button>
        </div>

        <div class="panel">
            <h3>LIVE MODEL DISPLAY</h3>

            <div class="stat">
                <span>System condition</span>
                <strong id="condition">Standby</strong>
            </div>

            <div class="stat">
                <span>Electrode status</span>
                <strong id="electrodes">Inactive</strong>
            </div>

            <div class="stat">
                <span>Visual bubbles</span>
                <strong id="bubbleCount">0</strong>
            </div>

            <div class="stat">
                <span>Elapsed simulation</span>
                <strong id="elapsed">0 sec</strong>
            </div>
        </div>

    </div>
</section>

<section class="section" id="working">
    <h2 class="section-title">How It Works</h2>
    <p class="subtitle">
        Understanding the scientific process behind hydrogen generation.
    </p>

    <div class="process">
        <div class="process-step">
            <div class="icon">⚡</div>
            <h3>Electrical Energy</h3>
            <p>Energy input</p>
        </div>

        <div class="arrow">→</div>

        <div class="process-step">
            <div class="icon">💧</div>
            <h3>Water</h3>
            <p>Electrolyte system</p>
        </div>

        <div class="arrow">→</div>

        <div class="process-step">
            <div class="icon">🔬</div>
            <h3>Electrolysis</h3>
            <p>Electrochemical reaction</p>
        </div>

        <div class="arrow">→</div>

        <div class="process-step">
            <div class="icon">H₂ + O₂</div>
            <h3>Products</h3>
            <p>Hydrogen and oxygen</p>
        </div>
    </div>
</section>

<section class="section" id="specs">
    <h2 class="section-title">Model Components</h2>
    <p class="subtitle">
        Overview of the components represented in the project.
    </p>

    <div class="panel">
        <table class="spec-table">
            <tr>
                <td>Vessel Material</td>
                <td>Titanium</td>
            </tr>
            <tr>
                <td>Positive Electrode</td>
                <td>Anode (+)</td>
            </tr>
            <tr>
                <td>Negative Electrode</td>
                <td>Cathode (−)</td>
            </tr>
            <tr>
                <td>Scientific Principle</td>
                <td>Water Electrolysis</td>
            </tr>
            <tr>
                <td>Energy Input</td>
                <td>Electrical Energy</td>
            </tr>
            <tr>
                <td>Expected Products</td>
                <td>Hydrogen and Oxygen</td>
            </tr>
        </table>
    </div>

    <div class="safety">
        <strong>⚠ IMPORTANT SAFETY INFORMATION</strong><br>
        This website is an educational simulation, not an operating
        guide for a hydrogen generator. Hydrogen is highly flammable,
        and hydrogen mixed with oxygen can create an explosive
        atmosphere. Never collect, compress, store, or ignite mixed
        gases. Real electrolysis equipment requires professionally
        engineered gas separation, ventilation, electrical protection,
        pressure protection and appropriate safety review.
    </div>
</section>

<footer>
    <h3 style="color:#55dfff;letter-spacing:3px;">
        H₂ / CLEAN ENERGY PROJECT
    </h3>
    <p>Innovation • Science • Sustainable Future</p>
    <p>Educational Working Model | Hydrogen Energy Concept</p>
    <br>
    © 2026 Hydrogen Project. All Rights Reserved.
</footer>

<script>

let running = false;
let startedAt = 0;
let elapsed = 0;
let timer = null;

const bubbles = document.getElementById("bubbles");
const slider = document.getElementById("intensity");

slider.addEventListener("input", function() {
    document.getElementById("intensityValue").innerText =
        this.value;
});

function createBubbles() {
    if (!running) return;

    const count = Number(slider.value);

    bubbles.innerHTML = "";

    for(let i = 0; i < count; i++) {
        let bubble = document.createElement("div");
        bubble.className = "bubble";

        bubble.style.left = (25 + Math.random()*55) + "%";
        bubble.style.animationDelay = (Math.random()*2) + "s";
        bubble.style.animationDuration =
            (2 + Math.random()*2) + "s";

        bubbles.appendChild(bubble);
    }

    document.getElementById("bubbleCount").innerText = count;
}

function toggleSimulation() {

    running = !running;

    const status = document.getElementById("status");
    const button = document.getElementById("startButton");

    if(running) {

        startedAt = Date.now() - elapsed * 1000;

        status.innerText = "SIMULATION ACTIVE";
        status.classList.add("on");

        button.innerText = "STOP SIMULATION";

        document.getElementById("condition").innerText =
            "Visual simulation active";

        document.getElementById("electrodes").innerText =
            "Conceptually active";

        createBubbles();

        timer = setInterval(updateSimulation, 1000);

    } else {

        status.innerText = "SIMULATION OFF";
        status.classList.remove("on");

        button.innerText = "START SIMULATION";

        document.getElementById("condition").innerText =
            "Standby";

        document.getElementById("electrodes").innerText =
            "Inactive";

        document.getElementById("bubbleCount").innerText = "0";

        bubbles.innerHTML = "";

        clearInterval(timer);
    }
}

function updateSimulation() {

    if(!running) return;

    elapsed = Math.floor((Date.now() - startedAt) / 1000);

    document.getElementById("elapsed").innerText =
        elapsed + " sec";

    createBubbles();

    fetch("/api/status")
    .then(response => response.json())
    .then(data => {
        console.log("Backend connected:", data.server);
    })
    .catch(error => console.log(error));
}

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/api/status")
def status():
    return jsonify({
        "server": "Connected",
        "project": "Hydrogen Electrolysis Model",
        "simulation": "Educational only",
        "timestamp": round(time.time() - start_time, 2)
    })


if __name__ == "__main__":
    app.run(debug=True)
