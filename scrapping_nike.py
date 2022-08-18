import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Chrome("C:/Users/naaom/Downloads/chromedriver.exe")
url = driver.get('https://www.nike.com/w/sale-3yaep')
page_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(10)
    last_height = driver.execute_script('return document.body.scrollHeight')
    if last_height == page_height:
        break
    last_height = page_height
    
df = pd.DataFrame({'Link':[''], 'Product':[''], 'Subtitle':[''], 'Price':[''],
                   'Discount Price':[''], 'Colors':['']})
soup = BeautifulSoup(driver.page_source, 'lxml')
products = soup.find_all('div', class_='product-card__body')
for product in products:
    try:
        link = product.find('a', class_='product-card__link-overlay').get('href')
        product_name = product.find('div', class_='product-card__title').text
        subtitle = product.find(('div'), class_='product-card__subtitle').text
        price = product.find('div', class_='product-price is--striked-out css-0').text
        discount_price = product.find('div', class_='product-price is--current-price css-1ydfahe').text
        colors = product.find('div', class_='product-card__product-count').text
        df = df.append({'Link':link, 'Product':product_name, 'Subtitle':subtitle, 
                        'Price':price,'Discount Price':discount_price, 
                        'Colors':colors}, ignore_index=True)
    except:
        pass
    
df.to_csv('C:/Users/naaom/Downloads/nike.csv')
    

