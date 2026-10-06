import streamlit as st
import streamlit.components.v1 as components
st.title("🏗️ RCC Beam Design")

st.write(
    "Interactive Reinforced Concrete Beam Design "
    "based on the supplied worked example."
)

# =========================================================
# TITLE
# =========================================================

# =========================================================
# PROBLEM STATEMENT
# =========================================================
# =========================================================
# PROBLEM STATEMENT — ENGINEERING STYLE
# =========================================================
# PROBLEM STATEMENT
# =========================================================

st.subheader("📖 Problem Statement")

st.html("""
<div style="
    background: linear-gradient(135deg, #102a43, #164e70);
    border-left: 6px solid #00c6ff;
    border-radius: 14px;
    padding: 28px 32px;
    margin: 10px 0 28px 0;
    color: #f5f9fc;
    box-shadow: 0 6px 20px rgba(0,0,0,0.25);
">

<div style="
    font-size: 17px;
    line-height: 1.8;
    text-align: justify;
">

A rectangular reinforced concrete beam, located inside a building in a coastal town, 
is simply supported on two masonry walls 230 mm thick and 6m apart (centre-to-centre). 
The beam has to carry, in addition to its own weight, a distributed live load 
of 10 kN/m and a dead load of 5 kN/m. Design the beam section for maximum 
moment at midspan. Assume Fe 415 steel.

</div>

</div>
""")









# =========================================================
# SIDEBAR — DESIGN INPUTS
# =========================================================

st.sidebar.header("🎛️ DESIGN INPUTS")

# ---------------------------------------------------------
# Geometry
# ---------------------------------------------------------

st.sidebar.subheader("📐 Geometry")

aggregate_size = st.number_input(
    "Nominal Maximum Aggregate Size (mm)",
    min_value=10.0,
    max_value=40.0,
    value=20.0,
    step=5.0
)

L = st.sidebar.number_input(
    "Span L (m)",
    min_value=1.0,
    max_value=30.0,
    value=6.0,
    step=0.1
)

wall_t = st.sidebar.number_input(
    "Masonry wall thickness (mm)",
    min_value=100.0,
    max_value=600.0,
    value=230.0,
    step=10.0
)

b = st.sidebar.number_input(
    "Beam width b (mm)",
    min_value=100.0,
    max_value=1000.0,
    value=250.0,
    step=10.0
)

D = st.sidebar.number_input(
    "Beam depth D (mm)",
    min_value=200.0,
    max_value=1500.0,
    value=450.0,
    step=10.0
)

# ---------------------------------------------------------
# Load
# ---------------------------------------------------------

st.sidebar.subheader("⚖️ Loads")

tributary_width = st.sidebar.number_input(
    "Tributary width (m)",
    min_value=0.10,
    max_value=10.0,
    value=0.60,
    step=0.05
)

slab_thickness = st.sidebar.number_input(
    "Slab thickness (m)",
    min_value=0.05,
    max_value=1.0,
    value=0.25,
    step=0.01
)

dead_load = st.sidebar.number_input(
    "Dead load excluding self-weight (kN/m)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.5
)

live_load = st.sidebar.number_input(
    "Live load (kN/m)",
    min_value=0.0,
    max_value=100.0,
    value=10.0,
    step=0.5
)

load_factor = st.sidebar.number_input(
    "Load factor",
    min_value=1.0,
    max_value=3.0,
    value=1.5,
    step=0.05
)

# ---------------------------------------------------------
# Material
# ---------------------------------------------------------

st.sidebar.subheader("🧱 Materials")

fck = st.sidebar.number_input(
    "Concrete grade fck (MPa)",
    min_value=15.0,
    max_value=60.0,
    value=25.0,
    step=5.0
)

fy = st.sidebar.number_input(
    "Steel grade fy (MPa)",
    min_value=250.0,
    max_value=600.0,
    value=415.0,
    step=5.0
)

concrete_unit_weight = st.sidebar.number_input(
    "RCC unit weight (kN/m³)",
    min_value=20.0,
    max_value=30.0,
    value=25.0,
    step=0.5
)

# ---------------------------------------------------------
# Reinforcement
# ---------------------------------------------------------

st.sidebar.subheader("🔩 Reinforcement")

clear_cover = st.sidebar.number_input(
    "Clear cover (mm)",
    min_value=15.0,
    max_value=100.0,
    value=30.0,
    step=1.0
)

stirrup_diameter = st.sidebar.number_input(
    "Stirrup diameter (mm)",
    min_value=6.0,
    max_value=20.0,
    value=8.0,
    step=1.0
)

main_bar_1 = st.sidebar.number_input(
    "Main bar 1 diameter (mm)",
    min_value=8.0,
    max_value=40.0,
    value=25.0,
    step=1.0
)

number_bar_1 = st.sidebar.number_input(
    "Number of bar 1",
    min_value=0,
    max_value=20,
    value=1,
    step=1
)

main_bar_2 = st.sidebar.number_input(
    "Main bar 2 diameter (mm)",
    min_value=8.0,
    max_value=40.0,
    value=20.0,
    step=1.0
)

number_bar_2 = st.sidebar.number_input(
    "Number of bar 2",
    min_value=0,
    max_value=20,
    value=2,
    step=1
)




# =========================================================
# MAIN SCREEN
# =========================================================
# =========================================================
# DYNAMIC BEAM ELEVATION — SIDE VIEW
# =========================================================

st.header("🏗️ Beam Elevation")

# Dynamic dimensions
beam_height = max(35, min(75, D * 0.14))
wall_width = max(45, min(90, wall_t * 0.30))

