import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.carpages.ca/used-cars/search/?category_id=6')

soup = BeautifulSoup(page.text, 'lxml')
soup


df = pd.DataFrame({'Link': [''], 'Name': [''], 'Price': [''], 'Color': ['']})

counter = 0
while counter < 10:
    postings = soup.find_all('div', class_='media soft push-none rule')
    for post in postings:
        link = post.find('a', class_='media__img media__img--thumb').get('href')
        link_full = 'https://www.carpages.ca'+link
        name = post.find('h4', class_='hN').text.strip()
        price = post.find('strong', class_='delta').text
        color = post.find_all('div', class_='grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
        df = df.append({'Link': link_full, 'Name': name, 'Price': price, 'Color':color}, ignore_index = True)

    try:
        next_page = soup.find_all('a', class_='nextprev').get('href')
    except:
        next_page = soup.find('a', class_='nextprev').get('href')
         
    page = requests.get(next_page)
    soup = BeautifulSoup(page.text, 'lxml')
    counter += 1
