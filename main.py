import streamlit as st

from components.navbar import show_navbar
from components.hero import show_hero
from components.capabilities import show_capabilities
from components.testimonials import show_testimonials
from components.footer import show_footer

st.set_page_config(
    page_title="AstroMind AI",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

with open("assets/style.css", encoding="utf-8") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

SECTIONS = (
    show_navbar,
    show_hero,
    show_capabilities,
    show_testimonials,
    show_footer,
)

for render_section in SECTIONS:
    render_section()
