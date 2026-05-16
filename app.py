import streamlit as st
import pandas as pd
import plotly.express as px
import random
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
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right, #0B1120, #111827);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161B22;
}

/* Feature Boxes */
.feature-box {
    background-color: #161B22;
    padding: 35px;
    border-radius: 20px;
    border: 1px solid #30363D;
    text-align: center;
    transition: 0.3s ease;
}

.feature-box:hover {
    transform: translateY(-8px);
    border: 1px solid #2EA043;
    box-shadow: 0px 0px 20px rgba(46,160,67,0.4);
}

/* Metric Cards */
div[data-testid="metric-container"] {
    background-color: #161B22;
    border: 1px solid #30363D;
    padding: 18px;
    border-radius: 15px;
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

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGIN SYSTEM
# =========================================

USERNAME = "admin"
PASSWORD = "password123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================================
# LANDING PAGE
# =========================================

if not st.session_state.logged_in:

    st.title("🚀 AI ERP ANALYTICS PLATFORM")

    st.subheader(
        "Smarter business intelligence powered by AI"
    )

    st.markdown("---")

    st.header("✨ Platform Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-box">
            <h2>📊 Analytics</h2>
            <p>Powerful ERP business insights.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-box">
            <h2>🤖 AI Forecasting</h2>
            <p>Predict future growth instantly.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-box">
            <h2>⚡ Smart Insights</h2>
            <p>AI recommendations for your ERP.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    st.markdown("---")

    st.header("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Launch Dashboard"):

        if username == USERNAME and password == PASSWORD:

            st.session_state.logged_in = True

            st.success("Login successful ✅")

            st.rerun()

        else:

            st.error("Invalid username or password ❌")

# =========================================
# MAIN DASHBOARD
# =========================================

else:

    st.sidebar.title("📌 Dashboard")

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()

    st.title("📊 ERP Dashboard")

    uploaded_file = st.file_uploader(
        "📂 Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        with st.spinner(
            "🤖 AI is analyzing your ERP data..."
        ):

            progress_bar = st.progress(0)

            for i in range(100):

                time.sleep(0.01)

                progress_bar.progress(i + 1)

        st.success("Analysis complete ✅")

        df = pd.read_csv(uploaded_file)

        st.subheader("📋 Uploaded Data")

        st.dataframe(df, use_container_width=True)

        # =========================================
        # SALES SUMMARY
        # =========================================

        summary = (
            df.groupby("Product")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        summary_df = summary.reset_index()

        summary_df.columns = ["Product", "Sales"]

        total_sales = int(summary.sum())

        top_product = summary.idxmax()

        lowest_product = summary.idxmin()

        avg_sales = int(summary.mean())

        growth_percent = random.randint(5, 20)

        predicted_sales = int(
            total_sales * (1 + growth_percent / 100)
        )

        col1, col2, col3, col4 = st.columns(4)

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
            "📈 Growth",
            f"{growth_percent}%"
        )

        st.markdown("---")

        # =========================================
        # CHART
        # =========================================

        st.subheader("📈 Sales Analytics")

        fig = px.bar(
            summary_df,
            x="Product",
            y="Sales",
            text="Sales",
            title="Product Sales"
        )

        fig.update_layout(
            template="plotly_dark",
            plot_bgcolor="#0B1120",
            paper_bgcolor="#0B1120",
            font_color="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")

        # =========================================
        # AI INSIGHTS
        # =========================================

        st.subheader("🤖 AI Insights")

        st.success(
            f"{top_product} is the best-performing product."
        )

        st.error(
            f"{lowest_product} is the lowest-performing product."
        )

        st.info(
            f"Predicted next month sales: {predicted_sales}"
        )

        # =========================================
        # AI CHAT
        # =========================================

        st.markdown("---")

        st.subheader(
            "💬 Ask AI About Your Data"
        )

        question = st.text_input(
            "Ask a business question..."
        )

        if question:

            q = question.lower()

            if "top" in q:

                st.success(
                    f"{top_product} is your top product."
                )

            elif "lowest" in q:

                st.error(
                    f"{lowest_product} is underperforming."
                )

            elif "forecast" in q:

                st.info(
                    f"Forecasted sales: {predicted_sales}"
                )

            else:

                st.warning(
                    "Try asking about top products, forecasts, or trends."
                )