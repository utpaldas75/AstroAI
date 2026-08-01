import math

import streamlit as st

CAPABILITIES = [
    ("Birth Chart", "Full Vedic chart with planetary positions, generated in seconds."),
    ("AI Prediction", "Career, relationship, finance and health forecasts from your chart."),
    ("Marriage Matching", "Kundli matching with a compatibility score and detailed notes."),
    ("Daily Horoscope", "A fresh reading each morning, built from live planetary transits."),
]

SYSTEMS = [
    ("🪐", "Vedic"),
    ("⭐", "KP"),
    ("🔢", "Numerology"),
    ("✋", "Palmistry"),
    ("🃏", "Tarot"),
    ("💎", "Gemstone"),
]


def _orbit() -> str:
    """Position the 6 astrology systems around a ring — echoes the hero's zodiac wheel."""
    radius = 128
    nodes = []
    for i, (icon, label) in enumerate(SYSTEMS):
        angle = math.radians(i * 60 - 90)
        x = 150 + radius * math.cos(angle)
        y = 150 + radius * math.sin(angle)
        nodes.append(
            f'<div class="orbit-node" style="left:{x:.0f}px; top:{y:.0f}px;">'
            f'<div class="orbit-node-icon">{icon}</div>'
            f'<div class="orbit-node-label">{label}</div></div>'
        )
    return f"""
<div class="orbit">
<div class="orbit-ring"></div>
{''.join(nodes)}
<div class="orbit-core">🔮</div>
</div>
"""


def show_capabilities():
    st.markdown("""
<section id="capabilities" class="section text-center">
<span class="eyebrow">Platform</span>
<h2 class="section-title">Six systems, cross-checked by <em>one</em> engine</h2>
<p class="section-subtitle">
AstroMind AI reads your chart through six traditional systems and reconciles them into
one prediction — so nothing you're told rests on a single method.
</p>
</section>
""", unsafe_allow_html=True)

    left, right = st.columns([1.1, 1])

    with left:
        items_html = "".join(
            f'<div class="capability-item"><div class="capability-dot"></div>'
            f'<div class="capability-title">{title}</div>'
            f'<div class="capability-text">{text}</div></div>'
            for title, text in CAPABILITIES
        )
        st.markdown(f'<div class="capability-list">{items_html}</div>', unsafe_allow_html=True)

    with right:
        st.markdown(f'<div class="orbit-wrap">{_orbit()}</div>', unsafe_allow_html=True)
