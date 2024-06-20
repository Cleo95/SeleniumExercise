from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ResultsPage:

    def __init__(self, driver):
        self.driver = driver

    results = (By.XPATH, "//span[@data-component-type='s-product-image']")

    def getResults(self):
        return self.driver.find_element(*ResultsPage.results)
