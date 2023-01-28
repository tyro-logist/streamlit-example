import streamlit as st

st.title("Hello World")
st.write("This is a Streamlit app that says 'Hello World'.")

if st.button("Say Hello"):
    st.write("Hello World!")
