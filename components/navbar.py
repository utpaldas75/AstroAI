import streamlit as st

NAV_LINKS = ["Capabilities", "Reviews"]


def show_navbar():
    links_html = "".join(f'<a href="#{l.lower()}">{l}</a>' for l in NAV_LINKS)

    st.markdown(f"""
<div class="navbar">
<div class="logo">🔮 Astro<span>Mind</span></div>
<div class="nav-links">{links_html}</div>
<a class="nav-cta" href="App">Start Free Reading</a>
</div>
""", unsafe_allow_html=True)
