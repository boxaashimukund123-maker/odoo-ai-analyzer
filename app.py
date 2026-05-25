import streamlit as st
import pandas as pd
import xmlrpc.client

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Odoo AI Analyzer",
    page_icon="🤖",
    layout="wide"
)

# =========================================
# SESSION
# =========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================================
# PREMIUM CSS
# =========================================

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {

    background: linear-gradient(
        135deg,
        #020617,
        #00113a,
        #0f172a
    );

    color: white;

    overflow-x: hidden;
}

/* PARTICLES */

.particles {

    position: fixed;

    width: 100%;

    height: 100%;

    top: 0;

    left: 0;

    overflow: hidden;

    z-index: 0;

    pointer-events: none;
}

.particle {

    position: absolute;

    width: 18px;

    height: 18px;

    background: rgba(59,130,246,0.9);

    border-radius: 50%;

    animation: float 12s linear infinite;

    filter: blur(1px);

    box-shadow:
        0px 0px 25px rgba(59,130,246,0.9);
}

.particle:nth-child(1) {
    left: 10%;
    animation-duration: 12s;
}

.particle:nth-child(2) {
    left: 25%;
    animation-duration: 18s;
}

.particle:nth-child(3) {
    left: 50%;
    animation-duration: 15s;
}

.particle:nth-child(4) {
    left: 75%;
    animation-duration: 20s;
}

.particle:nth-child(5) {
    left: 90%;
    animation-duration: 13s;
}

@keyframes float {

    0% {
        transform: translateY(100vh);
        opacity: 0;
    }

    10% {
        opacity: 1;
    }

    100% {
        transform: translateY(-10vh);
        opacity: 0;
    }
}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background: rgba(10,10,20,0.8);

    backdrop-filter: blur(12px);

    border-right: 1px solid rgba(255,255,255,0.08);
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

    transition: 0.3s ease;
}

.stButton > button:hover {

    transform: scale(1.03);

    box-shadow:
        0px 0px 30px rgba(59,130,246,0.7);
}

/* INPUTS */

.stTextInput input {

    background: rgba(255,255,255,0.06) !important;

    color: white !important;

    border-radius: 12px !important;
}

/* KPI CARDS */

.card {

    padding: 25px;

    border-radius: 22px;

    text-align: center;

    transition: 0.3s ease;

    color: white;
}

.card:hover {

    transform: translateY(-10px) scale(1.02);

    box-shadow:
        0px 0px 30px rgba(59,130,246,0.45);
}

