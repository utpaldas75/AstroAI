import streamlit as st

st.set_page_config(
    page_title="AstroMind AI — App",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

with open("assets/style.css", encoding="utf-8") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

if "authed" not in st.session_state:
    st.session_state.authed = False

TOOLS = ["Dashboard", "Birth Chart", "AI Astrologer", "Daily Prediction", "Compatibility", "Settings", "Admin"]


# ----------------------------------------------------------------
# AUTH GATE (Login / Register combined)
# ----------------------------------------------------------------
def show_auth():
    _, mid, _ = st.columns([1, 1.1, 1])
    with mid:
        with st.container(border=True):
            st.markdown(
                '<div class="auth-title">🔮 AstroMind AI</div>'
                '<div class="auth-sub">Sign in to reach your dashboard and readings.</div>',
                unsafe_allow_html=True,
            )
            st.write("")
            login_tab, register_tab = st.tabs(["Login", "Register"])

            with login_tab:
                st.text_input("Email", key="login_email", placeholder="you@example.com")
                st.text_input("Password", key="login_pw", type="password", placeholder="••••••••")
                if st.button("Log in", use_container_width=True, key="login_btn"):
                    st.session_state.authed = True
                    st.rerun()
                st.caption("Demo mode — any email/password signs you in. Wire up `database/auth.py` to make this real.")

            with register_tab:
                st.text_input("Full name", key="reg_name")
                st.text_input("Email", key="reg_email")
                st.text_input("Password", key="reg_pw", type="password")
                if st.button("Create account", use_container_width=True, key="reg_btn"):
                    st.session_state.authed = True
                    st.rerun()


# ----------------------------------------------------------------
# TOP BAR (logo + log out) — tool switching now lives in st.tabs below,
# so the whole app stays on this ONE page instead of spawning more pages.
# ----------------------------------------------------------------
def show_topbar():
    left, right = st.columns([3, 1])
    with left:
        st.markdown('<div class="logo">🔮 Astro<span>Mind</span></div>', unsafe_allow_html=True)
    with right:
        if st.button("Log out", use_container_width=True):
            st.session_state.authed = False
            st.rerun()
    st.markdown("<hr style='border-color:var(--border-soft);margin-top:8px;'>", unsafe_allow_html=True)


def page_head(title, subtitle):
    st.markdown(f'<div class="page-head"><h2>{title}</h2><p>{subtitle}</p></div>', unsafe_allow_html=True)


# ----------------------------------------------------------------
# TOOL SCREENS
# ----------------------------------------------------------------
def show_dashboard():
    page_head("Welcome back", "Here's a snapshot of your astrology activity.")
    stats = [("3", "Charts generated"), ("12", "AI readings"), ("87%", "Match score avg"), ("5", "Saved reports")]
    cards = "".join(
        f'<div class="dash-card"><div class="dash-num">{n}</div><div class="dash-label">{l}</div></div>'
        for n, l in stats
    )
    st.markdown(f'<div class="dash-grid">{cards}</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="result-card">Jump into <b>Birth Chart</b> to generate a new reading, or ask the '
        '<b>AI Astrologer</b> a question — connect the modules in <b>astrology/</b> and <b>ai/</b> to bring these to life.</div>',
        unsafe_allow_html=True,
    )


def show_birth_chart():
    page_head("Birth Chart", "Enter birth details to generate a Vedic chart.")
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Full name", key="bc_name")
        st.date_input("Date of birth", key="bc_dob")
    with c2:
        st.time_input("Time of birth", key="bc_time")
        st.text_input("Place of birth", key="bc_place")
    if st.button("Generate chart"):
        st.markdown(
            '<div class="result-card">Chart generation isn\'t wired up yet — this is where '
            '<b>astrology/calculator.py</b> and <b>astrology/houses.py</b> would return planetary '
            'positions and house placements for the details above.</div>',
            unsafe_allow_html=True,
        )


def show_ai_astrologer():
    page_head("AI Astrologer", "Ask anything about your chart, timing, or a decision you're weighing.")
    st.markdown(
        '<div class="chat-bubble ai">Hi! I can walk you through your chart once it\'s connected — try asking me a question.</div>',
        unsafe_allow_html=True,
    )
    question = st.text_input("Your question", key="ai_q", placeholder="Is this a good time to change careers?")
    if st.button("Ask") and question:
        st.markdown(f'<div class="chat-bubble user">{question}</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="chat-bubble ai">Placeholder response — connect <b>ai/chatbot.py</b> to generate a '
            'real, chart-aware answer here.</div>',
            unsafe_allow_html=True,
        )


def show_daily_prediction():
    page_head("Daily Prediction", "Today's transit-based reading.")
    st.markdown(
        '<div class="result-card">📅 <b>Today:</b> A steady day for focused work — favorable for finishing '
        'tasks you\'ve been putting off. (Placeholder — wire up <b>astrology/transit.py</b> for real transits.)</div>',
        unsafe_allow_html=True,
    )


def show_compatibility():
    page_head("Compatibility", "Compare two birth charts for a match score.")
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Your name", key="comp_a")
        st.date_input("Your date of birth", key="comp_a_dob")
    with c2:
        st.text_input("Partner's name", key="comp_b")
        st.date_input("Partner's date of birth", key="comp_b_dob")
    if st.button("Check compatibility"):
        st.markdown(
            '<div class="result-card">💞 Match score: <b>—</b> (placeholder). '
            'Connect <b>astrology/doshas.py</b> and a scoring routine to compute a real result.</div>',
            unsafe_allow_html=True,
        )


def show_settings():
    page_head("Settings", "Manage your profile and preferences.")
    st.text_input("Display name", key="set_name")
    st.text_input("Email", key="set_email")
    st.selectbox("Preferred astrology system", ["Vedic", "KP", "Western"], key="set_system")
    st.button("Save changes")


def show_admin():
    page_head("Admin", "Platform overview.")
    st.markdown('<span class="badge-role">Admin only</span>', unsafe_allow_html=True)
    stats = [("1,204", "Total users"), ("38", "Signups today"), ("$4,120", "MRR"), ("99.9%", "Uptime")]
    cards = "".join(
        f'<div class="dash-card"><div class="dash-num">{n}</div><div class="dash-label">{l}</div></div>'
        for n, l in stats
    )
    st.markdown(f'<div class="dash-grid" style="margin-top:16px;">{cards}</div>', unsafe_allow_html=True)


TOOL_SCREENS = {
    "Dashboard": show_dashboard,
    "Birth Chart": show_birth_chart,
    "AI Astrologer": show_ai_astrologer,
    "Daily Prediction": show_daily_prediction,
    "Compatibility": show_compatibility,
    "Settings": show_settings,
    "Admin": show_admin,
}


# ----------------------------------------------------------------
# ROUTE — only two pages exist in this whole app: this file (App)
# and main.py (Home). Every tool below lives inside st.tabs on this
# single page instead of adding more page files.
# ----------------------------------------------------------------
if not st.session_state.authed:
    show_auth()
else:
    show_topbar()
    tabs = st.tabs(TOOLS)
    for tab, tool in zip(tabs, TOOLS):
        with tab:
            TOOL_SCREENS[tool]()
