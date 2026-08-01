import streamlit as st

ZODIAC_GLYPHS = ["♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓"]

STATS = [
    ("25K+", "Charts read"),
    ("99%", "Model accuracy"),
    ("24/7", "AI availability"),
]


def _zodiac_wheel() -> str:
    """Build the 12-tick zodiac wheel from the glyph list instead of hand-writing each tick."""
    ticks = "".join(
        f'<div class="zodiac-tick" style="transform:rotate({i * 30}deg)">'
        f'<span style="transform:rotate({-i * 30}deg) translateY(-4px)">{glyph}</span>'
        f"</div>"
        for i, glyph in enumerate(ZODIAC_GLYPHS)
    )
    return f"""
<div class="zodiac-wheel">
<div class="zodiac-ring"></div>
<div class="zodiac-ring inner"></div>
{ticks}
<div class="zodiac-core">🔮</div>
</div>
"""


def show_hero():
    left, right = st.columns([1.1, 1])

    with left:
        stats_html = "".join(
            f'<div><div class="hero-stat-num">{num}</div>'
            f'<div class="hero-stat-label">{label}</div></div>'
            for num, label in STATS
        )
        st.markdown(f"""
<div class="hero">
<span class="eyebrow">AI-Powered Astrology</span>
<h1 class="hero-title">Discover your future with <em>AstroMind AI</em></h1>
<p class="hero-text">
Accurate, AI-interpreted readings across Vedic and KP astrology, numerology, palmistry
and tarot — one platform for career, marriage and life-path guidance.
</p>
<div class="hero-buttons">
<a class="btn-primary" href="App">🚀 Get Started</a>
<button class="btn-secondary">▶ Live Demo</button>
</div>
<div class="hero-stats">{stats_html}</div>
</div>
""", unsafe_allow_html=True)

    with right:
        st.markdown(f'<div class="wheel-wrap">{_zodiac_wheel()}</div>', unsafe_allow_html=True)
