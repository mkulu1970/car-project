import streamlit as st
st.title("Welcome")
name=st.text_input("Enter name")
age=st.number_input("Enter age",min_value=1, max_value=100, step=1)
st.selectbox("Enter your skills", ["Pytho"])
st.button("show")