components.html(
f"""
<!DOCTYPE html>

<html>

<head>

<style>

body {{
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: Arial, sans-serif;
}}

.beam-container {{
    width: 100%;
    background: white;
    border: 2px solid #444;
    border-radius: 10px;
    overflow: hidden;
}}

.title {{
    background: #d9f2ff;
    border-bottom: 2px solid #555;
    padding: 10px 14px;
    font-size: 18px;
    font-weight: bold;
    color: #111;
}}

.loads {{
    text-align: center;
    padding: 12px 5px 5px 5px;
    font-size: 16px;
    font-weight: bold;
}}

.dead {{
    color: #222;
}}

.live {{
    color: #e53935;
}}

svg {{
    display: block;
    width: 100%;
    height: auto;
}}

</style>

</head>


<body>


<div class="beam-container">


    <!-- =====================================================
         TITLE
         ===================================================== -->

    <div class="title">
        ▪ 2. BEAM ELEVATION (SIDE VIEW)
    </div>


    <!-- =====================================================
         LOAD VALUES
         ===================================================== -->

    <div class="loads">

        <div class="dead">
            W<sub>DL</sub> = {dead_load:.1f} kN/m
            (dead load)
        </div>

        <div class="live">
            W<sub>LL</sub> = {live_load:.1f} kN/m
            (live load)
        </div>

    </div>


    <!-- =====================================================
         ENGINEERING DRAWING
         ===================================================== -->

    <svg
        viewBox="0 0 1000 520"
        xmlns="http://www.w3.org/2000/svg"
    >


        <!-- =================================================
             BRICK PATTERN
             ================================================= -->

        <defs>

            <pattern
                id="brickPattern"
                width="40"
                height="20"
                patternUnits="userSpaceOnUse"
            >

                <rect
                    width="40"
                    height="20"
                    fill="#c9783c"
                />

                <path
                    d="
                    M 0 0 H 40
                    M 0 20 H 40
                    M 20 0 V 20
                    "
                    stroke="#8b4a24"
                    stroke-width="1"
                />

            </pattern>

        </defs>


        <!-- =================================================
             DISTRIBUTED LOAD ARROWS
             ================================================= -->

        <g
            stroke="#e53935"
            stroke-width="3"
            fill="#e53935"
        >

            <line x1="180" y1="75" x2="180" y2="135"/>
            <polygon points="174,127 186,127 180,140"/>

            <line x1="220" y1="75" x2="220" y2="135"/>
            <polygon points="214,127 226,127 220,140"/>

            <line x1="260" y1="75" x2="260" y2="135"/>
            <polygon points="254,127 266,127 260,140"/>

            <line x1="300" y1="75" x2="300" y2="135"/>
            <polygon points="294,127 306,127 300,140"/>

            <line x1="340" y1="75" x2="340" y2="135"/>
            <polygon points="334,127 346,127 340,140"/>

            <line x1="380" y1="75" x2="380" y2="135"/>
            <polygon points="374,127 386,127 380,140"/>

            <line x1="420" y1="75" x2="420" y2="135"/>
            <polygon points="414,127 426,127 420,140"/>

            <line x1="460" y1="75" x2="460" y2="135"/>
            <polygon points="454,127 466,127 460,140"/>

            <line x1="500" y1="75" x2="500" y2="135"/>
            <polygon points="494,127 506,127 500,140"/>

            <line x1="540" y1="75" x2="540" y2="135"/>
            <polygon points="534,127 546,127 540,140"/>

            <line x1="580" y1="75" x2="580" y2="135"/>
            <polygon points="574,127 586,127 580,140"/>

            <line x1="620" y1="75" x2="620" y2="135"/>
            <polygon points="614,127 626,127 620,140"/>

            <line x1="660" y1="75" x2="660" y2="135"/>
            <polygon points="654,127 666,127 660,140"/>

            <line x1="700" y1="75" x2="700" y2="135"/>
            <polygon points="694,127 706,127 700,140"/>

            <line x1="740" y1="75" x2="740" y2="135"/>
            <polygon points="734,127 746,127 740,140"/>

            <line x1="780" y1="75" x2="780" y2="135"/>
            <polygon points="774,127 786,127 780,140"/>

            <line x1="820" y1="75" x2="820" y2="135"/>
            <polygon points="814,127 826,127 820,140"/>

        </g>


        <!-- =================================================
             LEFT MASONRY WALL
             ================================================= -->

        <rect
            x="80"
            y="210"
            width="{wall_width:.1f}"
            height="150"
            fill="url(#brickPattern)"
            stroke="#5c321b"
            stroke-width="3"
        />


        <!-- =================================================
             RIGHT MASONRY WALL
             ================================================= -->

        <rect
            x="{920 - wall_width:.1f}"
            y="210"
            width="{wall_width:.1f}"
            height="150"
            fill="url(#brickPattern)"
            stroke="#5c321b"
            stroke-width="3"
        />


        <!-- =================================================
             LEFT BEARING
             ================================================= -->

        <rect
            x="145"
            y="180"
            width="50"
            height="30"
            fill="#777"
            stroke="#333"
            stroke-width="2"
        />


        <!-- =================================================
             RIGHT BEARING
             ================================================= -->

        <rect
            x="805"
            y="180"
            width="50"
            height="30"
            fill="#777"
            stroke="#333"
            stroke-width="2"
        />


        <!-- =================================================
             RCC BEAM
             ================================================= -->

        <rect
            x="170"
            y="145"
            width="660"
            height="{beam_height:.1f}"
            fill="#c7ccd1"
            stroke="#333"
            stroke-width="3"
        />


        <!-- =================================================
             BEAM TOP EDGE
             ================================================= -->

        <line
            x1="170"
            y1="145"
            x2="830"
            y2="145"
            stroke="#222"
            stroke-width="3"
        />


        <!-- =================================================
             LOAD CONTACT MARKS
             ================================================= -->

        <g
            stroke="#333"
            stroke-width="2"
        >

            <line x1="180" y1="145" x2="175" y2="157"/>
            <line x1="220" y1="145" x2="215" y2="157"/>
            <line x1="260" y1="145" x2="255" y2="157"/>
            <line x1="300" y1="145" x2="295" y2="157"/>
            <line x1="340" y1="145" x2="335" y2="157"/>
            <line x1="380" y1="145" x2="375" y2="157"/>
            <line x1="420" y1="145" x2="415" y2="157"/>
            <line x1="460" y1="145" x2="455" y2="157"/>
            <line x1="500" y1="145" x2="495" y2="157"/>
            <line x1="540" y1="145" x2="535" y2="157"/>
            <line x1="580" y1="145" x2="575" y2="157"/>
            <line x1="620" y1="145" x2="615" y2="157"/>
            <line x1="660" y1="145" x2="655" y2="157"/>
            <line x1="700" y1="145" x2="695" y2="157"/>
            <line x1="740" y1="145" x2="735" y2="157"/>
            <line x1="780" y1="145" x2="775" y2="157"/>
            <line x1="820" y1="145" x2="815" y2="157"/>

        </g>


        <!-- =================================================
             SPAN DIMENSION LINE
             ================================================= -->

        <line
            x1="170"
            y1="410"
            x2="830"
            y2="410"
            stroke="#222"
            stroke-width="2"
        />


        <!-- =================================================
             LEFT DIMENSION ARROW
             ================================================= -->

        <polygon
            points="170,410 188,401 188,419"
            fill="#222"
        />


        <!-- =================================================
             RIGHT DIMENSION ARROW
             ================================================= -->

        <polygon
            points="830,410 812,401 812,419"
            fill="#222"
        />


        <!-- =================================================
             SPAN LABEL
             ================================================= -->

        <text
            x="500"
            y="390"
            text-anchor="middle"
            font-size="23"
            font-weight="bold"
            fill="#222"
        >
            Span, L = {L:.1f} m
        </text>


        <!-- =================================================
             CENTRE TO CENTRE
             ================================================= -->

        <text
            x="500"
            y="440"
            text-anchor="middle"
            font-size="17"
            fill="#333"
        >
            (centre-to-centre)
        </text>


        <!-- =================================================
             LEFT WALL LABEL
             ================================================= -->

        <text
            x="120"
            y="480"
            text-anchor="middle"
            font-size="17"
            font-weight="bold"
            fill="#333"
        >
            {wall_t:.0f} mm wall
        </text>


        <!-- =================================================
             RIGHT WALL LABEL
             ================================================= -->

        <text
            x="880"
            y="480"
            text-anchor="middle"
            font-size="17"
            font-weight="bold"
            fill="#333"
        >
            {wall_t:.0f} mm wall
        </text>


        <!-- =================================================
             BEAM SECTION
             ================================================= -->

        <text
            x="500"
            y="500"
            text-anchor="middle"
            font-size="15"
            fill="#555"
        >
            Beam section = {b:.0f} mm × {D:.0f} mm
        </text>


    </svg>

</div>

</body>

</html>
""",
height=570,
scrolling=False
)

# =========================================================
# DYNAMIC BEAM CROSS-SECTION — FRONT VIEW
# =========================================================

st.header("🧱 Beam Cross-Section")


# =========================================================
# DYNAMIC CALCULATIONS FOR DRAWING
# =========================================================

d_dynamic = (
    D
    - clear_cover
    - stirrup_diameter
    - main_bar_1 / 2
)


# =========================================================
# CREATE MAIN BAR LIST
# =========================================================

bar_diameters = []

for _ in range(number_bar_1):
    bar_diameters.append(main_bar_1)

for _ in range(number_bar_2):
    bar_diameters.append(main_bar_2)


total_main_bars_dynamic = len(bar_diameters)


# =========================================================
# CREATE SVG CIRCLES FOR MAIN BARS
# =========================================================

main_bars_svg = ""

if total_main_bars_dynamic == 1:

    diameter = bar_diameters[0]

    radius = max(
        7,
        min(15, diameter * 0.45)
    )

    main_bars_svg = f"""
        <circle
            cx="500"
            cy="395"
            r="{radius:.1f}"
            fill="#111"
            stroke="#000"
            stroke-width="2"
        />
    """

else:

    for i, diameter in enumerate(bar_diameters):

        x_position = (
            390
            + i * (
                220 / (total_main_bars_dynamic - 1)
            )
        )

        radius = max(
            7,
            min(15, diameter * 0.45)
        )

        main_bars_svg += f"""
            <circle
                cx="{x_position:.1f}"
                cy="395"
                r="{radius:.1f}"
                fill="#111"
                stroke="#000"
                stroke-width="2"
            />
        """


# =========================================================
# REINFORCEMENT TEXT
# =========================================================

reinforcement_text_dynamic = (
    f"{number_bar_1} - {main_bar_1:.0f}φ + "
    f"{number_bar_2} - {main_bar_2:.0f}φ"
)


# =========================================================
# CROSS-SECTION HTML + SVG
# =========================================================

