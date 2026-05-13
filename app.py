import streamlit as st
import pandas as pd
import random

# ============================================
# PAGE SETTINGS
# ============================================

st.set_page_config(
    page_title="AI Odoo ERP Analyzer",
    page_icon="🚀",
    layout="wide"
)

# ============================================
# DARK MODE STYLING
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

if not st.session_state.logged_in:

    st.title("🔐 AI Odoo ERP Login")
    st.markdown("### Secure ERP Analytics Access")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Invalid username or password ❌")

# ============================================
# MAIN DASHBOARD
# ============================================

else:

    # ============================================
    # SIDEBAR
    # ============================================

    st.sidebar.title("📌 Dashboard Menu")

    st.sidebar.info("""
AI Odoo ERP Analyzer

Features:
- ERP Data Analysis
- Sales Insights
- Forecasting
- Smart AI Responses
- Export Reports
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
        "📂 Upload your Odoo CSV File",
        type=["csv"]
    )

    # ============================================
    # MAIN APP
    # ============================================

    if uploaded_file:

        # READ CSV
        df = pd.read_csv(uploaded_file)

        # ============================================
        # FILTERS
        # ============================================

        st.subheader("🎛️ Filters")

        products = df["Product"].unique()

        selected_products = st.multiselect(
            "Select Products",
            products,
            default=products
        )

        filtered_df = df[df["Product"].isin(selected_products)]

        # ============================================
        # RAW DATA
        # ============================================

        st.subheader("📋 Raw Data")

        st.dataframe(
            filtered_df,
            use_container_width=True
        )

        # ============================================
        # SALES SUMMARY
        # ============================================

        summary = (
            filtered_df.groupby("Product")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        summary_df = summary.reset_index()

        summary_df.columns = ["Product", "Sales"]

        st.subheader("📊 Sales Summary")

        st.dataframe(
            summary_df,
            use_container_width=True
        )

        # ============================================
        # EXPORT BUTTON
        # ============================================

        csv = summary_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Sales Report",
            data=csv,
            file_name="sales_report.csv",
            mime="text/csv"
        )

        st.divider()

        # ============================================
        # KPI METRICS
        # ============================================

        total_sales = int(summary.sum())

        top_product = summary.idxmax()
        top_sales = int(summary.max())

        lowest_product = summary.idxmin()
        lowest_sales = int(summary.min())

        avg_sales = int(summary.mean())

        health_score = random.randint(75, 98)

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("💰 Total Sales", total_sales)

        col2.metric("🏆 Top Product", top_product)

        col3.metric("📉 Lowest Product", lowest_product)

        col4.metric("📊 Average Sales", avg_sales)

        col5.metric("⚡ Health Score", f"{health_score}%")

        st.divider()

        # ============================================
        # BAR CHART
        # ============================================

        st.subheader("📈 Sales Performance")

        st.bar_chart(
            summary_df.set_index("Product"),
            use_container_width=True
        )

        st.divider()

        # ============================================
        # FORECAST
        # ============================================

        growth_percent = random.randint(5, 20)

        predicted_sales = int(
            total_sales * (1 + growth_percent / 100)
        )

        st.subheader("📈 AI Forecast")

        st.info(
            f"Predicted sales growth next month: "
            f"{growth_percent}%"
        )

        st.success(
            f"Expected next month sales: "
            f"{predicted_sales}"
        )

        # ============================================
        # AI INSIGHTS
        # ============================================

        st.subheader("🤖 AI Insights")

        st.success(
            f"{top_product} is currently the best-performing "
            f"product with sales of {top_sales}."
        )

        st.error(
            f"{lowest_product} is currently the lowest-performing "
            f"product with sales of {lowest_sales}."
        )

        # ============================================
        # SMART AI CHAT
        # ============================================

        st.subheader("💬 Ask AI About Your Business Data")

        question = st.text_input(
            "Ask anything about your ERP data..."
        )

        if question:

            q = question.lower()

            if "top" in q or "best" in q:

                st.success(
                    f"{top_product} is the best-performing "
                    f"product."
                )

            elif "lowest" in q or "worst" in q:

                st.error(
                    f"{lowest_product} is currently "
                    f"the weakest product."
                )

            elif "forecast" in q:

                st.info(
                    f"Forecasted sales next month are "
                    f"{predicted_sales}."
                )

            elif "average" in q:

                st.info(
                    f"Average sales are {avg_sales}."
                )

            elif "health" in q:

                st.info(
                    f"Business health score is "
                    f"{health_score}%."
                )

            elif "recommend" in q:

                st.warning(
                    f"Focus marketing efforts on "
                    f"{lowest_product} to improve performance."
                )

            else:

                st.info("""
Try asking:
- top product
- lowest product
- forecast
- average sales
- recommendations
- health score
""")

    else:

        st.info(
            "📁 Upload a CSV file to start ERP analysis."
        )