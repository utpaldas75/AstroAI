import streamlit as st


def show_footer():
    """Thin, fixed bottom bar — replaces the old full-height footer/CTA.

    Holds just the logo plus two actions: Pricing and Start Free Reading.
    """
    st.markdown("""
<div class="fixed-footer">
<div class="fixed-footer-inner">
<div class="logo">🔮 Astro<span>Mind</span></div>
<div class="fixed-footer-actions">
<a class="btn-pricing" href="#">Pricing</a>
<a class="btn-primary" href="App">Start Free Reading</a>
</div>
</div>
</div>
""", unsafe_allow_html=True)
