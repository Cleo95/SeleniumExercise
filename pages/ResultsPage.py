from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultsPage:

    def __init__(self, driver):
        self.driver = driver

    results = (By.XPATH, "//span[@data-component-type='s-product-image']")
    searchResults = (By.XPATH, "//img[@data-image-index='4']")
    def getResults(self):
        wait = WebDriverWait(self.driver, 10)
        results = wait.until(EC.presence_of_all_elements_located(ResultsPage.results))
        return results

    def getSearchResults(self):
        return self.driver.find_element(*ResultsPage.searchResults)
