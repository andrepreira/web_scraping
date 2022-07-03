from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

url = 'http://selenium.dev/'
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
browser.get(url)