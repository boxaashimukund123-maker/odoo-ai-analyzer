import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI ERP Platform",
    page_icon="🚀",
    layout="wide"
)

# =========================
# CSS + ANIMATIONS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        -45deg,
        #020617,
        #00113a,
        #0f172a,
        #111827
    );

    background-size: 400% 400%;

    animation: gradientMove 12s ease infinite;

    color: white;
}

/* ANIMATED BACKGROUND */

@keyframes gradientMove {

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

/* FLOATING PARTICLES */

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
    width: 6px;
    height: 6px;
    background: rgba(59,130,246,0.7);
    border-radius: 50%;
    animation: float 15s linear infinite;
}

.particle:nth-child(1) {
    left: 10%;
    animation-duration: 10s;
}

.particle:nth-child(2) {
    left: 25%;
    animation-duration: 14s;
}

.particle:nth-child(3) {
    left: 40%;
    animation-duration: 18s;
}

.particle:nth-child(4) {
    left: 60%;
    animation-duration: 12s;
}

.particle:nth-child(5) {
    left: 80%;
    animation-duration: 20s;
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

/* HERO LINE */

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

/* FEATURE CARDS */

.feature-card {
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 20px;
    color: white;
    font-size: 18px;
    font-weight: 500;
    transition: 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-6px);
}

.blue {
    background: linear-gradient(135deg, #1e3a8a, #0f172a);
}

.green {
    background: linear-gradient(135deg, #14532d, #052e16);
}

.yellow {
    background: linear-gradient(135deg, #713f12, #422006);
}

/* GLOW BUTTON */

.stButton > button {

    width: 100%;

    border-radius: 14px;

    padding: 14px;

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
        0px 0px 15px rgba(37,99,235,0.35);

    transition: 0.3s ease;
}

.stButton > button:hover {

    transform: scale(1.05);

    box-shadow:
        0px 0px 35px rgba(59,130,246,0.75);

    background: linear-gradient(
        135deg,
        #3b82f6,
        #2563eb
    );
}

</style>
""", unsafe_allow_html=True)

# =========================
# PARTICLES
# =========================

st.markdown("""
<div class="particles">

    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>

</div>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================

st.title("🚀 AI ERP PLATFORM")

st.subheader(
    "Smarter business intelligence powered by AI"
)

st.markdown(
    '<div class="hero-line"></div>',
    unsafe_allow_html=True
)

# =========================
# BUTTON
# =========================

col1, col2, col3 = st.columns([1,1,1])

with col2:

    if st.button("🚀 Launch Platform"):
        st.session_state.page = "analyzer"

# =========================
# ANALYZER
# =========================

if st.session_state.get("page") == "analyzer":

    st.divider()

    st.header("📊 ERP Analyzer Dashboard")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("CSV uploaded successfully!")

        st.subheader("📄 Data Preview")

        st.dataframe(df)

        st.subheader("📈 Dataset Info")

        c1, c2, c3 = st.columns(3)

        c1.metric("Rows", len(df))
        c2.metric("Columns", len(df.columns))
        c3.metric("Missing Values", df.isnull().sum().sum())

        st.subheader("🧠 AI Insights")

        numeric_cols = df.select_dtypes(include="number")

        if not numeric_cols.empty:

            st.dataframe(
                numeric_cols.describe().round(2)
            )

        else:
            st.warning("No numeric columns found.")

# =========================
# FEATURES
# =========================

st.write("")
st.write("")

st.header("✨ Platform Features")

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
    <div class="feature-card blue">
    📊 Analytics<br><br>
    Advanced ERP analytics with real-time business insights.
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="feature-card green">
    🤖 AI Forecasting<br><br>
    Predict future growth with AI.
    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown("""
    <div class="feature-card yellow">
    ⚡ Smart Insights<br><br>
    AI recommendations for ERP systems.
    </div>
    """, unsafe_allow_html=True)

# =========================
# STATS
# =========================

st.write("")
st.write("")

st.header("📈 Trusted Worldwide")

s1, s2, s3, s4 = st.columns(4)

s1.metric("Businesses", "10K+")
s2.metric("Uptime", "99.9%")
s3.metric("Reports", "1M+")
s4.metric("Monitoring", "24/7")

# =========================
# PRICING
# =========================

st.write("")
st.write("")

st.header("💎 Pricing")

p1, p2, p3 = st.columns(3)

with p1:
    st.subheader("Starter")
    st.write("$9/month")
    st.write("Basic analytics")
    st.write("AI insights")

with p2:
    st.subheader("Pro")
    st.write("$49/month")
    st.write("Advanced AI")
    st.write("Unlimited dashboards")

with p3:
    st.subheader("Enterprise")
    st.write("$199/month")
    st.write("Custom AI solutions")
    st.write("Priority support")

st.divider()

st.caption("🌐 Built with Streamlit + AI")