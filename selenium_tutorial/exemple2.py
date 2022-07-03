import unittest
from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)