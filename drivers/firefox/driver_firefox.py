from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class WebDriver:
    def __init__(self, headless: True | False = True) -> None:
        ops = webdriver.FirefoxOptions()
        ops.headless = headless
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=ops)
    
    def esperar(self, tempo_maximo: int = 10):
        return WebDriverWait(self.driver, tempo_maximo)
    
    def esperar_ate_elemento_ficar_visivel(self, css_selector_elemento: str, tempo_maximo: int = 10):
        return self.esperar(tempo_maximo).until(expected_conditions.visibility_of_element_located(
           ( By.CSS_SELECTOR, css_selector_elemento)
        ))