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
st.markdown("""
<style>

/* =========================================
   GLOBAL
========================================= */

.stApp {
    background:
        radial-gradient(circle at top left, #1e3a8a 0%, transparent 30%),
        radial-gradient(circle at bottom right, #7c3aed 0%, transparent 30%),
        linear-gradient(135deg, #020617, #0f172a);

    color: white;
}

/* =========================================
   SIDEBAR
========================================= */

section[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(18px);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* =========================================
   TITLES
========================================= */

h1 {
    font-size: 3rem !important;
    font-weight: 800 !important;

    background: linear-gradient(
        90deg,
        #60a5fa,
        #a855f7
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* =========================================
   BUTTONS
========================================= */

.stButton > button {

    background: linear-gradient(
        135deg,
        #2563eb,
        #7c3aed
    );

    border: none;

    color: white;

    border-radius: 16px;

    padding: 12px 22px;

    font-weight: bold;

    transition: 0.3s ease;

    box-shadow: 0 0 20px rgba(99,102,241,0.35);
}

.stButton > button:hover {

    transform: translateY(-4px) scale(1.03);

    box-shadow: 0 0 35px rgba(168,85,247,0.65);
}

/* =========================================
   INPUTS
========================================= */

.stTextInput input {

    background: rgba(255,255,255,0.06);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 14px;

    color: white;
}

/* =========================================
   CARDS
========================================= */

.card {

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 22px;

    padding: 28px;

    backdrop-filter: blur(16px);

    transition: 0.3s ease;

    box-shadow: 0 0 30px rgba(0,0,0,0.25);
}

.card:hover {

    transform: translateY(-6px);

    box-shadow: 0 0 40px rgba(96,165,250,0.25);
}

/* =========================================
   DATAFRAME
========================================= */

[data-testid="stDataFrame"] {

    border-radius: 18px;

    overflow: hidden;
}

/* =========================================
   METRICS
========================================= */

.metric {

    font-size: 2.2rem;

    font-weight: 800;

    color: #60a5fa;
}

/* =========================================
   HIDE STREAMLIT STUFF
========================================= */

[data-testid="stDecoration"] {
    display: none;
}

.stSpinner {
    display: none !important;
}
/* =========================================
   PAGE TRANSITIONS
========================================= */

section.main > div {

    animation: pageFade 0.45s ease;
}

/* Smooth fade + slight slide */

@keyframes pageFade {

    from {

        opacity: 0;

        transform: translateY(12px) scale(0.98);

        filter: blur(6px);
    }

    to {

        opacity: 1;

        transform: translateY(0px) scale(1);

        filter: blur(0px);
    }
}

/* Cards animate separately */

.card {

    animation: cardPop 0.5s ease;
}

@keyframes cardPop {

    from {

        opacity: 0;

        transform: translateY(20px);

    }

    to {

        opacity: 1;

        transform: translateY(0px);

    }
}

/* Sidebar smoothness */

section[data-testid="stSidebar"] * {

    transition: all 0.25s ease;
}

/* Radio buttons hover */

.stRadio label:hover{
    transform: translateX(10px);
}
/* METRIC CARD HOVER */

div[data-testid="metric-container"] {
    transition: all 0.3s ease;
    border-radius: 15px;
}

div[data-testid="metric-container"]:hover {
    transform: translateY(-12px) scale(1.05);
    box-shadow:
0 0 15px rgba(0,150,255,0.8),
0 0 35px rgba(0,150,255,0.6),
0 0 60px rgba(0,150,255,0.4);
}

/* EXTRA PAGE LOAD EFFECT */

.main {
    animation: pageLoad 0.8s ease;
}

@keyframes pageLoad {
    from {
        opacity: 0;
        transform: translateY(25px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* SIDEBAR GLOW */

.stRadio label:hover {
    color: #4da6ff;
    text-shadow: 0 0 10px #4da6ff;
}
</style>
""", unsafe_allow_html=True)
# =========================================
# MAIN APP
# =========================================

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
# =========================================
# PREMIUM LOGIN
# =========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.markdown("""
    <div class="card" style="
        max-width: 500px;
        margin: auto;
        margin-top: 80px;
        text-align: center;
    ">
        <h1>🤖 Odoo AI</h1>
        <p style="
            color: #94a3b8;
            font-size: 18px;
        ">
            Enterprise AI Analytics Platform
        </p>
    </div>
    """, unsafe_allow_html=True)

    username = st.text_input("👤 Username")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    if st.button("🚀 Login"):

        if username == "master" and password == "password":

            st.session_state.logged_in = True

            st.rerun()

        else:

            st.error("Invalid credentials")

    st.stop()

if page == "Dashboard":

        st.markdown("""
<h1 class="glow-title">
🚀 Odoo AI Dashboard
</h1>
""", unsafe_allow_html=True)

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

            # LOAD CUSTOMERS

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
                        "fields": [
                            "id",
                            "name",
                            "email"
                        ],
                        "limit": 20
                    }
                )

                st.subheader("👥 Customers")

                st.dataframe(
                    pd.DataFrame(customers)
                )

            # LOAD SALES ORDERS

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

                st.write(
                    "Orders found:",
                    len(orders)
                )

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
    
            if "odoo_url" not in st.session_state:
                st.warning(
                    "⚠️ Go to Odoo Connection and save your connection first."
                )
                st.stop()
    
            if "uid" not in st.session_state:
                st.warning(
                    "⚠️ Test your Odoo connection first."
                )
                st.stop()
    
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
                    "fields": ["name", "amount_total"]
                }
            )
    
            total_revenue = sum(
                order["amount_total"]
                for order in orders
            )
    
            total_orders = len(orders)
    
            avg_order = (
                total_revenue / total_orders
                if total_orders > 0
                else 0
            )
    
            st.metric(
                "💰 Total Revenue",
                f"${total_revenue:.2f}"
            )
    
            st.metric(
                "📦 Orders",
                total_orders
            )
    
            st.metric(
                "📈 Average Order Value",
                f"${avg_order:.2f}"
            )
    
            st.success(
                f"Loaded {total_orders} sales orders from Odoo."
            )
    
            revenues = [
                order["amount_total"]
                for order in orders
            ]
    
            st.subheader("📊 Revenue by Order")
    
            st.bar_chart(revenues)
          
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