components.html(
f"""
<!DOCTYPE html>

<html>

<head>

<style>

body {{
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: Arial, sans-serif;
}}

.section-container {{
    width: 100%;
    background: white;
    border: 2px solid #444;
    border-radius: 10px;
    overflow: hidden;
}}

.section-title {{
    background: #d9f2ff;
    border-bottom: 2px solid #555;
    padding: 10px 14px;
    font-size: 18px;
    font-weight: bold;
    color: #111;
}}

svg {{
    display: block;
    width: 100%;
    height: auto;
}}

</style>

</head>


<body>

<div class="section-container">


    <!-- =================================================
         TITLE
         ================================================= -->

    <div class="section-title">
        ▪ 3. CROSS-SECTION (FRONT VIEW)
    </div>


    <!-- =================================================
         SVG
         ================================================= -->

    <svg
        viewBox="0 0 1000 650"
        xmlns="http://www.w3.org/2000/svg"
    >


        <!-- =================================================
             BEAM / CONCRETE SECTION
             ================================================= -->

        <rect
            x="350"
            y="100"
            width="300"
            height="350"
            fill="#d1d5d9"
            stroke="#222"
            stroke-width="4"
        />


        <!-- =================================================
             STIRRUP
             ================================================= -->

        <rect
            x="375"
            y="125"
            width="250"
            height="300"
            fill="none"
            stroke="#333"
            stroke-width="8"
            rx="2"
        />


        <!-- =================================================
             MAIN REINFORCEMENT
             ================================================= -->

        {main_bars_svg}


        <!-- =================================================
             WIDTH DIMENSION
             ================================================= -->

        <line
            x1="350"
            y1="70"
            x2="650"
            y2="70"
            stroke="#222"
            stroke-width="2"
        />

        <polygon
            points="350,70 370,60 370,80"
            fill="#222"
        />

        <polygon
            points="650,70 630,60 630,80"
            fill="#222"
        />

        <text
            x="500"
            y="52"
            text-anchor="middle"
            font-size="23"
            font-weight="bold"
            fill="#222"
        >
            b = {b:.0f} mm
        </text>


        <!-- =================================================
             OVERALL DEPTH D
             ================================================= -->

        <line
            x1="300"
            y1="100"
            x2="300"
            y2="450"
            stroke="#222"
            stroke-width="2"
        />

        <polygon
            points="300,100 291,120 309,120"
            fill="#222"
        />

        <polygon
            points="300,450 291,430 309,430"
            fill="#222"
        />

        <text
            x="250"
            y="285"
            text-anchor="middle"
            font-size="22"
            font-weight="bold"
            fill="#222"
            transform="rotate(-90 250 285)"
        >
            D = {D:.0f} mm
        </text>


        <!-- =================================================
             EFFECTIVE DEPTH d
             ================================================= -->

        <line
            x1="690"
            y1="100"
            x2="690"
            y2="395"
            stroke="#333"
            stroke-width="2"
        />

        <polygon
            points="690,100 681,120 699,120"
            fill="#333"
        />

        <polygon
            points="690,395 681,375 699,375"
            fill="#333"
        />

        <text
            x="735"
            y="270"
            text-anchor="middle"
            font-size="21"
            font-weight="bold"
            fill="#333"
            transform="rotate(-90 735 270)"
        >
            d = {d_dynamic:.0f} mm
        </text>


        <!-- =================================================
             CLEAR COVER
             ================================================= -->

        <line
            x1="375"
            y1="425"
            x2="390"
            y2="425"
            stroke="#1565c0"
            stroke-width="3"
        />

        <line
            x1="375"
            y1="415"
            x2="375"
            y2="435"
            stroke="#1565c0"
            stroke-width="2"
        />

        <line
            x1="390"
            y1="415"
            x2="390"
            y2="435"
            stroke="#1565c0"
            stroke-width="2"
        />

        <text
            x="390"
            y="480"
            text-anchor="middle"
            font-size="17"
            font-weight="bold"
            fill="#1565c0"
        >
            Clear cover = {clear_cover:.0f} mm
        </text>


        <!-- =================================================
             STIRRUP LABEL
             ================================================= -->

        <line
            x1="625"
            y1="300"
            x2="760"
            y2="300"
            stroke="#555"
            stroke-width="2"
        />

        <circle
            cx="625"
            cy="300"
            r="5"
            fill="#555"
        />

        <text
            x="775"
            y="295"
            font-size="17"
            font-weight="bold"
            fill="#333"
        >
            Stirrup
        </text>

        <text
            x="775"
            y="320"
            font-size="17"
            fill="#333"
        >
            {stirrup_diameter:.0f} mm
        </text>


        <!-- =================================================
             REINFORCEMENT LABEL
             ================================================= -->

        <line
            x1="500"
            y1="395"
            x2="500"
            y2="525"
            stroke="#1565c0"
            stroke-width="2"
        />

        <polygon
            points="500,395 494,407 506,407"
            fill="#1565c0"
        />

        <text
            x="500"
            y="555"
            text-anchor="middle"
            font-size="19"
            font-weight="bold"
            fill="#222"
        >
            {reinforcement_text_dynamic}
        </text>


        <!-- =================================================
             TOTAL MAIN BARS
             ================================================= -->

        <text
            x="500"
            y="585"
            text-anchor="middle"
            font-size="15"
            fill="#555"
        >
            Total main bars = {total_main_bars_dynamic}
        </text>


    </svg>

</div>

</body>

</html>
""",
height=690,
scrolling=False
)
st.header("📋 Current Design Inputs")

# Row 1
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Span L",
    f"{L:.1f} m"
)

col2.metric(
    "Beam Width b",
    f"{b:.0f} mm"
)

col3.metric(
    "Beam Depth D",
    f"{D:.0f} mm"
)

col4.metric(
    "Wall Thickness",
    f"{wall_t:.0f} mm"
)

# Row 2
col5, col6, col7, col8 = st.columns(4)

col5.metric(
    "Dead Load",
    f"{dead_load:.1f} kN/m"
)

col6.metric(
    "Live Load",
    f"{live_load:.1f} kN/m"
)

col7.metric(
    "Concrete",
    f"M{fck:.0f}"
)

col8.metric(
    "Steel",
    f"Fe {fy:.0f}"
)

# Row 3
col9, col10, col11, col12 = st.columns(4)

col9.metric(
    "Cover",
    f"{clear_cover:.0f} mm"
)

col10.metric(
    "Stirrup",
    f"{stirrup_diameter:.0f} mm"
)

col11.metric(
    "Main Bar 1",
    f"{number_bar_1} × {main_bar_1:.0f}φ"
)

col12.metric(
    "Main Bar 2",
    f"{number_bar_2} × {main_bar_2:.0f}φ"
)

# =========================================================
# REINFORCEMENT SUMMARY
# =========================================================

st.subheader("🔩 Reinforcement Arrangement")

st.info(
    f"Bottom Main Reinforcement: "
    f"{number_bar_1}–{main_bar_1:.0f}φ + "
    f"{number_bar_2}–{main_bar_2:.0f}φ"
)

# =========================================================
# STEP 5 — BASIC CALCULATIONS
# =========================================================

# ---------------------------------------------------------
# Effective Depth
# ---------------------------------------------------------

effective_depth_raw = (
    D
    - clear_cover
    - stirrup_diameter
    - main_bar_1 / 2
)

effective_depth = effective_depth_raw
# ---------------------------------------------------------
# Self Weight / Load Calculation
# ---------------------------------------------------------

self_weight = (
    concrete_unit_weight
    * slab_thickness
    * tributary_width
)

total_dead_load = (
    dead_load
    + self_weight
)

service_load = (
    total_dead_load
    + live_load
)

factored_load = (
    load_factor
    * service_load
)

# =========================================================
# CALCULATION DISPLAY
# =========================================================

st.header("🧮 Step 5 — Basic Calculations")

# Effective Depth
st.subheader("1️⃣ Effective Depth")

st.latex(
    r"d = D - cover - \phi_s - \frac{\phi_1}{2}"
)

st.write(
    f"d = {D:.0f} − "
    f"{clear_cover:.0f} − "
    f"{stirrup_diameter:.0f} − "
    f"{main_bar_1:.0f}/2"
)

st.success(
    f"Effective depth, d = {effective_depth} mm"
)

# Load Calculation
st.subheader("2️⃣ Load Calculation")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Self Weight",
    f"{self_weight:.2f} kN/m"
)

col2.metric(
    "Total Dead Load",
    f"{total_dead_load:.2f} kN/m"
)

col3.metric(
    "Service Load",
    f"{service_load:.2f} kN/m"
)

col4.metric(
    "Factored Load",
    f"{factored_load:.2f} kN/m"
)

