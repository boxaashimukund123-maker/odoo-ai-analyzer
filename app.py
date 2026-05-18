rm app.py

cat > app.py << 'EOF'
import streamlit as st

st.set_page_config(page_title="AI ERP", layout="wide")

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#020617,#0f172a,#111827);
    color:white;
}

.hero{
    padding:120px 30px;
    border-radius:30px;
    text-align:center;
    background:rgba(17,24,39,0.7);
    border:1px solid rgba(255,255,255,0.08);
}

.hero-title{
    font-size:80px;
    font-weight:800;
    background:linear-gradient(to right,#22c55e,#3b82f6);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-sub{
    font-size:24px;
    color:#9CA3AF;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<div class="hero-title">
🚀 AI ERP PLATFORM
</div>

<div class="hero-sub">
Smarter business intelligence powered by AI
</div>

</div>
""", unsafe_allow_html=True)

EOF

streamlit run app.py