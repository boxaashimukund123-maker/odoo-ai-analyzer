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

    border-radius: 14px;

    padding: 12px;

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

        st.title("🚀 Odoo AI Dashboard")

        st.success(
            "AI systems operational • Live monitoring enabled"
        )

        st.write("")

        # KPI CARDS

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.markdown("""
            <div style="
                background:linear-gradient(135deg,#2563eb,#1e3a8a);
                padding:25px;
                border-radius:20px;
                text-align:center;
                box-shadow:0px 0px 25px rgba(37,99,235,0.45);
            ">

            <h3>💰 Revenue</h3>

            <h1>$128K</h1>

            <p>+18% Growth</p>

            </div>
            """, unsafe_allow_html=True)

        with c2:

            st.markdown("""
            <div style="
                background:linear-gradient(135deg,#16a34a,#14532d);
                padding:25px;
                border-radius:20px;
                text-align:center;
                box-shadow:0px 0px 25px rgba(34,197,94,0.45);
            ">

            <h3>👥 Users</h3>

            <h1>4,231</h1>

            <p>+9% Growth</p>

            </div>
            """, unsafe_allow_html=True)

        with c3:

            st.markdown("""
            <div style="
                background:linear-gradient(135deg,#d97706,#78350f);
                padding:25px;
                border-radius:20px;
                text-align:center;
                box-shadow:0px 0px 25px rgba(245,158,11,0.45);
            ">

            <h3>📦 Orders</h3>

            <h1>1,284</h1>

            <p>+12% Growth</p>

            </div>
            """, unsafe_allow_html=True)

        with c4:

            st.markdown("""
            <div style="
                background:linear-gradient(135deg,#9333ea,#581c87);
                padding:25px;
                border-radius:20px;
                text-align:center;
                box-shadow:0px 0px 25px rgba(168,85,247,0.45);
            ">

            <h3>🤖 AI Score</h3>

            <h1>98%</h1>

            <p>System Stable</p>

            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.write("")

        # CHARTS

        left, right = st.columns(2)

        with left:

            st.subheader("📈 Revenue Growth")

            st.line_chart(
                [5, 9, 14, 18, 22, 27, 35]
            )

        with right:

            st.subheader("📊 Sales Performance")

            st.bar_chart(
                [20, 14, 30, 25, 18]
            )

        st.write("")
        st.write("")

        # AI ACTIVITY

        st.subheader("🧠 Live AI Activity")

        st.info(
            "AI detected increased customer engagement in the last 24 hours."
        )

        st.success(
            "Revenue forecast predicts +21% growth next quarter."
        )

        st.warning(
            "Inventory for Product A may run low within 7 days."
        )

        # PROGRESS BARS

        st.subheader("⚡ System Performance")

        st.write("AI Processing")
        st.progress(92)

        st.write("Server Stability")
        st.progress(99)

        st.write("Customer Satisfaction")
        st.progress(87)

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