# Detailed calculation
with st.expander("📐 Show Load Calculation", expanded=True):

    st.write(
        f"Self weight = 25 × {slab_thickness:.2f} × "
        f"{tributary_width:.2f}"
        f" = **{self_weight:.2f} kN/m**"
    )

    st.write(
        f"Total dead load = {dead_load:.2f} + "
        f"{self_weight:.2f}"
        f" = **{total_dead_load:.2f} kN/m**"
    )

    st.write(
        f"Service load = {total_dead_load:.2f} + "
        f"{live_load:.2f}"
        f" = **{service_load:.2f} kN/m**"
    )

    st.write(
        f"Factored load = {load_factor:.2f} × "
        f"{service_load:.2f}"
        f" = **{factored_load:.2f} kN/m**"
    )




# =========================================================
# STEP 6 — DESIGN MOMENT & MINIMUM EFFECTIVE DEPTH CHECK
# =========================================================

st.header("📐 Step 6 — Design Moment & Depth Check")

# ---------------------------------------------------------
# Design Load
# ---------------------------------------------------------

# The book uses the displayed factored load of 28.1 kN/m
# for the design moment calculation.
design_load = round(factored_load, 1)

# ---------------------------------------------------------
# Maximum Factored Moment
# Simply supported beam with UDL
# Mu = wu L² / 8
# ---------------------------------------------------------

Mu = design_load * (L ** 2) / 8

# ---------------------------------------------------------
# Limiting Moment Parameter
# Rlim = 0.1389 fck
# ---------------------------------------------------------

R_lim = 0.1389 * fck

# ---------------------------------------------------------
# Minimum Effective Depth
#
# dmin = sqrt(Mu / (Rlim × b))
#
# Mu is converted from kNm to Nmm.
# b is in mm.
# Rlim is in N/mm².
# ---------------------------------------------------------

if R_lim > 0 and b > 0:

    d_min = (
        (Mu * 10**6)
        / (R_lim * b)
    ) ** 0.5

else:

    d_min = 0.0

# ---------------------------------------------------------
# Depth Check
# ---------------------------------------------------------

depth_check = effective_depth >= d_min

# =========================================================
# DESIGN MOMENT
# =========================================================

st.subheader("1️⃣ Maximum Factored Moment")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Factored Load",
    f"{design_load:.1f} kN/m"
)

col2.metric(
    "Span",
    f"{L:.2f} m"
)

col3.metric(
    "Design Moment Mu",
    f"{Mu:.1f} kNm"
)

with st.expander("📐 Show Design Moment Calculation", expanded=True):

    st.write(
        f"Factored load, wu = **{design_load:.1f} kN/m**"
    )

    st.write(
        f"Span, L = **{L:.2f} m**"
    )

    st.latex(
        r"M_u = \frac{w_u L^2}{8}"
    )

    st.write(
        f"Mu = {design_load:.1f} × "
        f"{L:.2f}² / 8"
        f" = **{Mu:.1f} kNm**"
    )

# =========================================================
# Rlim
# =========================================================

st.subheader("2️⃣ Limiting Moment Parameter")

col4, col5 = st.columns(2)

col4.metric(
    "Concrete Grade",
    f"M{fck:.0f}"
)

col5.metric(
    "Rlim",
    f"{R_lim:.3f} MPa"
)

st.latex(
    r"R_{lim} = 0.1389 f_{ck}"
)

st.write(
    f"Rlim = 0.1389 × {fck:.0f}"
    f" = **{R_lim:.3f} MPa**"
)

# =========================================================
# MINIMUM EFFECTIVE DEPTH
# =========================================================

st.subheader("3️⃣ Minimum Effective Depth")

col6, col7, col8 = st.columns(3)

col6.metric(
    "Required dmin",
    f"{d_min:.0f} mm"
)

col7.metric(
    "Provided d",
    f"{effective_depth:.0f} mm"
)

if depth_check:

    col8.success("✅ DEPTH ADEQUATE")

else:

    col8.error("❌ DEPTH INADEQUATE")

st.latex(
    r"d_{min} = \sqrt{\frac{M_u}{R_{lim}b}}"
)

st.write(
    f"dmin = √[({Mu:.1f} × 10⁶) / "
    f"({R_lim:.3f} × {b:.0f})]"
    f" = **{d_min:.0f} mm**"
)

# =========================================================
# FINAL DEPTH CHECK
# =========================================================

if depth_check:

    st.success(
        f"✅ Depth Check: d = {effective_depth:.0f} mm "
        f"≥ dmin = {d_min:.0f} mm — ADEQUATE"
    )

else:

    st.error(
        f"❌ Depth Check: d = {effective_depth:.0f} mm "
        f"< dmin = {d_min:.0f} mm — INADEQUATE"
    )







# =========================================================
# STEP 7 — REQUIRED STEEL AREA
# =========================================================
R = (
    Mu * 10**6
    / (b * effective_depth**2)
)

# st.header("🔩 Step 7 — Required Steel Area")
# st.write("DEBUG Mu =", Mu)
# st.write("DEBUG b =", b)
# st.write("DEBUG d =", effective_depth)
# st.write("DEBUG R =", R)
# st.write("DEBUG fck, fy =", fck, fy)
# ---------------------------------------------------------
# 1. DESIGN PARAMETER R
#
# R = Mu / (b d²)
#
# Mu = kNm → Nmm
# b, d = mm
# Therefore R = N/mm² = MPa
# ---------------------------------------------------------

# R = (
#     Mu * 10**6
#     / (b * effective_depth**2)
# )

# ---------------------------------------------------------
# 2. REQUIRED STEEL PERCENTAGE
#
# R = 0.87 fy (pt/100)
#     [1 - fy(pt/100)/fck]
#
# Let:
# x = pt/100
#
# x = fck/(2fy) *
#     [1 - sqrt(1 - 4R/(0.87 fck))]
# ---------------------------------------------------------

if fck > 0 and fy > 0:

    discriminant = (
        1
        - (4 * R) / (0.87 * fck)
    )

    if discriminant >= 0:

        pt_ratio = (
            fck / (2 * fy)
        ) * (
            1
            - discriminant**0.5
        )

        pt = 100 * pt_ratio

    else:

        pt = None

else:

    pt = None


# ---------------------------------------------------------
# 3. REQUIRED STEEL AREA
#
# Ast,req = (pt/100) × b × d
# ---------------------------------------------------------

if pt is not None:

    Ast_required = (
        (pt / 100)
        * b
        * effective_depth
    )

else:

    Ast_required = None


# =========================================================
# SECTION 1 — DESIGN PARAMETER R
# =========================================================

st.subheader("1️⃣ Design Parameter R")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Design Moment Mu",
    f"{Mu:.2f} kNm"
)

col2.metric(
    "Effective Depth d",
    f"{effective_depth:.1f} mm"
)

col3.metric(
    "R",
    f"{R:.3f} MPa"
)

with st.expander("📐 Show R Calculation", expanded=True):

    st.latex(
        r"""
        R = \frac{M_u}{bd^2}
        """
    )

    st.write(
        f"R = ({Mu:.2f} × 10⁶) / "
        f"({b:.0f} × {effective_depth:.1f}²)"
    )

    st.write(
        f"R = **{R:.3f} MPa**"
    )


# =========================================================
# SECTION 2 — REQUIRED PERCENTAGE OF STEEL
# =========================================================

st.subheader("2️⃣ Required Percentage of Steel")

st.latex(
    r"""
    R =
    0.87f_y
    \left(\frac{p_t}{100}\right)
    \left[
    1-\frac{f_y p_t}{100f_{ck}}
    \right]
    """
)

with st.expander(
    "🧮 Show Steel Percentage Calculation",
    expanded=True
):

    st.write(
        f"fck = **{fck:.0f} MPa**"
    )

    st.write(
        f"fy = **{fy:.0f} MPa**"
    )

    st.write(
        f"R = **{R:.3f} MPa**"
    )

    st.latex(
        r"""
        x=\frac{p_t}{100}
        """
    )

    st.latex(
        r"""
        x =
        \frac{f_{ck}}{2f_y}
        \left[
        1-
        \sqrt{
        1-\frac{4R}{0.87f_{ck}}
        }
        \right]
        """
    )

    if pt is not None:

        st.write(
            f"Required steel percentage:"
        )

        st.write(
            f"pₜ = **{pt:.3f} %**"
        )

    else:

        st.error(
            "❌ No valid steel percentage solution."
        )


# =========================================================
# SECTION 3 — REQUIRED STEEL AREA
# =========================================================

