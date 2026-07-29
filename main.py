import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AstroMind AI",
    page_icon="🔮",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🔮 AstroMind AI")
st.sidebar.write("AI-Powered Astrology Platform")

menu = st.sidebar.selectbox(
    "Select a Feature",
    [
        "Home",
        "Birth Chart",
        "Daily Horoscope",
        "AI Chat"
    ]
)

# -----------------------------
# Home Page
# -----------------------------
if menu == "Home":
    st.title("🔮 AstroMind AI")
    st.write("Welcome to your AI-powered astrology software!")

# -----------------------------
# Birth Chart Page
# -----------------------------
elif menu == "Birth Chart":

    st.title("🪐 Birth Chart Generator")

    st.write("Please enter your birth details below.")

    name = st.text_input("👤 Full Name")

    birth_date = st.date_input("📅 Birth Date")

    birth_time = st.time_input("🕒 Birth Time")

    birth_place = st.text_input("📍 Birth Place")

    if st.button("Generate Birth Chart"):
        st.success("Birth details submitted successfully!")

        st.subheader("Entered Information")

        st.write(f"**Name:** {name}")
        st.write(f"**Birth Date:** {birth_date}")
        st.write(f"**Birth Time:** {birth_time}")
        st.write(f"**Birth Place:** {birth_place}")

# -----------------------------
# Daily Horoscope Page
# -----------------------------
elif menu == "Daily Horoscope":

    st.title("🌞 Daily Horoscope")

    st.info("This feature will be added soon.")

# -----------------------------
# AI Chat Page
# -----------------------------
elif menu == "AI Chat":

    st.title("🤖 AI Astrology Assistant")

    st.info("AI chat feature coming soon.")