import streamlit as st

st.set_page_config(
    page_title="AI ERP Platform",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI ERP PLATFORM")

st.subheader(
    "Smarter business intelligence powered by AI"
)

st.divider()

col1, col2, col3 = st.columns([1,1,1])

with col2:
    st.button("🚀 Launch Platform")

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

st.write("")
st.write("")

st.header("📈 Trusted Worldwide")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Businesses", "10K+")
c2.metric("Uptime", "99.9%")
c3.metric("Reports", "1M+")
c4.metric("Monitoring", "24/7")

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