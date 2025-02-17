import streamlit as st
import pandas as pd
import requests, random
from bs4 import BeautifulSoup

st.title("✨Welcome To The Quote Scraper✨")
st.write("This is a simpe web scraper, where you can find all types of quotes! To start, just pick a category of a quote in the dropdown menu. After that a random quote will appear with that category!")

tag = st.selectbox('Pick A Category:', ['love', 'humor', 'books', 'reading', 'inspirational', 'life', 'friendship', 'Truth'])
st.button("Generate")

url = f'https://quotes.toscrape.com/tag/{tag}/'
baseUrl = 'https://quotes.toscrape.com/'

res = requests.get(url)
content = BeautifulSoup(res.content, 'html.parser')

quotes = content.find_all('div', class_='quote')
quote = quotes[random.randint(1, len(quotes)-1)]

text = quote.find('span', class_='text').text
author = quote.find('small', class_='author').text
link = baseUrl + quote.find('a')['href']

st.write(f"""{text} - **{author}**""")
