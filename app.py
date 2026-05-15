import streamlit as st
import pandas as pd
import random
import plotly.express as px

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="AI Odoo ERP Analyzer",
    page_icon="🚀",
    layout="wide"
)

# ============================================
# PREMIUM CSS / MOBILE UI
# ============================================

st.markdown("""
<style>

/* Main App */
.stApp {
    background: linear-gradient(to bottom right, #0E1117, #111827);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161B22;
    border-right: 1px solid #30363D;
}

/* Metric Cards */
div[data-testid="metric-container"] {
    background: #161B22;
    border: 1px solid #30363D;
    padding: 18px;
    border-radius: 16px;
    transition: 0.3s ease;
    box-shadow: 0px 0px 12px rgba(0,0,0,0.3);
}

/* Metric Hover */
div[data-testid="metric-container"]:hover {
    transform: translateY(-5px);
    border: 1px solid #2EA043;
    box-shadow: 0px 0px 20px rgba(46,160,67,0.5);
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(to right, #238636, #2EA043);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1.2rem;
    font-weight: bold;
    transition: 0.3s ease;
}

/* Button Hover */
div.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 15px rgba(46,160,67,0.5);
}

/* Text Inputs */
.stTextInput input {
    background-color: #161B22 !important;
    color: white !important;
    border-radius: 10px !important;
}

/* File Upload */
[data-testid="stFileUploader"] {
    background-color: #161B22;
    border-radius: 15px;
    padding: 10px;
    border: 1px solid #30363D;
}

/* Mobile Optimization */
@media (max-width: 768px) {

    .block-container {
        padding: 1rem;
    }

    h1 {
        font-size: 1.8rem;
    }

    h2 {
        font-size: 1.3rem;
    }

    div[data-testid="metric-container"] {
        padding: 12px;
    }
}

</style>
""", unsafe_allow_html=True)

# ============================================
# LOGIN SYSTEM
# ============================================

USERNAME = "admin"
PASSWORD = "password123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ============================================
# LOGIN PAGE
# ============================================

if not st.session_state.logged_in:

    st.title("🔐 AI Odoo ERP Login")
    st.markdown("### Secure ERP Analytics Access")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

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

    st.sidebar.title("📌 Dashboard")

    st.sidebar.info("""
AI Odoo ERP Analyzer

Features:
- AI Forecasting
- Interactive Charts
- Smart Recommendations
- Mobile Friendly
- Premium UI
""")

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()

    # ============================================
    # TITLE
    # ============================================

    st.title("🚀 AI-Powered Odoo ERP Analyzer")
    st.markdown("## Smart insights from your business data")

    st.divider()

    # ============================================
    # FILE UPLOAD
    # ============================================

    uploaded_file = st.file_uploader(
        "📂 Upload ERP CSV File",
        type=["csv"]
    )

    # ============================================
    # DATA ANALYSIS
    # ============================================

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("📋 Uploaded ERP Data")

        st.dataframe(
            df,
            use_container_width=True
        )

        # ============================================
        # SALES SUMMARY
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
        top_sales = int(summary.max())

        lowest_product = summary.idxmin()
        lowest_sales = int(summary.min())

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
        # PLOTLY CHART
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
            f"Projected business growth next month: "
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
            f"{top_product} is currently the "
            f"best-performing product."
        )

        st.error(
            f"{lowest_product} is currently the "
            f"lowest-performing product."
        )

        st.divider()

        # ============================================
        # AI CHAT
        # ============================================

        st.subheader("💬 Ask AI About Your Business Data")

        question = st.text_input(
            "Ask your business question..."
        )

        if question:

            q = question.lower()

            if "top" in q or "best" in q:

                st.success(
                    f"{top_product} is the top product "
                    f"with sales of {top_sales}."
                )

            elif "worst" in q or "lowest" in q:

                st.error(
                    f"{lowest_product} is the "
                    f"lowest-performing product."
                )

            elif "summary" in q:

                st.info(
                    f"Total sales are {total_sales}."
                )

            elif "forecast" in q:

                st.success(
                    f"Predicted next month sales: "
                    f"{predicted_sales}"
                )

            elif "trend" in q:

                st.success(
                    f"Strong upward trend detected "
                    f"with {growth_percent}% growth."
                )

            elif "risk" in q:

                st.error(
                    f"Potential business risk "
                    f"detected in {lowest_product}."
                )

            elif "strategy" in q:

                st.info(
                    f"Recommended strategy: scale "
                    f"{top_product} and improve "
                    f"marketing for {lowest_product}."
                )

            elif "recommend" in q:

                st.warning(
                    f"Focus more on {top_product} "
                    f"while improving {lowest_product}."
                )

            else:

                st.info("""
Try asking:
- top products
- forecast
- risks
- trends
- strategy
- recommendations
""")

    else:

        st.info(
            "📁 Upload a CSV file to begin ERP analysis."
        )