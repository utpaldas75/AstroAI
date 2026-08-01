import streamlit as st

TESTIMONIALS = [
    ("A", "Amit Sharma", "Software Engineer", "The AI predictions are surprisingly accurate, and the reports read like a real astrologer wrote them."),
    ("S", "Sarah Johnson", "Business Owner", "Clean, detailed birth chart analysis — I check my daily reading every morning."),
    ("R", "Rahul Das", "Student", "Marriage matching and career prediction actually helped me make a decision."),
]


def show_testimonials():
    st.markdown("""
<section id="reviews" class="section text-center">
<span class="eyebrow">Reviews</span>
<h2 class="section-title">Trusted by <em>thousands</em></h2>
</section>
""", unsafe_allow_html=True)

    cols = st.columns(3)
    for col, (avatar, name, role, text) in zip(cols, TESTIMONIALS):
        with col:
            st.markdown(f"""
<div class="testimonial-card">
<div class="testimonial-text">"{text}"</div>
<div class="user">
<div class="avatar">{avatar}</div>
<div>
<div class="user-name">{name}</div>
<div class="user-role">{role}</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)
