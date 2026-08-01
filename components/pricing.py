import streamlit as st

PLANS = ["Free", "Pro", "Enterprise"]
PRICES = ["$0", "$19", "$49"]
CTAS = [("Get Started", "ghost"), ("Buy Now", ""), ("Contact Us", "ghost")]
FEATURED_INDEX = 1  # Pro

# Each row: (label, [included for Free, Pro, Enterprise])
ROWS = [
    ("Daily Horoscope & Birth Chart", [True, True, True]),
    ("Numerology Report", [True, True, True]),
    ("AI Prediction & KP Astrology", [False, True, True]),
    ("Marriage Matching & Career Guidance", [False, True, True]),
    ("Premium & Unlimited Reports", [False, True, True]),
    ("API Access", [False, False, True]),
    ("Priority Support", [False, False, True]),
]


def show_pricing():
    st.markdown("""
<section id="pricing" class="section text-center">
<span class="eyebrow">Pricing</span>
<h2 class="section-title">Plans for every <em>stage</em></h2>
<p class="section-subtitle">Start free, upgrade when the AI is doing more of the work for you.</p>
</section>
""", unsafe_allow_html=True)

    header_cells = ['<div class="pt-cell"></div>']
    for i, (name, price, (cta, cta_style)) in enumerate(zip(PLANS, PRICES, CTAS)):
        col_class = "pt-cell pt-head col-featured" if i == FEATURED_INDEX else "pt-cell pt-head"
        header_cells.append(f"""
<div class="{col_class}">
<div class="pt-plan-name">{name}</div>
<div class="pt-plan-price">{price}<span>/mo</span></div>
<button class="pt-cta {cta_style}">{cta}</button>
</div>
""")

    row_cells = []
    for label, included in ROWS:
        row_cells.append(f'<div class="pt-cell pt-row-label">{label}</div>')
        for i, ok in enumerate(included):
            col_class = "pt-cell col-featured" if i == FEATURED_INDEX else "pt-cell"
            mark = '<span class="pt-check">✓</span>' if ok else '<span class="pt-dash">—</span>'
            row_cells.append(f'<div class="{col_class}">{mark}</div>')

    st.markdown(
        f'<div class="pricing-table">{"".join(header_cells)}{"".join(row_cells)}</div>',
        unsafe_allow_html=True,
    )
