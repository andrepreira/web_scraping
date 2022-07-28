

from drivers.firefox.driver_firefox import WebDriver

webdriver = WebDriver(False)

url = 'https://esaj.tjsc.jus.br/cpopg/open.do'
webdriver.driver.get(url)

webdriver.esperar_ate_elemento_ficar_visivel('#rc-anchor-container')