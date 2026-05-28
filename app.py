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
# =====================================
# PREMIUM ANIMATED UI
# =====================================

st.markdown("""
<style>

/* =====================================
   GLOBAL BACKGROUND
===================================== */

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

/* =====================================
   ANIMATIONS
===================================== */

@keyframes fadeIn {

    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

@keyframes slideIn {

    from {
        opacity: 0;
        transform: translateX(-40px);
    }

    to {
        opacity: 1;
        transform: translateX(0px);
    }
}

@keyframes glowPulse {

    0% {
        box-shadow: 0 0 10px #3b82f6;
    }

    50% {
        box-shadow: 0 0 30px #3b82f6;
    }

    100% {
        box-shadow: 0 0 10px #3b82f6;
    }
}

@keyframes floating {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-12px);
    }

    100% {
        transform: translateY(0px);
    }
}

/* =====================================
   PAGE LOAD
===================================== */

.main .block-container {

    animation: fadeIn 0.8s ease;
}

/* =====================================
   SIDEBAR
===================================== */

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #000814,
        #001845
    );

    border-right: 1px solid rgba(255,255,255,0.1);

    box-shadow: 0 0 25px rgba(59,130,246,0.25);

    animation: slideIn 0.8s ease;
}

/* =====================================
   TITLES
===================================== */

h1, h2, h3 {

    color: white !important;

    font-weight: 800 !important;

    animation: slideIn 0.6s ease;
}

/* =====================================
   BUTTONS
===================================== */

.stButton > button {

    background: linear-gradient(
        135deg,
        #2563eb,
        #3b82f6
    ) !important;

    color: white !important;

    border-radius: 16px !important;

    border: none !important;

    font-weight: bold !important;

    transition: all 0.3s ease !important;

    padding: 12px 20px !important;
}

.stButton > button:hover {

    transform: translateY(-5px) scale(1.03);

    animation: glowPulse 2s infinite;

    box-shadow: 0 0 35px rgba(59,130,246,0.7);
}

/* =====================================
   INPUTS
===================================== */

.stTextInput input {

    background: rgba(255,255,255,0.08) !important;

    border-radius: 14px !important;

    border: 1px solid rgba(255,255,255,0.12) !important;

    color: white !important;

    transition: all 0.3s ease !important;
}

.stTextInput input:focus {

    border: 1px solid #60a5fa !important;

    box-shadow: 0 0 20px rgba(96,165,250,0.7) !important;
}

/* =====================================
   SUCCESS / ERROR BOXES
===================================== */

div[data-baseweb="notification"] {

    border-radius: 18px !important;

    animation: fadeIn 0.5s ease;
}

/* =====================================
   DATAFRAME
===================================== */

[data-testid="stDataFrame"] {

    border-radius: 20px;

    overflow: hidden;

    animation: fadeIn 0.8s ease;
}

/* =====================================
   METRIC CARDS
===================================== */

.metric-card {

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.1);

    backdrop-filter: blur(15px);

    border-radius: 20px;

    padding: 25px;

    transition: all 0.3s ease;

    animation: fadeIn 0.8s ease;
}

.metric-card:hover {

    transform: translateY(-8px);

    box-shadow: 0 0 35px rgba(59,130,246,0.35);
}

/* =====================================
   FLOATING PARTICLES
===================================== */

.particle {

    position: fixed;

    width: 14px;

    height: 14px;

    border-radius: 50%;

    background: #60a5fa;

    box-shadow: 0 0 25px #60a5fa;

    z-index: -1;

    animation: floating 6s infinite ease-in-out;
}

.dot1 {
    left: 10%;
    top: 20%;
}

.dot2 {
    left: 80%;
    top: 30%;
}

.dot3 {
    left: 50%;
    top: 70%;
}

.dot4 {
    left: 20%;
    top: 85%;
}

.dot5 {
    left: 90%;
    top: 60%;
}

/* =====================================
   SCROLLBAR
===================================== */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #001233;
}

::-webkit-scrollbar-thumb {

    background: #3b82f6;

    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #60a5fa;
}

</style>

<div class="particle dot1"></div>
<div class="particle dot2"></div>
<div class="particle dot3"></div>
<div class="particle dot4"></div>
<div class="particle dot5"></div>

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
st.session_state.logged_in = True
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