st.subheader("3️⃣ Required Steel Area")

st.latex(
    r"""
    A_{st,req}
    =
    \frac{p_t}{100}bd
    """
)

if Ast_required is not None:

    with st.expander(
        "📐 Show Required Steel Area Calculation",
        expanded=True
    ):

        st.write(
            f"Aₛₜ,req = ({pt:.3f}/100) × "
            f"{b:.0f} × {effective_depth:.1f}"
        )

        st.write(
            f"Aₛₜ,req = **{Ast_required:.1f} mm²**"
        )

    st.success(
        f"🔩 Required steel area = "
        f"**{Ast_required:.1f} mm²**"
    )

else:

    st.error(
        "❌ Required steel area cannot be calculated."
    )







# =========================================================
# STEP 8 — PROVIDED STEEL & REINFORCEMENT CHECK
# =========================================================

st.header("🔩 Step 8 — Provided Steel & Reinforcement Check")

# ---------------------------------------------------------
# 1. AREA OF EACH TYPE OF MAIN BAR
#
# Area of one circular bar:
#
# A = πφ² / 4
# ---------------------------------------------------------

area_bar_1 = (
    3.141592653589793
    * main_bar_1**2
    / 4
)

area_bar_2 = (
    3.141592653589793
    * main_bar_2**2
    / 4
)

# ---------------------------------------------------------
# 2. TOTAL PROVIDED STEEL AREA
#
# Ast,provided =
# (number of bar 1 × area of bar 1)
# +
# (number of bar 2 × area of bar 2)
# ---------------------------------------------------------

Ast_provided = (
    number_bar_1 * area_bar_1
    +
    number_bar_2 * area_bar_2
)

# ---------------------------------------------------------
# 3. PROVIDED STEEL PERCENTAGE
#
# pt,provided = Ast,provided / (b × d) × 100
# ---------------------------------------------------------

if b > 0 and effective_depth > 0:

    pt_provided = (
        Ast_provided
        / (b * effective_depth)
        * 100
    )

else:

    pt_provided = None

# ---------------------------------------------------------
# 4. STEEL ADEQUACY CHECK
#
# Provided steel must be >= required steel
# ---------------------------------------------------------

if Ast_required is not None:

    steel_check = (
        Ast_provided >= Ast_required
    )

else:

    steel_check = False


# =========================================================
# SECTION 1 — BAR AREA CALCULATION
# =========================================================

st.subheader("1️⃣ Main Bar Area")

col1, col2 = st.columns(2)

col1.metric(
    "Main Bar 1",
    f"{number_bar_1} × {main_bar_1:.0f}φ"
)

col2.metric(
    "Main Bar 2",
    f"{number_bar_2} × {main_bar_2:.0f}φ"
)

with st.expander(
    "📐 Show Bar Area Calculation",
    expanded=True
):

    st.write(
        f"Area of one {main_bar_1:.0f}φ bar = "
        f"π × {main_bar_1:.0f}² / 4 "
        f"= **{area_bar_1:.1f} mm²**"
    )

    st.write(
        f"Area of one {main_bar_2:.0f}φ bar = "
        f"π × {main_bar_2:.0f}² / 4 "
        f"= **{area_bar_2:.1f} mm²**"
    )


# =========================================================
# SECTION 2 — PROVIDED STEEL AREA
# =========================================================

st.subheader("2️⃣ Provided Steel Area")

st.latex(
    r"""
    A_{st,provided}
    =
    n_1\frac{\pi\phi_1^2}{4}
    +
    n_2\frac{\pi\phi_2^2}{4}
    """
)

with st.expander(
    "🔩 Show Provided Steel Calculation",
    expanded=True
):

    st.write(
        f"Aₛₜ,provided = "
        f"{number_bar_1} × π × {main_bar_1:.0f}² / 4 "
        f"+ "
        f"{number_bar_2} × π × {main_bar_2:.0f}² / 4"
    )

    st.write(
        f"Aₛₜ,provided = **{Ast_provided:.1f} mm²**"
    )

st.metric(
    "Provided Steel Area",
    f"{Ast_provided:.1f} mm²"
)


# =========================================================
# SECTION 3 — PROVIDED STEEL PERCENTAGE
# =========================================================

st.subheader("3️⃣ Provided Steel Percentage")

st.latex(
    r"""
    p_{t,provided}
    =
    \frac{A_{st,provided}}{bd}
    \times 100
    """
)

if pt_provided is not None:

    with st.expander(
        "📊 Show Provided Steel Percentage",
        expanded=True
    ):

        st.write(
            f"pₜ,provided = "
            f"({Ast_provided:.1f} / "
            f"({b:.0f} × {effective_depth:.1f})) × 100"
        )

        st.write(
            f"pₜ,provided = **{pt_provided:.3f} %**"
        )


# =========================================================
# SECTION 4 — REQUIRED vs PROVIDED STEEL
# =========================================================

st.subheader("4️⃣ Required vs Provided Steel")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Required Ast",
    f"{Ast_required:.1f} mm²"
)

col2.metric(
    "Provided Ast",
    f"{Ast_provided:.1f} mm²"
)

col3.metric(
    "Extra Steel",
    f"{Ast_provided - Ast_required:.1f} mm²"
)


# =========================================================
# FINAL STEEL ADEQUACY CHECK
# =========================================================

if steel_check:

    st.success(
        f"✅ STEEL ADEQUATE — "
        f"Ast,provided = {Ast_provided:.1f} mm² "
        f">= Ast,required = {Ast_required:.1f} mm²"
    )

else:

    st.error(
        f"❌ STEEL INADEQUATE — "
        f"Ast,provided = {Ast_provided:.1f} mm² "
        f"< Ast,required = {Ast_required:.1f} mm²"
    )


# =========================================================
# REINFORCEMENT ARRANGEMENT
# =========================================================

st.subheader("5️⃣ Reinforcement Arrangement")

st.info(
    f"Bottom Main Reinforcement: "
    f"{number_bar_1}–{main_bar_1:.0f}φ + "
    f"{number_bar_2}–{main_bar_2:.0f}φ"
)






# =========================================================
# STEP 9 — FLEXURAL STRENGTH CHECK
# =========================================================

st.header("💪 Step 9 — Flexural Strength Check")

# ---------------------------------------------------------
# DESIGN
#
# Moment of resistance using PROVIDED tension steel:
#
# MuR = 0.87 fy (pt/100)
#       [1 - fy(pt/100)/fck] b d²
#
# where:
# pt = provided percentage of tension steel
# b  = beam width
# d  = effective depth
# ---------------------------------------------------------

if (
    Ast_provided > 0
    and b > 0
    and effective_depth > 0
    and fy > 0
    and fck > 0
):

    # Provided steel percentage as decimal
    pt_provided_ratio = (
        Ast_provided
        / (b * effective_depth)
    )

    # Moment of resistance in Nmm
    MuR_Nmm = (
        0.87
        * fy
        * pt_provided_ratio
        * (
            1
            - (
                fy
                * pt_provided_ratio
                / fck
            )
        )
        * b
        * effective_depth**2
    )

    # Convert Nmm → kNm
    MuR = MuR_Nmm / 10**6

else:

    pt_provided_ratio = None
    MuR = None


# =========================================================
# SECTION 1 — PROVIDED STEEL
# =========================================================

st.subheader("1️⃣ Provided Reinforcement")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Provided Ast",
    f"{Ast_provided:.1f} mm²"
)

col2.metric(
    "Provided pt",
    f"{pt_provided:.3f} %"
)

col3.metric(
    "Effective Depth d",
    f"{effective_depth:.1f} mm"
)


# =========================================================
# SECTION 2 — MOMENT OF RESISTANCE
# =========================================================

st.subheader("2️⃣ Moment of Resistance")

st.latex(
    r"""
    M_{u,R}
    =
    0.87 f_y
    \left(\frac{p_t}{100}\right)
    \left[
    1-
    \frac{f_y p_t}{100f_{ck}}
    \right]
    bd^2
    """
)

