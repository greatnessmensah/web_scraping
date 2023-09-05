from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome("C:/Users/naaom/Downloads/chromedriver.exe")
driver.get('https://twitter.com/i/flow/login')
time.sleep(60)
celebrity = 'Ryan Reynolds'
user_name = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
user_name.send_keys('username')
user_name.send_keys(Keys.ENTER)
time.sleep(5)
password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys('password')
password.send_keys(Keys.ENTER)
search = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
search.send_keys(celebrity)
search.send_keys(Keys.ENTER)
time.sleep(5)
people = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]').click()
time.sleep(5)
profile = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]').click()
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'lxml')
postings = soup.find_all('div', class_ = 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0') 
tweets = []
while True:
    for post in postings:
        tweets.append(post.text)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_ = 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
    tweets2 = list(set(tweets))
    if len(tweets2) > 5:
        break
        












