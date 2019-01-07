from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Driver.WebDriverManager import WebDriverManager

class WebElementHelper(object):
    _driver=None

    def __init__(self, brw):
        self._driver = WebDriverManager.get_web_driver(brw)
        self._wait = WebDriverWait(self._driver,10)
    
    def get_web_element_by_xpath(self, xpath):
        _locator = By.XPATH,xpath
        return self._wait.until(EC.presence_of_element_located(_locator))
    
    def get_web_elements_by_xpath(self, xpath):
        return self._wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def open(self, path):
        self._driver.get(path)
    
    def close(self):
        self._driver.quit()