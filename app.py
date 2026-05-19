import streamlit as st
import pandas as pd

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI ERP Platform",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# SESSION STATE
# =========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================================
# PREMIUM CSS
# =========================================

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

    /* LOGIN BOX */

    .login-box {

        max-width: 600px;

        margin: auto;

        margin-top: 90px;

        padding: 45px;

        border-radius: 24px;

        background: rgba(255,255,255,0.08);

        backdrop-filter: blur(16px);

        border: 1px solid rgba(255,255,255,0.1);

        text-align: center;

        box-shadow:
            0px 0px 40px rgba(59,130,246,0.35);
    }

    /* BUTTONS */

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

        transition: 0.3s ease;
    }

    .stButton > button:hover {

        transform: scale(1.02);

        box-shadow:
            0px 0px 25px rgba(59,130,246,0.7);
    }

    /* INPUTS */

    .stTextInput input {

        background: rgba(255,255,255,0.06) !important;

        color: white !important;

        border-radius: 12px !important;
    }

    /* DASHBOARD CARDS */

    .card {

        background: rgba(255,255,255,0.08);

        padding: 25px;

        border-radius: 20px;

        border: 1px solid rgba(255,255,255,0.1);

        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================
# LOGIN PAGE
# =========================================

if not st.session_state.logged_in:

    st.markdown(
        """
        <div class="login-box">

            <h1 style="
                font-size:65px;
                margin-bottom:10px;
            ">
                🚀 AI ERP
            </h1>

            <p style="
                color:#CBD5E1;
                font-size:20px;
            ">
                Next generation AI business intelligence platform
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

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

            st.error("Invalid username or password")

# =========================================
# MAIN APP
# =========================================

else:

    # SIDEBAR

    st.sidebar.title("🚀 AI ERP")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Analyzer"
        ]
    )

    # =====================================
    # DASHBOARD
    # =====================================

    if page == "Dashboard":

        st.title("🚀 AI ERP Dashboard")

        st.success("Welcome back admin 🔥")

        st.divider()

        c1, c2, c3 = st.columns(3)

        with c1:

            st.markdown(
                """
                <div class="card">
                    <h2>📈 Revenue</h2>
                    <h1>$128K</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:

            st.markdown(
                """
                <div class="card">
                    <h2>👥 Users</h2>
                    <h1>4,231</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c3:

            st.markdown(
                """
                <div class="card">
                    <h2>🤖 AI Score</h2>
                    <h1>98%</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")
        st.write("")

        st.subheader("📊 Business Growth")

        st.line_chart(
            [5, 9, 7, 12, 15, 20, 24]
        )

        st.subheader("🧠 AI Insights")

        st.info(
            "Revenue expected to grow by 18% this quarter."
        )

    # =====================================
    # ANALYZER
    # =====================================

    if page == "Analyzer":

        st.title("📊 ERP Analyzer")

        uploaded_file = st.file_uploader(
            "Upload CSV File",
            type=["csv"]
        )

        if uploaded_file is not None:

            df = pd.read_csv(uploaded_file)

            st.success("CSV uploaded successfully!")

            st.subheader("📄 Data Preview")

            st.dataframe(df)

            # NUMERIC COLUMNS

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

                st.subheader("📉 Statistics")

                st.dataframe(
                    df[numeric_cols].describe()
                )

            else:

                st.warning(
                    "No numeric columns found in CSV."
                )

# =========================================
# FOOTER
# =========================================

st.divider()

st.caption("🌐 Built with Streamlit + AI")