
import streamlit as st

st.title("Mentor Mantra - AI Learning Buddy")

topic = st.text_input("Enter Topic")

if st.button("Generate"):
    st.write("Java OOP Concepts explained...")