if MuR is not None:

    with st.expander(
        "📐 Show Moment of Resistance Calculation",
        expanded=True
    ):

        st.write(
            f"fck = **{fck:.0f} MPa**"
        )

        st.write(
            f"fy = **{fy:.0f} MPa**"
        )

        st.write(
            f"pt,provided = **{pt_provided:.3f} %**"
        )

        st.write(
            f"b = **{b:.0f} mm**"
        )

        st.write(
            f"d = **{effective_depth:.1f} mm**"
        )

        st.write(
            "Moment of resistance:"
        )

        st.latex(
            r"""
            M_{u,R}
            =
            0.87 f_y
            \left(\frac{p_t}{100}\right)
            \left[
            1-
            \frac{f_y p_t}{100f_{ck}}
            \right]
            bd^2
            """
        )

        st.write(
            f"Mᵤ,R = **{MuR:.2f} kNm**"
        )

else:

    st.error(
        "❌ Moment of resistance cannot be calculated."
    )


# =========================================================
# SECTION 3 — DESIGN MOMENT VS RESISTANCE
# =========================================================

st.subheader("3️⃣ Design Moment vs Moment of Resistance")

if MuR is not None:

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Design Moment Mu",
        f"{Mu:.2f} kNm"
    )

    col2.metric(
        "Moment Resistance MuR",
        f"{MuR:.2f} kNm"
    )

    col3.metric(
        "Reserve Moment",
        f"{MuR - Mu:.2f} kNm"
    )


# =========================================================
# SECTION 4 — FLEXURAL SAFETY CHECK
# =========================================================

if MuR is not None:

    if MuR >= Mu:

        st.success(
            f"✅ FLEXURE SAFE — "
            f"Mᵤ,R = {MuR:.2f} kNm "
            f"> Mᵤ = {Mu:.2f} kNm"
        )

    else:

        st.error(
            f"❌ FLEXURE INADEQUATE — "
            f"Mᵤ,R = {MuR:.2f} kNm "
            f"< Mᵤ = {Mu:.2f} kNm"
        )






# =========================================================
# STEP 10 — REINFORCEMENT DETAILING & SPACING CHECK
# =========================================================

st.header("📏 Step 10 — Reinforcement Detailing & Spacing Check")


# =========================================================
# 1. TOTAL NUMBER OF MAIN BARS
# =========================================================

total_main_bars = (
    number_bar_1 + number_bar_2
)


# =========================================================
# 2. AVAILABLE WIDTH FOR MAIN BARS
#
# Clear cover is measured up to the outside of stirrup.
# Therefore, the width available inside the stirrups is:
#
# Available width =
# b - 2(clear cover + stirrup diameter)
# =========================================================

available_bar_width = (
    b
    - 2 * (clear_cover + stirrup_diameter)
)


# =========================================================
# 3. WIDTH OCCUPIED BY MAIN BARS
#
# Main bar width =
# n1 × φ1 + n2 × φ2
# =========================================================

main_bar_width = (
    number_bar_1 * main_bar_1
    + number_bar_2 * main_bar_2
)


# =========================================================
# 4. NUMBER OF CLEAR SPACES
#
# For one layer of bars:
#
# Number of clear spaces = total bars - 1
# =========================================================

number_of_spaces = (
    total_main_bars - 1
)


# =========================================================
# 5. CLEAR SPACING BETWEEN MAIN BARS
#
# Clear spacing =
# (available width - total bar width)
# / number of clear spaces
# =========================================================

if number_of_spaces > 0:

    clear_spacing = (
        available_bar_width
        - main_bar_width
    ) / number_of_spaces

else:

    clear_spacing = None


# =========================================================
# 6. LARGEST MAIN BAR DIAMETER
# =========================================================

largest_main_bar = max(
    main_bar_1,
    main_bar_2
)


# =========================================================
# 7. MINIMUM REQUIRED CLEAR SPACING
#
# Minimum clear spacing is governed by the greater of:
#
# 1. Diameter of the largest main bar
# 2. 2/3 of nominal maximum aggregate size
#
# =========================================================

minimum_clear_spacing = max(
    largest_main_bar,
    (2 / 3) * aggregate_size
)


# =========================================================
# 8. SPACING CHECK
# =========================================================

if clear_spacing is not None:

    spacing_check = (
        clear_spacing >= minimum_clear_spacing
    )

else:

    spacing_check = False


# =========================================================
# SECTION 1 — REINFORCEMENT ARRANGEMENT
# =========================================================

st.subheader("1️⃣ Reinforcement Arrangement")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Main Bar 1",
    f"{number_bar_1} × {main_bar_1:.0f}φ"
)

col2.metric(
    "Main Bar 2",
    f"{number_bar_2} × {main_bar_2:.0f}φ"
)

col3.metric(
    "Total Main Bars",
    f"{total_main_bars}"
)

st.info(
    f"Bottom reinforcement: "
    f"{number_bar_1}–{main_bar_1:.0f}φ + "
    f"{number_bar_2}–{main_bar_2:.0f}φ"
)


# =========================================================
# SECTION 2 — AVAILABLE WIDTH FOR MAIN BARS
# =========================================================

st.subheader("2️⃣ Available Width for Main Bars")

with st.expander(
    "📐 Show Available Width Calculation",
    expanded=True
):

    st.write(
        f"Beam width, b = **{b:.0f} mm**"
    )

    st.write(
        f"Clear cover = **{clear_cover:.0f} mm**"
    )

    st.write(
        f"Stirrup diameter = "
        f"**{stirrup_diameter:.0f} mm**"
    )

    st.write(
        f"Effective side allowance = "
        f"{clear_cover:.0f} + "
        f"{stirrup_diameter:.0f} "
        f"= **{clear_cover + stirrup_diameter:.0f} mm**"
    )

    st.write(
        f"Available width = "
        f"{b:.0f} − 2("
        f"{clear_cover:.0f} + "
        f"{stirrup_diameter:.0f})"
    )

    st.write(
        f"Available width = "
        f"**{available_bar_width:.1f} mm**"
    )


# =========================================================
# SECTION 3 — CLEAR SPACING BETWEEN MAIN BARS
# =========================================================

st.subheader("3️⃣ Clear Spacing Between Main Bars")

st.latex(
    r"""
    s_b =
    \frac{
    b-2(c+\phi_{st})
    -(n_1\phi_1+n_2\phi_2)
    }{
    (n_1+n_2)-1
    }
    """
)

if clear_spacing is not None:

    with st.expander(
        "📏 Show Clear Spacing Calculation",
        expanded=True
    ):

        st.write(
            f"s_b = ["
            f"{b:.0f} − 2("
            f"{clear_cover:.0f} + "
            f"{stirrup_diameter:.0f}) − "
            f"{number_bar_1}×{main_bar_1:.0f} − "
            f"{number_bar_2}×{main_bar_2:.0f}"
            f"] / ({total_main_bars} − 1)"
        )

        st.write(
            f"s_b = **{clear_spacing:.1f} mm**"
        )

else:

    st.warning(
        "⚠️ Clear spacing cannot be calculated "
        "because fewer than two main bars are provided."
    )


# =========================================================
# SECTION 4 — MINIMUM CLEAR SPACING REQUIREMENT
# =========================================================

st.subheader("4️⃣ Minimum Clear Spacing Requirement")

with st.expander(
    "📐 Show Minimum Spacing Check",
    expanded=True
):

    st.write(
        f"Largest main bar diameter = "
        f"**{largest_main_bar:.0f} mm**"
    )

    st.write(
        f"Nominal maximum aggregate size = "
        f"**{aggregate_size:.0f} mm**"
    )

    aggregate_spacing_limit = (
        (2 / 3) * aggregate_size
    )

    st.write(
        f"(2/3) × aggregate size = "
        f"**{aggregate_spacing_limit:.1f} mm**"
    )

    st.write(
        "Minimum required clear spacing = "
        "max(largest bar diameter, "
        "2/3 aggregate size)"
    )

    st.write(
        f"Minimum required clear spacing = "
        f"**{minimum_clear_spacing:.1f} mm**"
    )


# =========================================================
# SECTION 5 — CLEAR SPACING CHECK
# =========================================================

st.subheader("5️⃣ Clear Spacing Check")

if clear_spacing is not None:

    spacing_margin = (
        clear_spacing - minimum_clear_spacing
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Provided Clear Spacing",
        f"{clear_spacing:.1f} mm"
    )

    col2.metric(
        "Minimum Required",
        f"{minimum_clear_spacing:.1f} mm"
    )

    col3.metric(
        "Spacing Margin",
        f"{spacing_margin:.1f} mm"
    )

    if spacing_check:

        st.success(
            f"✅ SPACING ADEQUATE — "
            f"{clear_spacing:.1f} mm ≥ "
            f"{minimum_clear_spacing:.1f} mm"
        )

    else:

        st.error(
            f"❌ SPACING INADEQUATE — "
            f"{clear_spacing:.1f} mm < "
            f"{minimum_clear_spacing:.1f} mm"
        )