.blue {
    background: linear-gradient(135deg,#2563eb,#1e3a8a);
}

.green {
    background: linear-gradient(135deg,#16a34a,#14532d);
}

.orange {
    background: linear-gradient(135deg,#d97706,#78350f);
}

.purple {
    background: linear-gradient(135deg,#9333ea,#581c87);
}

</style>
""", unsafe_allow_html=True)

# =========================================
# PARTICLES
# =========================================

st.markdown("""
<div class="particles">

<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>

</div>
""", unsafe_allow_html=True)

# =========================================
# LOGIN PAGE
# =========================================

if not st.session_state.logged_in:

    st.title("🤖 Odoo AI Analyzer")

    st.subheader(
        "AI-powered ERP analytics platform"
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

    st.sidebar.title("🤖 Odoo AI")

    page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analyzer",
        "AI Insights",
        "🔗 Odoo Connection"
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
            <div class="card blue">
            <h3>💰 Revenue</h3>
            <h1>$128K</h1>
            <p>+18%</p>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="card green">
            <h3>👥 Users</h3>
            <h1>4,231</h1>
            <p>+9%</p>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown("""
            <div class="card orange">
            <h3>📦 Orders</h3>
            <h1>1,284</h1>
            <p>+12%</p>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown("""
            <div class="card purple">
            <h3>🤖 AI Score</h3>
            <h1>98%</h1>
            <p>Stable</p>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.write("")

        # CHARTS

        left, right = st.columns(2)

        with left:

            st.subheader("📈 Revenue Growth")

            st.line_chart(
                [5, 8, 12, 18, 24, 32, 41]
            )

        with right:

            st.subheader("📊 Sales Performance")

            st.bar_chart(
                [20, 14, 30, 25, 18]
            )

        st.write("")
        st.write("")

        # PROGRESS

        st.subheader("⚡ System Performance")

        st.write("AI Processing")
        st.progress(92)

        st.write("Server Stability")
        st.progress(99)

        st.write("Customer Satisfaction")
        st.progress(87)        

        st.success(
            "Customer engagement increased this week."
        )

        st.warning(
            "Inventory for Product A may run low soon."
        )

    # =====================================
    # ANALYZER
    # =====================================

    if page == "Analyzer":

        st.title("📊 Odoo Data Analyzer")

        if "uid" not in st.session_state:

            st.warning(
                "⚠️ Connect to Odoo first from the Odoo Connection page."
            )

        else:

            st.success("✅ Odoo connection detected")

            # -------------------------
            # LOAD CUSTOMERS
            # -------------------------

            if st.button("📥 Load Customers"):

                models = xmlrpc.client.ServerProxy(
                    f"{st.session_state['odoo_url']}/xmlrpc/2/object"
                )

                customers = models.execute_kw(
                    st.session_state["database"],
                    st.session_state["uid"],
                    st.session_state["api_key"],
                    "res.partner",
                    "search_read",
                    [[]],
                    {
                        "fields": ["id", "name", "email"],
                        "limit": 20
                    }
                )

                st.subheader("👥 Customers")
                st.dataframe(pd.DataFrame(customers))

            # -------------------------
            # LOAD SALES ORDERS
            # -------------------------

            if st.button("📈 Load Sales Orders"):

                models = xmlrpc.client.ServerProxy(
                    f"{st.session_state['odoo_url']}/xmlrpc/2/object"
                )

                orders = models.execute_kw(
                    st.session_state["database"],
                    st.session_state["uid"],
                    st.session_state["api_key"],
                    "sale.order",
                    "search_read",
                    [[]],
                    {
                        "fields": [
                            "name",
                            "partner_id",
                            "amount_total",
                            "state"
                        ],
                        "limit": 20
                    }
                )

                st.subheader("📈 Sales Orders")
                st.write("Orders found:", len(orders))

                if len(orders) > 0:

                    df = pd.DataFrame(orders)

                    if "partner_id" in df.columns:

                        df["customer"] = df["partner_id"].apply(
                            lambda x: x[1]
                            if isinstance(x, (list, tuple)) and len(x) > 1
                            else str(x)
                        )

                        df.drop(
                            columns=["partner_id"],
                            inplace=True
                        )

                    st.dataframe(df)

                else:

                    st.warning(
                        "No sales orders found in Odoo."

                        )

    # =====================================
    # AI INSIGHTS
    # =====================================

if page == "AI Insights":

    st.title("🧠 AI Business Insights")

    st.info(
        "AI predicts 21% sales growth next quarter."
    )

    st.subheader("📈 Revenue Growth")

    st.line_chart(
        [5, 8, 12, 18, 24, 32, 41]
    )

    st.subheader("📊 Sales Performance")

    st.bar_chart(
        [20, 14, 30, 25, 18]
    )

    st.subheader("⚡ System Performance")

    st.write("AI Processing")
    st.progress(92)

    st.write("Server Stability")
    st.progress(99)

    st.write("Customer Satisfaction")
    st.progress(87)

    st.success(
        "Customer engagement increased this week."
    )

    st.warning(
        "Inventory for Product A may run low soon."
    ) 

    # =====================================
    # ODOO CONNECTION
    # =====================================

    if page == "🔗 Odoo Connection":

        st.title("🔗 Odoo Connection")

        st.success("Ready for Odoo 18 Integration")

        odoo_url = st.text_input(
            "Odoo URL",
            value="https://franciscovortex.odoo.com"
        )

        database = st.text_input(
            "Database",
            value="franciscovortex"
        )

        email = st.text_input("Email")

        api_key = st.text_input(
            "API Key",
            type="password"
        )

        if st.button("🚀 Save Connection"):

            st.session_state["odoo_url"] = odoo_url
            st.session_state["database"] = database
            st.session_state["email"] = email
            st.session_state["api_key"] = api_key

            st.success("Connection Saved!")

        if st.button("🔍 Test Connection"):

            try:

                common = xmlrpc.client.ServerProxy(
                    f"{odoo_url}/xmlrpc/2/common"
                )

                uid = common.authenticate(
                    database,
                    email,
                    api_key,
                    {}
                )

                if uid:

                    st.session_state["uid"] = uid

                    st.success(
                        f"✅ Connected successfully! User ID: {uid}"
                    )

                else:

                    st.error(
                        "❌ Login failed. Check email or API key."
                    )

            except Exception as e:

                st.error(
                    f"❌ Connection error: {e}"
                )