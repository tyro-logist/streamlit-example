import streamlit as st
import pandas as pd

st.title("Hello World")
st.write("This is a Streamlit app that says 'Hello World'.")

if st.button("Say Hello"):
    st.write("Hello World!")
    
url = "https://raw.githubusercontent.com/tyro-logist/Ontario-GREENHOUSE-GAS-EMISSIONS-REPORTING-BY-FACILITY/main/GHG_Data_2010_2020_data_Dec162021.csv"
df = pd.read_csv(url, encoding = "ISO-8859-1")
df.head()
