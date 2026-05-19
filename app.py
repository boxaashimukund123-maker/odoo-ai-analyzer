# =========================================
# LOGIN PAGE
# =========================================

if not st.session_state.logged_in:

    st.markdown("""
    <div class="login-card">

        <div class="login-title">
            🚀 AI ERP
        </div>

        <div class="login-sub">
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

            st.session_state.logged_in = True

            st.success("Login successful 🚀")

            time.sleep(1)

            st.rerun()

        else:
            st.error("Invalid credentials")