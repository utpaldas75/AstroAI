import streamlit as st

st.set_page_config(
    page_title="AstroMind AI",
    page_icon="🔮",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""

<div align="center">

<div class="hero-title">
🔮 AstroMind AI
</div>

<div class="hero-subtitle">
AI Powered Vedic Astrology Platform
</div>

<div class="hero-text">
Discover your destiny through Artificial Intelligence,
Vedic Astrology, KP Astrology, Numerology and
Personalized Future Prediction.
</div>

</div>

""", unsafe_allow_html=True)

st.write("")
st.write("")

col1,col2,col3=st.columns([1,1,1])

with col2:
    if st.button("🚀 Get Started",use_container_width=True):
        st.success("Coming Soon")

st.write("")
st.write("")

c1,c2,c3=st.columns(3)

with c1:

    st.markdown("""

<div class="feature-card">

<div class="feature-icon">
🪐
</div>

<div class="feature-title">
Birth Chart
</div>

<div class="feature-text">
Generate professional Vedic birth charts instantly using AI.
</div>

</div>

""",unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class="feature-card">

<div class="feature-icon">
🤖
</div>

<div class="feature-title">
AI Astrologer
</div>

<div class="feature-text">
Chat with your personal AI astrologer anytime.
</div>

</div>

""",unsafe_allow_html=True)

with c3:

    st.markdown("""

<div class="feature-card">

<div class="feature-icon">
🌙
</div>

<div class="feature-title">
Daily Horoscope
</div>

<div class="feature-text">
Receive personalized horoscope and lucky guidance every day.
</div>

</div>

""",unsafe_allow_html=True)