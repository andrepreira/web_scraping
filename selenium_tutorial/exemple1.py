from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

url = 'http://www.yahoo.com'
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
browser.get(url)
assert 'Yahoo' in browser.title

elem = browser.find_element(By.NAME, 'p')  #find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()