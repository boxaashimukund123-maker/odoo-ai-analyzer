import streamlit as st
import pandas as pd

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI ERP",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# LOGIN SESSION
# =========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================================
# CLEAN CSS
# =========================================

st.markdown("""
<style>

/* BACKGROUND */

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

/* INPUTS */

.stTextInput input {

    background: rgba(255,255,255,0.06) !important;

    color: white !important;

    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGIN PAGE
# =========================================

if not st.session_state.logged_in:

    st.markdown(
        """
        <div class="login-box">

            <div class="title">
                🚀 AI ERP
            </div>

            <div class="sub">
                Next generation AI business intelligence platform
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    username = st.text_input("👤 Username")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    if st.button("✨ Login"):

        if username == "admin" and password == "admin":

            st.session_state.logged_in = True

            st.rerun()

        else:

            st.error("Invalid credentials")

# =========================================
# MAIN APP
# =========================================

else:

    st.sidebar.title("🚀 AI ERP")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Analyzer"
        ]
    )

    # HOME PAGE

    if page == "Home":

        st.title("🚀 AI ERP PLATFORM")

        st.subheader(
            "Smarter business intelligence powered by AI"
        )

        st.divider()

        st.header("✨ Platform Features")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.info(
                "📊 Advanced ERP analytics with real-time insights."
            )

        with c2:

            st.success(
                "🤖 AI forecasting and predictive analytics."
            )

        with c3:

            st.warning(
                "⚡ Smart recommendations for ERP systems."
            )

    # ANALYZER PAGE

    if page == "Analyzer":

        st.title("📊 ERP Analyzer Dashboard")

        uploaded_file = st.file_uploader(
            "Upload CSV File",
            type=["csv"]
        )

        if uploaded_file is not None:

            df = pd.read_csv(uploaded_file)

            st.success("CSV uploaded successfully!")

            st.subheader("📄 Data Preview")

            st.dataframe(df)

            numeric_cols = df.select_dtypes(
                include="number"
            ).columns

            if len(numeric_cols) > 0:

                selected_col = st.selectbox(
                    "Choose a column",
                    numeric_cols
                )

                st.subheader("📈 Line Chart")

                st.line_chart(df[selected_col])

                st.subheader("📊 Bar Chart")

                st.bar_chart(df[selected_col])

st.divider()

st.caption("🌐 Built with Streamlit + AI")