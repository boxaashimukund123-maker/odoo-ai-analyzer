cat > app.py << 'EOF'
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

.stApp {
    background: linear-gradient(
        135deg,
        #020617,
        #0F172A,
        #111827
    );
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* HERO */

.hero {
    text-align: center;
    padding: 90px 40px;
    border-radius: 35px;
    background: rgba(17, 24, 39, 0.65);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08);
    animation: fadeIn 1s ease;
}

.hero-title {
    font-size: 5rem;
    font-weight: 800;
    background: linear-gradient(
        to right,
        #2EA043,
        #58A6FF
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;
}

.hero-subtitle {
    font-size: 1.4rem;
    color: #9CA3AF;
}

/* TITLES */

.section-title {
    font-size: 2.2rem;
    font-weight: 700;
    margin-bottom: 25px;
}

/* CARDS */

.card {
    background: rgba(17,24,39,0.7);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    transition: 0.3s ease;
    height: 230px;
}

.card:hover {
    transform: translateY(-10px);
    border: 1px solid #58A6FF;
    box-shadow: 0px 0px 30px rgba(88,166,255,0.25);
}

/* STATS */

.stat-card {
    background: rgba(17,24,39,0.7);
    padding: 40px;
    border-radius: 25px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

/* PRICING */

.price-card {
    background: rgba(17,24,39,0.75);
    padding: 40px;
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.08);
    text-align: center;
    transition: 0.3s ease;
}

.price-card:hover {
    transform: scale(1.03);
    border: 1px solid #2EA043;
    box-shadow: 0px 0px 25px rgba(46,160,67,0.3);
}

/* BUTTON */

div.stButton > button {
    width: 100%;
    background: linear-gradient(
        to right,
        #238636,
        #2EA043
    );
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.8rem 1rem;
    font-size: 1rem;
    font-weight: bold;
    transition: 0.3s ease;
}

div.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 25px rgba(46,160,67,0.45);
}

/* ANIMATION */

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
<div class="hero">

    <div class="hero-title">
        🚀 AI ERP PLATFORM
    </div>

    <div class="hero-subtitle">
        Smarter business intelligence powered by AI
    </div>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================
# BUTTON
# =========================================

col1, col2, col3 = st.columns([1,1,1])

with col2:
    st.button("🚀 Launch Platform")

st.write("")
st.write("")

# =========================================
# FEATURES
# =========================================

st.markdown(
    '<div class="section-title">✨ Platform Features</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h1>📊</h1>
        <h2>Analytics</h2>
        <p>
        Advanced ERP analytics with
        real-time business insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h1>🤖</h1>
        <h2>AI Forecasting</h2>
        <p>
        Predict future business growth
        using AI-powered forecasting.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h1>⚡</h1>
        <h2>Smart Insights</h2>
        <p>
        AI-generated recommendations
        for faster decision making.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================
# STATS
# =========================================

st.markdown(
    '<div class="section-title">📈 Trusted Worldwide</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <h1>10K+</h1>
        <p>Businesses</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <h1>99.9%</h1>
        <p>Uptime</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <h1>1M+</h1>
        <p>Reports Generated</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <h1>24/7</h1>
        <p>AI Monitoring</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================
# PRICING
# =========================================

st.markdown(
    '<div class="section-title">💎 Pricing</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="price-card">
        <h2>Starter</h2>
        <h1>$9</h1>
        <p>Basic analytics</p>
        <p>AI insights</p>
        <p>1 dashboard</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="price-card">
        <h2>Pro</h2>
        <h1>$49</h1>
        <p>Advanced AI</p>
        <p>Unlimited dashboards</p>
        <p>Forecasting tools</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="price-card">
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
<div style="text-align:center; padding:20px;">

    <h3>🌐 AI ERP PLATFORM</h3>

    <p style="color:#9CA3AF;">
        Built with AI + Streamlit + Premium UI
    </p>

</div>
""", unsafe_allow_html=True)

EOF