import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI ERP Platform",
    page_icon="🚀",
    layout="wide"
)

# =========================
# HOME PAGE
# =========================

st.title("🚀 AI ERP PLATFORM")

st.subheader(
    "Smarter business intelligence powered by AI"
)

st.divider()

col1, col2, col3 = st.columns([1,1,1])

with col2:
    if st.button("🚀 Launch Platform"):
        st.session_state.page = "analyzer"

# =========================
# ANALYZER PAGE
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

        st.success("File uploaded successfully!")

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

            st.write("Average values:")

            st.dataframe(
                numeric_cols.mean().round(2)
            )

            st.write("Maximum values:")

            st.dataframe(
                numeric_cols.max()
            )

        else:
            st.warning("No numeric columns found.")

# =========================
# FEATURES
# =========================

st.write("")
st.write("")

st.header("✨ Platform Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
📊 Analytics

Advanced ERP analytics with real-time business insights.
""")

with col2:
    st.success("""
🤖 AI Forecasting

Predict future growth with AI.
""")

with col3:
    st.warning("""
⚡ Smart Insights

AI recommendations for ERP systems.
""")

# =========================
# STATS
# =========================

st.write("")
st.write("")

st.header("📈 Trusted Worldwide")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Businesses", "10K+")
c2.metric("Uptime", "99.9%")
c3.metric("Reports", "1M+")
c4.metric("Monitoring", "24/7")

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