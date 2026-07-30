import streamlit as st

st.set_page_config(page_title="Birth Chart", page_icon="🪐")

st.title("🪐 Birth Chart Generator")

name = st.text_input("Full Name")

birth_date = st.date_input("Birth Date")

birth_time = st.time_input("Birth Time")

birth_place = st.text_input("Birth Place")

if st.button("Generate Birth Chart"):
    st.success("Birth details submitted successfully!")