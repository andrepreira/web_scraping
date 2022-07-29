

from drivers.firefox.driver_firefox import WebDriver
from selenium.webdriver.common.by import By

webdriver = WebDriver()

url1 = 'https://esaj.tjsc.jus.br/cpopg/open.do'
url2 = 'https://esaj.tjms.jus.br/cpopg5/open.do'
url3 = 'https://consultasaj.tjam.jus.br/cpopg/open.do'
webdriver.driver.get(url2)

# webdriver.esperar_ate_elemento_ficar_visivel('.form__consultar-processos__item--captcha')
webdriver.esperar_ate_elemento_ficar_visivel('.grecaptcha-badge')
webdriver.driver.find_element(By.CSS_SELECTOR,value='.grecaptcha-badge')
