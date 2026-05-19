import streamlit as st
import pandas as pd

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Odoo AI Analyzer",
    page_icon="🤖",
    layout="wide"
)

# =========================================
# LOGIN SESSION
# =========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================================
# STYLING
# =========================================

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

/* BUTTONS */

.stButton > button {

    width: 100%;

    border-radius: 12px;

    padding: 12px;

    font-size: 18px;

    font-weight: bold;

    background: #2563eb;

    color: white;

    border: none;
}

/* INPUTS */

.stTextInput input {

    background: rgba(255,255,255,0.06) !important;

    color: white !important;

    border-radius: 10px !important;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background: rgba(10,10,20,0.75);
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGIN PAGE
# =========================================

if not st.session_state.logged_in:

    st.title("🤖 Odoo AI Analyzer")

    st.subheader(
        "AI-powered ERP analytics and business intelligence"
    )

    st.write("")

    username = st.text_input("👤 Username")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    if st.button("🚀 Login"):

        if username == "admin" and password == "admin":

            st.session_state.logged_in = True

            st.rerun()

        else:

            st.error("Wrong username or password")

# =========================================
# MAIN APP
# =========================================

else:

    # SIDEBAR

    st.sidebar.title("🤖 Odoo AI")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Analyzer",
            "AI Insights"
        ]
    )

    # =====================================
    # DASHBOARD
    # =====================================

    if page == "Dashboard":

        st.title("📊 Odoo AI Dashboard")

        st.success(
            "Connected to AI business intelligence system"
        )

        st.divider()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "💰 Revenue",
            "$128K",
            "+18%"
        )

        col2.metric(
            "👥 Customers",
            "4,231",
            "+9%"
        )

        col3.metric(
            "📦 Orders",
            "1,284",
            "+12%"
        )

        col4.metric(
            "🤖 AI Score",
            "98%",
            "+4%"
        )

        st.write("")

        st.subheader("📈 Revenue Growth")

        st.line_chart(
            [5, 8, 12, 15, 18, 22, 27]
        )

        st.write("")

        st.subheader("📊 Sales Distribution")

        st.bar_chart(
            [20, 14, 30, 25, 18]
        )

    # =====================================
    # ANALYZER
    # =====================================

    if page == "Analyzer":

        st.title("📂 ERP Data Analyzer")

        uploaded_file = st.file_uploader(
            "Upload CSV File",
            type=["csv"]
        )

        if uploaded_file is not None:

            df = pd.read_csv(uploaded_file)

            st.success("CSV uploaded successfully!")

            st.subheader("📄 Dataset Preview")

            st.dataframe(df)

            numeric_cols = df.select_dtypes(
                include="number"
            ).columns

            if len(numeric_cols) > 0:

                selected_col = st.selectbox(
                    "Choose a numeric column",
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
                    "No numeric columns found."
                )

    # =====================================
    # AI INSIGHTS
    # =====================================

    if page == "AI Insights":

        st.title("🧠 AI Business Insights")

        st.info(
            "AI predicts a 21% increase in sales next quarter."
        )

        st.warning(
            "Inventory for Product A may run low in 7 days."
        )

        st.success(
            "Customer retention improved by 13%."
        )

        st.subheader("🤖 AI Recommendations")

        st.write(
            "- Increase marketing for high-performing products"
        )

        st.write(
            "- Restock inventory for trending items"
        )

        st.write(
            "- Optimize pricing for slow-moving products"
        )

# =========================================
# FOOTER
# =========================================

st.divider()

st.caption("🌐 Odoo AI Analyzer • Powered by Streamlit + AI")