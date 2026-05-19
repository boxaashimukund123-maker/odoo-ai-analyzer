import streamlit as st
import pandas as pd

# PAGE CONFIG
st.set_page_config(
    page_title="AI ERP",
    page_icon="🚀",
    layout="wide"
)

# LOGIN SESSION
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# SIMPLE DARK STYLE
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#020617,#00113a,#0f172a);
    color: white;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    padding: 12px;
    font-size: 18px;
    background: #2563eb;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# LOGIN PAGE
if not st.session_state.logged_in:

    st.title("🚀 AI ERP")

    st.subheader(
        "Next generation AI business intelligence platform"
    )

    st.write("")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == "admin" and password == "admin":

            st.session_state.logged_in = True

            st.rerun()

        else:

            st.error("Wrong username or password")

# MAIN APP
else:

    st.sidebar.title("🚀 AI ERP")

    page = st.sidebar.radio(
        "Navigation",
        ["Dashboard", "Analyzer"]
    )

    # DASHBOARD
    if page == "Dashboard":

        st.title("📊 Dashboard")

        col1, col2, col3 = st.columns(3)

        col1.metric("Revenue", "$128K")
        col2.metric("Users", "4,231")
        col3.metric("AI Score", "98%")

        st.write("")

        st.subheader("Business Growth")

        st.line_chart(
            [5, 8, 12, 15, 18, 22, 27]
        )

        st.success(
            "AI predicts 18% growth this quarter."
        )

    # ANALYZER
    if page == "Analyzer":

        st.title("📂 ERP Analyzer")

        uploaded_file = st.file_uploader(
            "Upload CSV",
            type=["csv"]
        )

        if uploaded_file is not None:

            df = pd.read_csv(uploaded_file)

            st.dataframe(df)

            numeric_cols = df.select_dtypes(
                include="number"
            ).columns

            if len(numeric_cols) > 0:

                selected = st.selectbox(
                    "Choose Column",
                    numeric_cols
                )

                st.line_chart(df[selected])

                st.bar_chart(df[selected])