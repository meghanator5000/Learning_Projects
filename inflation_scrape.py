import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from pandas import DataFrame
import html5lib
import matplotlib.pyplot as plt

URL = 'https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find( "table" )
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]

df = pd.read_html(str(table))[0]
df.columns = df.iloc[1]
df = df.iloc[2:] 
df = df.fillna(0)

df = df.apply(pd.to_numeric, errors='coerce')

df.plot(x='Year', y='Avg-Avg', kind='line', title='US Inflation over Time', legend = None)
plt.show()
