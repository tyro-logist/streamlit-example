"""import streamlit as st
import pandas as pd

st.title("Hello World")
st.write("This is a Streamlit app that says 'Hello World'.")

if st.button("Say Hello"):
    st.write("Hello World!")
    
url = "https://raw.githubusercontent.com/tyro-logist/Ontario-GREENHOUSE-GAS-EMISSIONS-REPORTING-BY-FACILITY/main/GHG_Data_2010_2020_data_Dec162021.csv"
df = pd.read_csv(url, encoding = "ISO-8859-1")
df.head()"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CO2e Emissions over Time")

url = "https://raw.githubusercontent.com/tyro-logist/Ontario-GREENHOUSE-GAS-EMISSIONS-REPORTING-BY-FACILITY/main/GHG_Data_2010_2020_data_Dec162021.csv"
data = pd.read_csv(url, encoding = "ISO-8859-1")

st.write("Data loaded from:", url)

# Create line plot
plt.plot(data['Year'], data['Total CO2e from all sources in CO2e (t)'])
plt.xlabel('Year')
plt.ylabel('Total CO2e from all sources in CO2e (t)')
st.pyplot()


