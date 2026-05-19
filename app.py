import streamlit as st

st.set_page_config(
    page_title="AI ERP",
    page_icon="🚀",
    layout="centered"
)

st.markdown(
    """
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

    .box {
        background: rgba(255,255,255,0.08);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin-top: 100px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="box">
        <h1>🚀 AI ERP</h1>
        <p>Next generation AI business intelligence platform</p>
    </div>
    """,
    unsafe_allow_html=True
)

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if username == "admin" and password == "admin":

        st.success("WORKING 🔥")

    else:

        st.error("Wrong password")