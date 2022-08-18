import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.nfl.com/standings/league/2020/REG'
requests.get(url)
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', {'summary': 'Standings - Detailed View'})

headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

headers

df = pd.DataFrame(columns=headers)

for row in table.find_all('tr')[1:]:
    full_names = row.find_all('td')[0].find('div', class_='d3-o-club-fullname').text.strip()
    data = row.find_all('td')[1:]
    row_data = [td.text.strip() for td in data]
    row_data.insert(0, full_names)
    length = len(df)
    df.loc[length] = row_data

df
