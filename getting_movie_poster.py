from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome("C:/Users/naaom/Downloads/chromedriver.exe")
driver.get('https://www.google.com/')
box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('top 100 movies of all time')
box.send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/a/h3').click()
time.sleep(5)
driver.execute_script('window.scrollTo(0, 10000)')
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[49]/div[2]/a/img').screenshot('C:/Users/naaom/Downloads/poster.png')

