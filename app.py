import streamlit as st

st.set_page_config(
    page_title="AI ERP",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #020617,
        #00113a,
        #0f172a
    );
    color: white;
}

/* LOGIN CARD */

.login-box {

    max-width: 500px;

    margin: auto;

    margin-top: 120px;

    padding: 40px;

    border-radius: 24px;

    background: rgba(255,255,255,0.08);

    backdrop-filter: blur(16px);

    border: 1px solid rgba(255,255,255,0.1);

    text-align: center;

    box-shadow:
        0px 0px 40px rgba(59,130,246,0.3);
}

/* TITLE */

.title {

    font-size: 52px;

    font-weight: bold;

    color: white;

    margin-bottom: 10px;
}

/* SUBTITLE */

.sub {

    color: #CBD5E1;

    font-size: 18px;

    margin-bottom: 25px;
}

/* BUTTON */

.stButton > button {

    width: 100%;

    border-radius: 14px;

    padding: 14px;

    font-size: 18px;

    font-weight: bold;

    border: none;

    color: white;

    background: linear-gradient(
        135deg,
        #2563eb,
        #3b82f6
    );
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="login-box">

    <div class="title">
        🚀 AI ERP
    </div>

    <div class="sub">
        Next generation AI business intelligence platform
    </div>

</div>
""", unsafe_allow_html=True)

username = st.text_input("👤 Username")

password = st.text_input(
    "🔒 Password",
    type="password"
)

if st.button("✨ Login"):

    if username == "admin" and password == "admin":

        st.success("Login successful 🚀")

    else:

        st.error("Invalid credentials")