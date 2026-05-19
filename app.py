import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="AI ERP Platform",
    page_icon="🚀",
    layout="wide"
)

# ========================================
# MASSIVE PREMIUM CSS
# ========================================

st.markdown("""
<style>

/* MAIN APP */

.stApp {

    background: linear-gradient(
        -45deg,
        #020617,
        #00113a,
        #0f172a,
        #111827,
        #1e1b4b
    );

    background-size: 400% 400%;

    animation: aurora 15s ease infinite;

    color: white;

    overflow-x: hidden;
}

/* AURORA BACKGROUND */

@keyframes aurora {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

/* PARTICLES */

.particles {
    position: fixed;
    width: 100%;
    height: 100%;
    overflow: hidden;
    top: 0;
    left: 0;
    z-index: -1;
}

.particle {
    position: absolute;
    width: 8px;
    height: 8px;
    background: rgba(59,130,246,0.6);
    border-radius: 50%;
    animation: float 18s linear infinite;
    filter: blur(1px);
}

.particle:nth-child(1) {
    left: 10%;
    animation-duration: 10s;
}

.particle:nth-child(2) {
    left: 25%;
    animation-duration: 16s;
}

.particle:nth-child(3) {
    left: 45%;
    animation-duration: 13s;
}

.particle:nth-child(4) {
    left: 65%;
    animation-duration: 20s;
}

.particle:nth-child(5) {
    left: 80%;
    animation-duration: 14s;
}

@keyframes float {

    0% {
        transform: translateY(100vh);
        opacity: 0;
    }

    10% {
        opacity: 1;
    }

    100% {
        transform: translateY(-10vh);
        opacity: 0;
    }
}

/* HERO */

.hero-line {

    width: 100%;
    height: 5px;

    border-radius: 999px;

    background: rgba(255,255,255,0.08);

    overflow: hidden;

    margin-top: 25px;
    margin-bottom: 45px;
}

.hero-line::before {

    content: "";

    display: block;

    width: 40%;
    height: 100%;

    background: linear-gradient(
        90deg,
        transparent,
        #3b82f6,
        transparent
    );

    animation: slide 2s linear infinite;
}

@keyframes slide {

    0% {
        transform: translateX(-150%);
    }

    100% {
        transform: translateX(350%);
    }
}

/* FLOATING GLASS CARDS */

.glass {

    background: rgba(255,255,255,0.06);

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 22px;

    padding: 28px;

    transition: 0.35s ease;

    animation: floatCard 4s ease-in-out infinite;
}

.glass:hover {

    transform: translateY(-10px) scale(1.02);

    box-shadow:
        0px 0px 35px rgba(59,130,246,0.35);
}

@keyframes floatCard {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-6px);
    }

    100% {
        transform: translateY(0px);
    }
}

/* GLOW BUTTON */

.stButton > button {

    width: 100%;

    border-radius: 16px;

    padding: 15px;

    font-size: 18px;

    font-weight: bold;

    color: white;

    border: none;

    background: linear-gradient(
        135deg,
        #2563eb,
        #1d4ed8
    );

    box-shadow:
        0px 0px 18px rgba(37,99,235,0.45);

    transition: 0.3s ease;

    animation: pulse 2s infinite;
}

.stButton > button:hover {

    transform: scale(1.05);

    box-shadow:
        0px 0px 40px rgba(59,130,246,0.9);
}

@keyframes pulse {

    0% {
        box-shadow:
            0px 0px 15px rgba(37,99,235,0.4);
    }

    50% {
        box-shadow:
            0px 0px 35px rgba(59,130,246,0.8);
    }

    100% {
        box-shadow:
            0px 0px 15px rgba(37,99,235,0.4);
    }
}

/* COUNTERS */

.metric-box {

    text-align: center;

    padding: 20px;

    border-radius: 18px;

    background: rgba(255,255,255,0.05);

    backdrop-filter: blur(10px);

    border: 1px solid rgba(255,255,255,0.08);
}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background: rgba(10,10,20,0.75);

    backdrop-filter: blur(12px);

    border-right: 1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# ========================================
# PARTICLES
# ========================================

st.markdown("""
<div class="particles">

<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>

</div>
""", unsafe_allow_html=True)

# ========================================
# SIDEBAR
# ========================================

st.sidebar.title("🚀 AI ERP")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Analyzer"
    ]
)

# ========================================
# HOME PAGE
# ========================================

if page == "Home":

    st.title("🚀 AI ERP PLATFORM")

    st.subheader(
        "Smarter business intelligence powered by AI"
    )

    st.markdown(
        '<div class="hero-line"></div>',
        unsafe_allow_html=True
    )

    # TYPING EFFECT

    with st.empty():

        text = ""

        for char in "Analyzing future business intelligence...":

            text += char

            st.markdown(
                f"### 🤖 {text}"
            )

            time.sleep(0.03)

    st.write("")
    st.write("")

    # BUTTON

    col1, col2, col3 = st.columns([1,1,1])

    with col2:

        if st.button("🚀 Launch Platform"):

            st.success(
                "Open the Analyzer tab from the sidebar 🔥"
            )

    st.write("")
    st.write("")

    # FLOATING GLASS CARDS

    st.header("✨ Platform Features")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="glass">

        <h2>📊 Analytics</h2>

        <p>
        Advanced ERP analytics with
        real-time business insights.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="glass">

        <h2>🤖 AI Forecasting</h2>

        <p>
        Predict future growth with AI.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="glass">

        <h2>⚡ Smart Insights</h2>

        <p>
        AI recommendations for ERP systems.
        </p>

        </div>
        """, unsafe_allow_html=True)

    # ANIMATED COUNTERS

    st.write("")
    st.write("")

    st.header("📈 Trusted Worldwide")

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.markdown("""
        <div class="metric-box">
        <h1>10K+</h1>
        <p>Businesses</p>
        </div>
        """, unsafe_allow_html=True)

    with s2:
        st.markdown("""
        <div class="metric-box">
        <h1>99.9%</h1>
        <p>Uptime</p>
        </div>
        """, unsafe_allow_html=True)

    with s3:
        st.markdown("""
        <div class="metric-box">
        <h1>1M+</h1>
        <p>Reports</p>
        </div>
        """, unsafe_allow_html=True)

    with s4:
        st.markdown("""
        <div class="metric-box">
        <h1>24/7</h1>
        <p>Monitoring</p>
        </div>
        """, unsafe_allow_html=True)

# ========================================
# ANALYZER PAGE
# ========================================

if page == "Analyzer":

    st.title("📊 ERP Analyzer Dashboard")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("CSV uploaded successfully!")

        st.subheader("📄 Data Preview")

        st.dataframe(df)

        # CHARTS

        st.subheader("📈 Live Charts")

        numeric_cols = df.select_dtypes(
            include="number"
        ).columns

        if len(numeric_cols) > 0:

            selected_col = st.selectbox(
                "Choose a column",
                numeric_cols
            )

            st.line_chart(df[selected_col])

            st.bar_chart(df[selected_col])

        # INFO

        st.subheader("🧠 AI Insights")

        numeric_df = df.select_dtypes(
            include="number"
        )

        if not numeric_df.empty:

            st.dataframe(
                numeric_df.describe().round(2)
            )

st.divider()

st.caption("🌐 Built with Streamlit + AI")