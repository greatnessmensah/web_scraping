import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.com/s/Accra--Ghana/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&place_id=ChIJc6e3soSQ3w8RYQbYT8_WxlM&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

df = pd.DataFrame({'Link': [''], 'Title': [''], 'Description': [''], 'Price': [''], 'Rating':[''], })

while True:
    postings = soup.find_all('div', class_='c4mnd7m dir dir-ltr')
    for post in postings:
        try:
            link = post.find('a', class_='ln2bl2p dir dir-ltr').get('href')
            full_link = 'https://www.airbnb.com'+link
            description = post.find('span', class_='t19nnqvo dir dir-ltr').text
            title = post.find('div', class_='t1jojoys dir dir-ltr').text
            price = post.find('span', class_='_tyxjp1').text
            rating = post.find('span', class_='ru0q88m dir dir-ltr').text
            df = df.append({'Link': full_link, 'Title': title, 'Description': description, 'Price': price, 'Rating': rating, }, ignore_index=True)
        except:
            pass
    try:
        next_page = soup.find_all('a', {'aria-label': 'Next'}).get('href')
        next_page = 'https://www.airbnb.com'+next_page
    except:
        next_page = soup.find('a', {'aria-label': 'Next'}).get('href')
        next_page = 'https://www.airbnb.com'+next_page
        
    next_page_url = next_page
    new_page = requests.get(url)
    new_soup = BeautifulSoup(new_page.text, 'lxml')
    
    
df.to_csv('airbnb.csv')
    