else:

    st.error(
        "❌ Spacing check cannot be performed."
    )


# =========================================================
# SECTION 6 — DETAILING SUMMARY
# =========================================================

st.subheader("6️⃣ Detailing Summary")

st.write(
    f"Beam width = **{b:.0f} mm**"
)

st.write(
    f"Clear cover = **{clear_cover:.0f} mm**"
)

st.write(
    f"Stirrup = **{stirrup_diameter:.0f}φ**"
)

st.write(
    f"Nominal maximum aggregate size = "
    f"**{aggregate_size:.0f} mm**"
)

st.write(
    f"Bottom reinforcement = "
    f"**{number_bar_1}–{main_bar_1:.0f}φ + "
    f"{number_bar_2}–{main_bar_2:.0f}φ**"
)

if clear_spacing is not None:

    st.write(
        f"Clear spacing = "
        f"**{clear_spacing:.1f} mm**"
    )

    st.write(
        f"Minimum required spacing = "
        f"**{minimum_clear_spacing:.1f} mm**"
    )










# =========================================================
# STEP 11 — DEFLECTION CONTROL CHECK
# =========================================================

st.header("📐 Step 11 — Deflection Control Check")


# =========================================================
# 1. EFFECTIVE SPAN
#
# Example 5.1:
#
# Effective span is the lesser of:
#
# 1. Centre-to-centre span
# 2. Clear span + 0.55 m
#
# Clear span:
#
# clear span = L - wall thickness
#
# wall_t is in mm, so convert it to metres.
# =========================================================

clear_span_m = (
    L - wall_t / 1000
)

clear_span_plus_055_m = (
    clear_span_m + 0.55
)

effective_span_m = min(
    L,
    clear_span_plus_055_m
)

effective_span_mm = (
    effective_span_m * 1000
)


# =========================================================
# 2. PROVIDED STEEL PERCENTAGE
#
# pt,provided =
# Ast,provided / (b × d) × 100
# =========================================================

if (
    Ast_provided is not None
    and b > 0
    and effective_depth > 0
):

    pt_provided = (
        Ast_provided
        / (b * effective_depth)
    ) * 100

else:

    pt_provided = None


# =========================================================
# 3. SERVICE STEEL STRESS
#
# Example 5.1:
#
# fs = 0.58 fy
#      × (Ast,required / Ast,provided)
#
# Ast_required comes from Step 7.
# Ast_provided comes from reinforcement selection.
# =========================================================

if (
    Ast_required is not None
    and Ast_provided is not None
    and Ast_provided > 0
):

    fs = (
        0.58
        * fy
        * (
            Ast_required
            / Ast_provided
        )
    )

else:

    fs = None


# =========================================================
# 4. DEFLECTION MODIFICATION FACTORS
#
# Example 5.1:
#
# k1 = 1.014
# k2 = 1.0
#
# These values are taken directly from the
# textbook worked example.
# =========================================================

k1 = 1.014
k2 = 1.0


# =========================================================
# 5. MAXIMUM PERMISSIBLE L/d
#
# (l/d)max = 20 × k1 × k2
# =========================================================

ld_max = (
    20
    * k1
    * k2
)


# =========================================================
# 6. ACTUAL L/d
#
# Actual l/d =
# effective span / effective depth
# =========================================================

if effective_depth > 0:

    actual_ld = (
        effective_span_mm
        / effective_depth
    )

else:

    actual_ld = None


# =========================================================
# 7. DEFLECTION CHECK
# =========================================================

if actual_ld is not None:

    deflection_check = (
        actual_ld <= ld_max
    )

else:

    deflection_check = False


# =========================================================
# 8. DEFLECTION MARGIN
# =========================================================

if actual_ld is not None:

    deflection_margin = (
        ld_max - actual_ld
    )

else:

    deflection_margin = None


# =========================================================
# SECTION 1 — EFFECTIVE SPAN
# =========================================================

st.subheader("1️⃣ Effective Span")

with st.expander(
    "📏 Show Effective Span Calculation",
    expanded=True
):

    st.write(
        f"Centre-to-centre span, L = "
        f"**{L:.2f} m**"
    )

    st.write(
        f"Masonry wall thickness = "
        f"**{wall_t:.0f} mm**"
    )

    st.write(
        f"Clear span = "
        f"{L:.2f} − {wall_t / 1000:.3f}"
        f" = **{clear_span_m:.3f} m**"
    )

    st.write(
        f"Clear span + 0.55 m = "
        f"{clear_span_m:.3f} + 0.55"
        f" = **{clear_span_plus_055_m:.3f} m**"
    )

    st.write(
        f"Effective span = "
        f"min({L:.2f}, "
        f"{clear_span_plus_055_m:.3f})"
    )

    st.write(
        f"Effective span = "
        f"**{effective_span_m:.3f} m**"
    )

    st.write(
        f"Effective span = "
        f"**{effective_span_mm:.0f} mm**"
    )


# =========================================================
# SECTION 2 — PROVIDED REINFORCEMENT
# =========================================================

st.subheader("2️⃣ Provided Reinforcement")

col1, col2, col3 = st.columns(3)


if Ast_provided is not None:

    col1.metric(
        "Provided Ast",
        f"{Ast_provided:.1f} mm²"
    )

else:

    col1.metric(
        "Provided Ast",
        "N/A"
    )


if pt_provided is not None:

    col2.metric(
        "Provided pt",
        f"{pt_provided:.3f} %"
    )

else:

    col2.metric(
        "Provided pt",
        "N/A"
    )


col3.metric(
    "Effective Depth d",
    f"{effective_depth:.1f} mm"
)


# =========================================================
# SECTION 3 — SERVICE STEEL STRESS
# =========================================================

st.subheader("3️⃣ Service Steel Stress")

st.latex(
    r"""
    f_s =
    0.58 f_y
    \left(
    \frac{A_{st,req}}
    {A_{st,provided}}
    \right)
    """
)

if fs is not None:

    with st.expander(
        "🧮 Show Service Stress Calculation",
        expanded=True
    ):

        st.write(
            f"fy = **{fy:.0f} MPa**"
        )

        st.write(
            f"Required steel area = "
            f"**{Ast_required:.1f} mm²**"
        )

        st.write(
            f"Provided steel area = "
            f"**{Ast_provided:.1f} mm²**"
        )

        st.write(
            f"fs = 0.58 × {fy:.0f} × "
            f"({Ast_required:.1f} / "
            f"{Ast_provided:.1f})"
        )

        st.write(
            f"fs = **{fs:.1f} MPa**"
        )

else:

    st.error(
        "❌ Service steel stress cannot be calculated."
    )


# =========================================================
# SECTION 4 — DEFLECTION MODIFICATION FACTORS
# =========================================================

st.subheader("4️⃣ Deflection Modification Factors")

with st.expander(
    "📐 Show Modification Factors",
    expanded=True
):

    st.write(
        "For Example 5.1, the textbook gives:"
    )

    st.write(
        f"k₁ = **{k1:.3f}**"
    )

    st.write(
        f"k₂ = **{k2:.1f}**"
    )

    st.info(
        "k₁ and k₂ are retained from the "
        "textbook Example 5.1."
    )


# =========================================================
# SECTION 5 — MAXIMUM PERMISSIBLE L/d
# =========================================================

st.subheader(
    "5️⃣ Maximum Permissible Span / Depth Ratio"
)

st.latex(
    r"""
    \left(\frac{l}{d}\right)_{\max}
    =
    20 k_1 k_2
    """
)

with st.expander(
    "📐 Show Maximum L/d Calculation",
    expanded=True
):

    st.write(
        f"(l/d)max = "
        f"20 × {k1:.3f} × {k2:.1f}"
    )

    st.write(
        f"(l/d)max = **{ld_max:.2f}**"
    )


# =========================================================
# SECTION 6 — ACTUAL L/d
# =========================================================

st.subheader(
    "6️⃣ Actual Span / Effective Depth Ratio"
)

if actual_ld is not None:

    with st.expander(
        "📏 Show Actual L/d Calculation",
        expanded=True
    ):

        st.write(
            f"Effective span, l = "
            f"**{effective_span_mm:.0f} mm**"
        )

        st.write(
            f"Effective depth, d = "
            f"**{effective_depth:.1f} mm**"
        )

        st.write(
            f"l/d = "
            f"{effective_span_mm:.0f} / "
            f"{effective_depth:.1f}"
        )

        st.write(
            f"l/d = **{actual_ld:.2f}**"
        )

