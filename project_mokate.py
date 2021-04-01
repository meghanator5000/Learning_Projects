import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from pandas import DataFrame

URL = 'https://www.crisisctr.org/about/board-of-directors/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

members = soup.find_all("ul") 

details = []
names = []
positions = []
companies = []

for member in members:
    for row in member.find_all('strong'):
        name = row.text
        names.append(name)
        
    for row in member.select("li > em:nth-of-type(1)"):
        position = row.text
        positions.append(position)
    
    for row in member.select("li > em:last-of-type"):
        company = row.text
        companies.append(company)

df = pd.DataFrame(list(zip(names, positions, companies)), columns = ['Name', 'Position', 'Company'])

df['Company'].where(df['Position'] != df['Company'], "N/A", inplace = True)
df['Name'] = df['Name'].str.replace(' –', '')
df = df.apply(lambda x: x.str.strip())
print(df)