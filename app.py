import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI ERP Platform",
    page_icon="🚀",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right, #0B1120, #111827);
    color: white;
}

.hero-box {
    background-color: #161B22;
    padding: 60px;
    border-radius: 25px;
    text-align: center;
    margin-top: 40px;
    border: 1px solid #30363D;
}

.feature-box {
    background-color: #161B22;
    padding: 30px;
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

</style>
""", unsafe_allow_html=True)

# =====================================
# HERO SECTION
# =====================================

st.markdown("""
<div class="hero-box">

    <h1 style="font-size:4rem;">
        🚀 AI ERP ANALYTICS PLATFORM
    </h1>

    <p style="font-size:1.4rem; color:#9CA3AF;">
        Smarter business intelligence powered by AI
    </p>

</div>
""", unsafe_allow_html=True)

st.markdown("")

# =====================================
# FEATURES
# =====================================

st.markdown("## ✨ Platform Features")

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

# =====================================
# CTA SECTION
# =====================================

st.markdown("""
<div class="hero-box">

    <h1>
        🌐 Cloud Hosted ERP Intelligence
    </h1>

    <p style="font-size:1.2rem; color:#9CA3AF;">
        Built with Streamlit + AI + Modern UI
    </p>

</div>
""", unsafe_allow_html=True)