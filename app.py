import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI ERP Platform",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# PREMIUM CSS
# =========================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0B1120,
        #111827,
        #0F172A
    );
    color: white;
    overflow-x: hidden;
}

/* Hero Box */
.hero-box {
    padding: 80px;
    border-radius: 35px;
    text-align: center;
    margin-top: 40px;
    background: rgba(22, 27, 34, 0.7);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    animation: fadeIn 1s ease-in-out;
}

/* Big Title */
.big-title {
    font-size: 5rem;
    font-weight: 800;
    background: linear-gradient(
        to right,
        #2EA043,
        #58A6FF
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    font-size: 1.5rem;
    color: #9CA3AF;
    margin-top: 20px;
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(
        to right,
        #238636,
        #2EA043
    );
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.8rem 1.6rem;
    font-weight: bold;
    font-size: 1rem;
    transition: 0.3s ease;
}

/* Button Hover */
div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 25px rgba(46,160,67,0.5);
}

/* Feature Cards */
.feature-card {
    background: rgba(22, 27, 34, 0.7);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    transition: 0.3s ease;
    height: 240px;
}

/* Hover Animation */
.feature-card:hover {
    transform: translateY(-10px);
    border: 1px solid #2EA043;
    box-shadow: 0px 0px 30px rgba(46,160,67,0.35);
}

/* Stats Box */
.stats-box {
    background: rgba(22,27,34,0.7);
    padding: 40px;
    border-radius: 25px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Pricing Cards */
.pricing-card {
    background: rgba(22,27,34,0.75);
    padding: 40px;
    border-radius: 25px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
    transition: 0.3s ease;
}

.pricing-card:hover {
    transform: scale(1.03);
    border: 1px solid #58A6FF;
    box-shadow: 0px 0px 30px rgba(88,166,255,0.3);
}

/* Fade Animation */
@keyframes fadeIn {

    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HERO SECTION
# =========================================

st.markdown("""
<div class="hero-box">

    <div class="big-title">
        AI ERP PLATFORM
    </div>

    <div class="subtitle">
        Smarter business intelligence powered by AI
    </div>

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================================
# BUTTONS
# =========================================

col1, col2, col3 = st.columns([1,1,1])

with col2:
    st.button("🚀 Launch Platform")

st.write("")
st.write("")

# =========================================
# FEATURES
# =========================================

st.header("✨ Platform Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="feature-card">

        <h2>📊 Analytics</h2>

        <p>
        Advanced ERP analytics with
        real-time business insights.
        </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="feature-card">

        <h2>🤖 AI Forecasting</h2>

        <p>
        Predict future business growth
        using AI-powered forecasting.
        </p>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="feature-card">

        <h2>⚡ Smart Insights</h2>

        <p>
        AI-generated recommendations
        for faster decision making.
        </p>

    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================
# STATS SECTION
# =========================================

st.header("📈 Trusted Worldwide")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stats-box">
        <h1>10K+</h1>
        <p>Businesses</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-box">
        <h1>99.9%</h1>
        <p>Uptime</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-box">
        <h1>1M+</h1>
        <p>Reports Generated</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stats-box">
        <h1>24/7</h1>
        <p>AI Monitoring</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================
# PRICING
# =========================================

st.header("💎 Pricing")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="pricing-card">

        <h2>Starter</h2>

        <h1>$9</h1>

        <p>Basic analytics</p>
        <p>AI insights</p>
        <p>1 dashboard</p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="pricing-card">

        <h2>Pro</h2>

        <h1>$49</h1>

        <p>Advanced AI</p>
        <p>Unlimited dashboards</p>
        <p>Forecasting tools</p>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="pricing-card">

        <h2>Enterprise</h2>

        <h1>$199</h1>

        <p>Custom AI solutions</p>
        <p>Priority support</p>
        <p>Unlimited everything</p>

    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================
# FOOTER
# =========================================

st.markdown("---")

st.markdown("""
<center>

<h3>🌐 AI ERP PLATFORM</h3>

<p style="color:#9CA3AF;">
Built with AI + Streamlit + Modern SaaS Design
</p>

</center>
""", unsafe_allow_html=True)