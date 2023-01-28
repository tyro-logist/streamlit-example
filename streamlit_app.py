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
from bs4 import BeautifulSoup
import requests
from collections import Counter

st.title("Most Frequently Used Words in a Website")

def get_word_count(url):
    # Make a request to the website
    try:
        page = requests.get(url)
    except:
        st.write("The connection failed, please enter a different url")
        return
    soup = BeautifulSoup(page.content, 'html.parser')

    # Remove HTML tags and convert to lowercase
    text = soup.get_text().lower()
    for tag in soup.find_all(['script', 'style']):
        tag.decompose()
    text = soup.get_text().lower()
    text = "".join([c if c.isalnum() or c.isspace() else " " for c in text])
    # Split the text into words
    words = text.split()

    # Use the counter function to count the frequency of each word
    word_count = Counter(words)

    return word_count

url = st.text_input("Enter the URL:")
if st.button("Submit"):
    word_count = get_word_count(url)
    if word_count:
        st.write("The most frequently used words are:")
        st.write(word_count.most_common(10))



