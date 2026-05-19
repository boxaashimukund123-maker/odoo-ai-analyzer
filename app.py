import streamlit as st
import pandas as pd
import time

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI ERP Platform",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# LOGIN SESSION
# =========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================================
# PREMIUM CSS
# =========================================

st.markdown("""
<style>

/* APP BACKGROUND */

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
}

/* AURORA */

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
    top: 0;
    left: 0;
    z-index: -1;
}

.particle {
    position: absolute;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(59,130,246,0.7);
    animation: float 18s linear infinite;
}

.particle:nth-child(1) {
    left: 10%;
    animation-duration: 12s;
}

.particle:nth-child(2) {
    left: 30%;
    animation-duration: 16s;
}

.particle:nth-child(3) {
    left: 50%;
    animation-duration: 20s;
}

.particle:nth-child(4) {
    left: 70%;
    animation-duration: 14s;
}

.particle:nth-child(5) {
    left: 90%;
    animation-duration: 18s;
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

/* LOGIN CARD */

.login-card {

    max-width: 500px;

    margin: auto;

    margin-top: 100px;

    padding: 40px;

    border-radius: 24px;

    background: rgba(255,255,255,0.08);

    backdrop-filter: blur(18px);

    border: 1px solid rgba(255,255,255,0.1);

    text-align: center;

    box-shadow:
        0px 0px 40px rgba(59,130,246,0.25);

    animation: floatCard 4s ease-in-out infinite;
}

/* FLOATING CARD */

@keyframes floatCard {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-8px);
    }

    100% {
        transform: translateY(0px);
    }
}

/* LOGIN TITLE */

.login-title {

    font-size: 52px;

    font-weight: bold;

    margin-bottom: 10px;

    color: white;
}

/* LOGIN SUBTITLE */

.login-sub {

    color: #CBD5E1;

    font-size: 18px;

    margin-bottom: 25px;
}

/* INPUTS */

.stTextInput input {

    background: rgba(255,255,255,0.06) !important;

    color: white !important;

    border-radius: 12px !important;
}

/* BUTTON */

.stButton > button {

    width: 100%;

    border-radius: 14px;

    padding: 14px;

    font-size: 18px;

    font-weight: bold;

    border: none;

    color: white;

    background: linear-gradient(
        135deg,
        #2563eb,
        #3b82f6
    );

    box-shadow:
        0px 0px 20px rgba(59,130,246,0.5);

    transition: 0.3s ease;
}

.stButton > button:hover {

    transform: scale(1.03);

    box-shadow:
        0px 0px 40px rgba(59,130,246,0.9);
}

/* HERO LINE */

.hero-line {

    width: 100%;
    height: 5px;

    border-radius: 999px;

    background: rgba(255,255,255,0.08);

    overflow: hidden;

    margin-top: 20px;
    margin-bottom: 40px;
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

/* GLASS CARDS */

.glass {

    background: rgba(255,255,255,0.06);

    backdrop-filter: blur(14px);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 20px;

    padding: 25px;

    transition: 0.3s ease;

    animation: floatCard 4s ease-in-out infinite;
}

.glass:hover {

    transform: translateY(-10px);

    box-shadow:
        0px 0px 35px rgba(59,130,246,0.35);
}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background: rgba(10,10,20,0.75);

    backdrop-filter: blur(12px);
}

</style>
""", unsafe_allow_html=True)

# =========================================
# PARTICLES
# =========================================

st.markdown("""
<div class="particles">

<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>

</div>
""", unsafe_allow_html=True)

# =========================================
# LOGIN PAGE
# =========================================

if not st.session_state.logged_in:

    st.markdown("""
    <div class="login-card">

        <div class="login-title">
            🚀 AI ERP
        </div>

        <div class="login-sub">
            Next generation AI business intelligence platform
        </div>

    </div>
    """, unsafe_allow_html=True)

    username = st.text_input("👤 Username")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    if st.button("✨ Login"):

        if username == "admin" and password == "admin":

            st.session_state.logged_in = True

            st.success("Login successful 🚀")

            time.sleep(1)

            st.rerun()

        else:
            st.error("Invalid credentials")

# =========================================
# MAIN APP
# =========================================

else:

    st.sidebar.title("🚀 AI ERP")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Analyzer"
        ]
    )

    # HOME PAGE

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

                st.markdown(f"### 🤖 {text}")

                time.sleep(0.03)

        st.write("")
        st.write("")

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

    # ANALYZER PAGE

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