else:

    st.error(
        "❌ Actual l/d cannot be calculated."
    )


# =========================================================
# SECTION 7 — FINAL DEFLECTION CHECK
# =========================================================

st.subheader("7️⃣ Deflection Check")

if actual_ld is not None:

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Actual l/d",
        f"{actual_ld:.2f}"
    )

    col2.metric(
        "Maximum Permissible l/d",
        f"{ld_max:.2f}"
    )

    col3.metric(
        "Deflection Margin",
        f"{deflection_margin:.2f}"
    )


    if deflection_check:

        st.success(
            f"✅ DEFLECTION — OK\n\n"
            f"Actual l/d = {actual_ld:.2f} "
            f"≤ Maximum l/d = {ld_max:.2f}"
        )

    else:

        st.error(
            f"❌ DEFLECTION — NOT OK\n\n"
            f"Actual l/d = {actual_ld:.2f} "
            f"> Maximum l/d = {ld_max:.2f}"
        )

else:

    st.error(
        "❌ Deflection check cannot be performed."
    )


# =========================================================
# SECTION 8 — TEXTBOOK COMPARISON
# =========================================================

with st.expander(
    "📖 Textbook Example 5.1 Reference"
):

    st.write(
        "The textbook gives, using its rounded "
        "intermediate values:"
    )

    st.write(
        "fs = 228.4 MPa"
    )

    st.write(
        "k₁ = 1.014"
    )

    st.write(
        "k₂ = 1.0"
    )

    st.write(
        "(l/d)max = 20.28"
    )

    st.write(
        "Actual l/d = 15.04"
    )

    st.write(
        "Therefore, deflection control is satisfactory."
    )






    # =========================================================
    # STEP 12 — FINAL DESIGN SUMMARY
    # =========================================================

    st.header("🎯 Step 12 — Final Design Summary")

    st.success(
        "✅ Final RCC Beam Design Summary"
    )

    # =========================================================
    # 1. BEAM GEOMETRY
    # =========================================================

    st.subheader("📐 1️⃣ Beam Geometry")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Span L",
        f"{L:.2f} m"
    )

    col2.metric(
        "Beam Width b",
        f"{b:.0f} mm"
    )

    col3.metric(
        "Beam Depth D",
        f"{D:.0f} mm"
    )

    col4.metric(
        "Effective Depth d",
        f"{effective_depth:.1f} mm"
    )

    # =========================================================
    # 2. EFFECTIVE SPAN
    # =========================================================

    st.subheader("📏 2️⃣ Effective Span")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Centre-to-Centre Span",
        f"{L:.2f} m"
    )

    col2.metric(
        "Clear Span",
        f"{clear_span_m:.3f} m"
    )

    col3.metric(
        "Effective Span",
        f"{effective_span_m:.3f} m"
    )

    # =========================================================
    # 3. LOAD SUMMARY
    # =========================================================

    st.subheader("⚖️ 3️⃣ Load Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Self Weight",
        f"{self_weight:.2f} kN/m"
    )

    col2.metric(
        "Dead Load",
        f"{dead_load:.2f} kN/m"
    )

    col3.metric(
        "Live Load",
        f"{live_load:.2f} kN/m"
    )

    col4.metric(
        "Factored Load",
        f"{factored_load:.2f} kN/m"
    )

    # =========================================================
    # 4. DESIGN MOMENT
    # =========================================================

    st.subheader("💪 4️⃣ Design Moment")

    col1, col2 = st.columns(2)

    col1.metric(
        "Factored Load",
        f"{design_load:.1f} kN/m"
    )

    col2.metric(
        "Design Moment Mu",
        f"{Mu:.2f} kNm"
    )

    # =========================================================
    # 5. FLEXURAL STEEL
    # =========================================================

    st.subheader("🔩 5️⃣ Flexural Reinforcement")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Required Ast",
        f"{Ast_required:.1f} mm²"
    )

    col2.metric(
        "Provided Ast",
        f"{Ast_provided:.1f} mm²"
    )

    col3.metric(
        "Provided pt",
        f"{pt_provided:.3f} %"
    )

    if steel_check:

        st.success(
            f"✅ STEEL ADEQUATE — "
            f"{Ast_provided:.1f} mm² ≥ "
            f"{Ast_required:.1f} mm²"
        )

    else:

        st.error(
            f"❌ STEEL INADEQUATE — "
            f"{Ast_provided:.1f} mm² < "
            f"{Ast_required:.1f} mm²"
        )

    # =========================================================
    # 6. REINFORCEMENT DETAILING
    # =========================================================

    st.subheader("🧱 6️⃣ Reinforcement Detailing")

    st.info(
        f"Bottom Main Reinforcement: "
        f"{number_bar_1}–{main_bar_1:.0f}φ + "
        f"{number_bar_2}–{main_bar_2:.0f}φ"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Main Bars",
        f"{total_main_bars}"
    )

    col2.metric(
        "Clear Spacing",
        f"{clear_spacing:.1f} mm"
    )

    col3.metric(
        "Minimum Required",
        f"{minimum_clear_spacing:.1f} mm"
    )

    if spacing_check:

        st.success(
            f"✅ SPACING ADEQUATE — "
            f"{clear_spacing:.1f} mm ≥ "
            f"{minimum_clear_spacing:.1f} mm"
        )

    else:

        st.error(
            f"❌ SPACING INADEQUATE — "
            f"{clear_spacing:.1f} mm < "
            f"{minimum_clear_spacing:.1f} mm"
        )

    # =========================================================
    # 7. FLEXURAL STRENGTH
    # =========================================================

    st.subheader("💪 7️⃣ Flexural Strength")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Design Moment Mu",
        f"{Mu:.2f} kNm"
    )

    col2.metric(
        "Moment Resistance MuR",
        f"{MuR:.2f} kNm"
    )

    col3.metric(
        "Reserve Moment",
        f"{MuR - Mu:.2f} kNm"
    )

    if MuR >= Mu:

        st.success(
            f"✅ FLEXURE SAFE — "
            f"MuR = {MuR:.2f} kNm ≥ "
            f"Mu = {Mu:.2f} kNm"
        )

    else:

        st.error(
            f"❌ FLEXURE INADEQUATE — "
            f"MuR = {MuR:.2f} kNm < "
            f"Mu = {Mu:.2f} kNm"
        )

    # =========================================================
    # 8. DEFLECTION
    # =========================================================

    st.subheader("📐 8️⃣ Deflection Check")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Actual l/d",
        f"{actual_ld:.2f}"
    )

    col2.metric(
        "Maximum l/d",
        f"{ld_max:.2f}"
    )

    col3.metric(
        "Deflection Margin",
        f"{deflection_margin:.2f}"
    )

    if deflection_check:

        st.success(
            f"✅ DEFLECTION OK — "
            f"{actual_ld:.2f} ≤ {ld_max:.2f}"
        )

    else:

        st.error(
            f"❌ DEFLECTION NOT OK — "
            f"{actual_ld:.2f} > {ld_max:.2f}"
        )

    # =========================================================
    # 9. FINAL DESIGN
    # =========================================================

    st.markdown("---")

    st.subheader("🏆 FINAL RCC BEAM DESIGN")

    st.success(
        f"""
    ### Beam Section

    **Beam Size:** {b:.0f} mm × {D:.0f} mm

    **Effective Depth:** {effective_depth:.1f} mm

    **Effective Span:** {effective_span_m:.3f} m

    ### Reinforcement

    **Bottom Reinforcement:** 
    {number_bar_1}–{main_bar_1:.0f}φ + 
    {number_bar_2}–{main_bar_2:.0f}φ

    **Provided Steel:** {Ast_provided:.1f} mm²

    **Required Steel:** {Ast_required:.1f} mm²

    **Clear Spacing:** {clear_spacing:.1f} mm

    ### Final Checks

    **Steel:** {"✅ ADEQUATE" if steel_check else "❌ INADEQUATE"}

    **Spacing:** {"✅ ADEQUATE" if spacing_check else "❌ INADEQUATE"}

    **Flexure:** {"✅ SAFE" if MuR >= Mu else "❌ INADEQUATE"}

    **Deflection:** {"✅ OK" if deflection_check else "❌ NOT OK"}
    """
    )








