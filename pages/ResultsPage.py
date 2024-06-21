from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultsPage:

    def __init__(self, driver):
        self.driver = driver

    results = (By.XPATH, "//span[@data-component-type='s-product-image']")

    def getResults(self):
        wait = WebDriverWait(self.driver, 10)
        results = wait.until(EC.presence_of_all_elements_located(ResultsPage.results))
        return results
