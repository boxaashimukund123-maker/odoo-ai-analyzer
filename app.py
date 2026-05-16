import streamlit as st

st.set_page_config(
    page_title="AI ERP Platform",
    page_icon="🚀",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right, #0B1120, #111827);
    color: white;
}

.main-box {
    background-color: #161B22;
    padding: 60px;
    border-radius: 25px;
    text-align: center;
    margin-top: 40px;
    border: 1px solid #30363D;
}

.feature-card {
    background-color: #161B22;
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #30363D;
    text-align: center;
    transition: 0.3s;
}

.feature-card:hover {
    transform: translateY(-8px);
    border: 1px solid #2EA043;
    box-shadow: 0px 0px 20px rgba(46,160,67,0.4);
}

.big-text {
    font-size: 3.8rem;
    font-weight: bold;
}

.small-text {
    font-size: 1.3rem;
    color: #9CA3AF;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================

st.markdown("""
<div class="main-box">

    <div class="big-text">
        🚀 AI ERP ANALYTICS PLATFORM
    </div>

    <br>

    <div class="small-text">
        Smarter business intelligence powered by AI
    </div>

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# FEATURES
# =========================

st.markdown("## ✨ Platform Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h2>📊 Analytics</h2>
        <p>Powerful ERP data insights and reports.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h2>🤖 AI Forecasting</h2>
        <p>Predict sales and business growth instantly.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h2>⚡ Smart Insights</h2>
        <p>AI-generated recommendations for your business.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================
# CTA SECTION
# =========================

st.markdown("""
<div class="main-box">

    <h1>🌐 Cloud Hosted ERP Intelligence</h1>

    <p class="small-text">
        Built with Streamlit + AI + Modern Analytics
    </p>

</div>
""", unsafe_allow_html=True)