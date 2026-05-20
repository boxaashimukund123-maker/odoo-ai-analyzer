import streamlit as st
import pandas as pd
import time

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Odoo AI Analyzer",
    page_icon="🤖",
    layout="wide"
)

# =========================================
# SESSION
# =========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================================
# CSS
# =========================================

st.markdown("""
<style>

/* BACKGROUND */

.stApp {

    background: linear-gradient(
        135deg,
        #020617,
        #00113a,
        #0f172a
    );

    color: white;
}

/* PARTICLES */

.particles {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    overflow: hidden;
    z-index: -1;
}

.particle {
    position: absolute;
    width: 10px;
    height: 10px;
    background: rgba(59,130,246,0.5);
    border-radius: 50%;
    animation: float 16s linear infinite;
}

.particle:nth-child(1) {
    left: 10%;
    animation-duration: 12s;
}

.particle:nth-child(2) {
    left: 25%;
    animation-duration: 18s;
}

.particle:nth-child(3) {
    left: 50%;
    animation-duration: 15s;
}

.particle:nth-child(4) {
    left: 75%;
    animation-duration: 20s;
}

.particle:nth-child(5) {
    left: 90%;
    animation-duration: 13s;
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

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background: rgba(10,10,20,0.8);

    backdrop-filter: blur(12px);

    border-right: 1px solid rgba(255,255,255,0.08);
}

/* BUTTONS */

.stButton > button {

    width: 100%;

    border-radius: 14px;

    padding: 12px;

    font-size: 18px;

    font-weight: bold;

    border: none;

    color: white;

    background: linear-gradient(
        135deg,
        #2563eb,
        #3b82f6
    );

    transition: 0.3s ease;
}

.stButton > button:hover {

    transform: scale(1.03);

    box-shadow:
        0px 0px 30px rgba(59,130,246,0.7);
}

/* INPUTS */

.stTextInput input {

    background: rgba(255,255,255,0.06) !important;

    color: white !important;

    border-radius: 12px !important;
}

/* KPI CARDS */

.card {

    padding: 25px;

    border-radius: 22px;

    text-align: center;

    transition: 0.3s ease;

    color: white;
}

.card:hover {

    transform: translateY(-10px) scale(1.02);

    box-shadow:
        0px 0px 30px rgba(59,130,246,0.45);
}

.blue {
    background: linear-gradient(135deg,#2563eb,#1e3a8a);
}

.green {
    background: linear-gradient(135deg,#16a34a,#14532d);
}

.orange {
    background: linear-gradient(135deg,#d97706,#78350f);
}

.purple {
    background: linear-gradient(135deg,#9333ea,#581c87);
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
# LOGIN
# =========================================

if not st.session_state.logged_in:

    st.title("🤖 Odoo AI Analyzer")

    st.subheader(
        "AI-powered ERP analytics platform"
    )

    st.write("")

    username = st.text_input("👤 Username")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    if st.button("🚀 Login"):

        if username == "admin" and password == "admin":

            st.session_state.logged_in = True

            st.rerun()

        else:

            st.error("Wrong username or password")

# =========================================
# MAIN APP
# =========================================

else:

    st.sidebar.title("🤖 Odoo AI")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Analyzer",
            "AI Insights"
        ]
    )

    # DASHBOARD

    if page == "Dashboard":

        st.title("🚀 Odoo AI Dashboard")

        st.success(
            "AI systems operational • Live monitoring enabled"
        )

        st.write("")

        # KPI CARDS

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown("""
            <div class="card blue">
            <h3>💰 Revenue</h3>
            <h1>$128K</h1>
            <p>+18%</p>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="card green">
            <h3>👥 Users</h3>
            <h1>4,231</h1>
            <p>+9%</p>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown("""
            <div class="card orange">
            <h3>📦 Orders</h3>
            <h1>1,284</h1>
            <p>+12%</p>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown("""
            <div class="card purple">
            <h3>🤖 AI Score</h3>
            <h1>98%</h1>
            <p>Stable</p>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.write("")

        # ANIMATED COUNTERS

        st.subheader("📈 Business Growth")

        chart = st.empty()

        data = [5, 8, 12, 18, 24, 32, 41]

        chart.line_chart(data)

        st.write("")
        st.write("")

        # PROGRESS

        st.subheader("⚡ System Performance")

        st.write("AI Processing")
        st.progress(92)

        st.write("Server Stability")
        st.progress(99)

        st.write("Customer Satisfaction")
        st.progress(87)

    # ANALYZER

    if page == "Analyzer":

        st.title("📂 ERP Data Analyzer")

        uploaded_file = st.file_uploader(
            "Upload CSV File",
            type=["csv"]
        )

        if uploaded_file is not None:

            df = pd.read_csv(uploaded_file)

            st.success("CSV uploaded successfully!")

            st.dataframe(df)

            numeric_cols = df.select_dtypes(
                include="number"
            ).columns

            if len(numeric_cols) > 0:

                selected_col = st.selectbox(
                    "Choose column",
                    numeric_cols
                )

                st.line_chart(df[selected_col])

                st.bar_chart(df[selected_col])

    # AI INSIGHTS

    if page == "AI Insights":

        st.title("🧠 AI Business Insights")

        st.info(
            "AI predicts 21% sales growth next quarter."
        )

        st.success(
            "Customer engagement increased this week."
        )

        st.warning(
            "Inventory for Product A may run low soon."
        )

st.divider()

st.caption(
    "🌐 Odoo AI Analyzer • Powered by Streamlit + AI"
)