import requests
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
soup

premarket = soup.find('bg-quote', class_='value').text
premarket

closing_price_outcome = soup.find('td', class_='table__cell u-semi').text

fifty_two_week_range_min = soup.find_all('div', class_='range__header')[2]
fifty_two_week_range_min_outcome = fifty_two_week_range_min.find_all('span', class_='primary')[0].text

fifty_two_week_range_max = soup.find_all('div', class_='range__header')[2]
fifty_two_week_range_max_outcome = fifty_two_week_range_max.find_all('span', class_='primary')[1].text

analyst_rating_outcome = soup.find('li', class_='analyst__option active').text

print(f"{premarket}, {closing_price_outcome}, {fifty_two_week_range_min_outcome}, {fifty_two_week_range_max_outcome}, {analyst_rating_outcome}")