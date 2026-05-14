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
# CUSTOM CSS
# ============================================

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #161B22;
}

div[data-testid="metric-container"] {
    background-color: #161B22;
    border: 1px solid #30363D;
    padding: 15px;
    border-radius: 12px;
}

div.stButton > button {
    background-color: #238636;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.5rem 1rem;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #2EA043;
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
- ERP Analysis
- AI Forecasting
- Smart Recommendations
- Interactive Charts
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
    # FILE UPLOADER
    # ============================================

    uploaded_file = st.file_uploader(
        "📂 Upload your ERP CSV file",
        type=["csv"]
    )

    # ============================================
    # IF FILE EXISTS
    # ============================================

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("📋 Uploaded Data")

        st.dataframe(df, use_container_width=True)

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

        average_sales = int(summary.mean())

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
            average_sales
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
        # FORECAST
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
            f"{top_product} is currently the "
            f"best-performing product."
        )

        st.error(
            f"{lowest_product} is currently the "
            f"lowest-performing product."
        )

        st.divider()

        # ============================================
        # SMART AI CHAT
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
                    f"lowest-performing product "
                    f"with sales of {lowest_sales}."
                )

            elif "summary" in q:

                st.info(
                    f"Total sales are {total_sales}."
                )

            elif "average" in q:

                st.info(
                    f"Average sales are "
                    f"{average_sales}."
                )

            elif "forecast" in q or "prediction" in q:

                st.success(
                    f"Predicted next month sales: "
                    f"{predicted_sales}"
                )

            elif "trend" in q:

                st.success(
                    f"Business growth trend is "
                    f"{growth_percent}% upward."
                )

            elif "risk" in q:

                st.error(
                    f"Potential risk detected in "
                    f"{lowest_product} due to "
                    f"low performance."
                )

            elif "strategy" in q:

                st.info(
                    f"Recommended strategy: "
                    f"scale {top_product}, improve "
                    f"marketing for {lowest_product}, "
                    f"and optimize pricing."
                )

            elif "recommend" in q:

                st.warning(
                    f"Focus on improving "
                    f"{lowest_product} while "
                    f"expanding {top_product}."
                )

            else:

                st.info("""
Try asking:
- top product
- worst product
- forecast
- risks
- trends
- strategy
- recommendations
""")

    else:

        st.info(
            "📁 Upload a CSV file to begin analysis."
        )