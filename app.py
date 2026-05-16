import streamlit as st
import pandas as pd
import random
import time
import plotly.express as px

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="AI ERP Analyzer",
    page_icon="🚀",
    layout="wide"
)

# ============================================
# CUSTOM CSS
# ============================================

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to bottom right, #0E1117, #111827);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161B22;
    border-right: 1px solid #30363D;
}

/* Cards */
div[data-testid="metric-container"] {
    background-color: #161B22;
    border: 1px solid #30363D;
    padding: 18px;
    border-radius: 15px;
    transition: 0.3s ease;
}

/* Hover Effect */
div[data-testid="metric-container"]:hover {
    transform: translateY(-5px);
    border: 1px solid #2EA043;
    box-shadow: 0px 0px 20px rgba(46,160,67,0.5);
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(to right, #238636, #2EA043);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-weight: bold;
}

/* Inputs */
.stTextInput input {
    background-color: #161B22 !important;
    color: white !important;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background-color: #161B22;
    border-radius: 12px;
    border: 1px solid #30363D;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# LOGIN INFO
# ============================================

USERNAME = "admin"
PASSWORD = "password123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ============================================
# LANDING PAGE + LOGIN
# ============================================

if not st.session_state.logged_in:

    st.markdown(
        """
        <div style='text-align:center; padding-top:40px;'>

            <h1 style='font-size:3.5rem;'>
                🚀 AI ERP ANALYTICS PLATFORM
            </h1>

            <p style='font-size:1.3rem; color:#9CA3AF;'>
                Smarter business intelligence powered by AI
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("## ✨ Platform Features")

        st.markdown("""
- 📊 Interactive ERP Analytics
- 🤖 AI Business Insights
- 📈 Smart Forecasting
- 🌐 Cloud Hosted Dashboard
- 📱 Mobile Optimized UI
- ⚡ Premium SaaS Experience
""")

        st.divider()

        st.markdown("## 🔐 Secure Login")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if username == USERNAME and password == PASSWORD:

                st.session_state.logged_in = True

                st.success("Login successful ✅")

                st.rerun()

            else:

                st.error("Invalid username or password ❌")

# ============================================
# MAIN APP
# ============================================

else:

    # ============================================
    # SIDEBAR
    # ============================================

    st.sidebar.title("📌 Dashboard")

    st.sidebar.info("""
AI ERP Analyzer

Features:
- ERP Analysis
- AI Forecasting
- Smart Recommendations
- Interactive Charts
""")

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()

    # ============================================
    # HEADER
    # ============================================

    st.title("🚀 AI-Powered Odoo ERP Analyzer")

    st.markdown(
        "## Smart insights from your business data"
    )

    st.divider()

    # ============================================
    # FILE UPLOAD
    # ============================================

    uploaded_file = st.file_uploader(
        "📂 Upload your ERP CSV file",
        type=["csv"]
    )

    # ============================================
    # DATA ANALYSIS
    # ============================================

    if uploaded_file is not None:

        # ============================================
        # LOADING ANIMATION
        # ============================================

        with st.spinner(
            "🤖 AI is analyzing your ERP data..."
        ):

            progress_bar = st.progress(0)

            for i in range(100):

                time.sleep(0.01)

                progress_bar.progress(i + 1)

        st.success("Analysis complete ✅")

        # ============================================
        # READ CSV
        # ============================================

        df = pd.read_csv(uploaded_file)

        st.subheader("📋 Uploaded Data")

        st.dataframe(
            df,
            use_container_width=True
        )

        # ============================================
        # SUMMARY
        # ============================================

        summary = (
            df.groupby("Product")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        summary_df = summary.reset_index()

        summary_df.columns = ["Product", "Sales"]

        # ============================================
        # KPI METRICS
        # ============================================

        total_sales = int(summary.sum())

        top_product = summary.idxmax()

        lowest_product = summary.idxmin()

        avg_sales = int(summary.mean())

        growth_percent = random.randint(5, 20)

        predicted_sales = int(
            total_sales * (1 + growth_percent / 100)
        )

        health_score = random.randint(75, 98)

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric(
            "💰 Total Sales",
            total_sales
        )

        col2.metric(
            "🏆 Top Product",
            top_product
        )

        col3.metric(
            "📉 Lowest Product",
            lowest_product
        )

        col4.metric(
            "📊 Avg Sales",
            avg_sales
        )

        col5.metric(
            "⚡ Health Score",
            f"{health_score}%"
        )

        st.divider()

        # ============================================
        # CHART
        # ============================================

        st.subheader("📈 Interactive Sales Chart")

        fig = px.bar(
            summary_df,
            x="Product",
            y="Sales",
            text="Sales",
            title="Product Sales Analysis"
        )

        fig.update_layout(
            template="plotly_dark",
            plot_bgcolor="#0E1117",
            paper_bgcolor="#0E1117",
            font_color="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # ============================================
        # AI FORECAST
        # ============================================

        st.subheader("📈 AI Forecast")

        st.info(
            f"Projected growth next month: "
            f"{growth_percent}%"
        )

        st.success(
            f"Predicted sales next month: "
            f"{predicted_sales}"
        )

        st.divider()

        # ============================================
        # AI INSIGHTS
        # ============================================

        st.subheader("🤖 AI Insights")

        st.success(
            f"{top_product} is currently "
            f"the best-performing product."
        )

        st.error(
            f"{lowest_product} is currently "
            f"the lowest-performing product."
        )

        st.divider()

        # ============================================
        # AI CHAT
        # ============================================

        st.subheader(
            "💬 Ask AI About Your Business Data"
        )

        question = st.text_input(
            "Ask your business question..."
        )

        if question:

            q = question.lower()

            if "top" in q or "best" in q:

                st.success(
                    f"{top_product} is the "
                    f"top-performing product."
                )

            elif "lowest" in q or "worst" in q:

                st.error(
                    f"{lowest_product} is the "
                    f"lowest-performing product."
                )

            elif "forecast" in q:

                st.info(
                    f"Predicted sales next month: "
                    f"{predicted_sales}"
                )

            elif "summary" in q:

                st.success(
                    f"Total sales are "
                    f"{total_sales}."
                )

            elif "health" in q:

                st.info(
                    f"Business health score: "
                    f"{health_score}%"
                )

            else:

                st.warning("""
Try asking:
- top products
- forecast
- health
- summary
- lowest product
""")

    else:

        st.info(
            "📁 Upload a CSV file to start analysis."
        )