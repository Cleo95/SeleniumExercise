import inspect
import logging

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def search_results(num, results):

        # Check the number of results and raise an error if not enough
        assert len(results) >= num, "Not enough search results found."

        # Iterate through the results and click the 4th one
        for index, result in enumerate(results):
            element = num - 1
            if index == element:  # Index 3 corresponds to the 4th element (0-based indexing)
                result.click()
                break  # Exit the loop after clicking the 4th result

    def product_price(self, element):

        assert element is not None, "Price element not found."

        price_text = self.driver.execute_script("return arguments[0].textContent;", element).strip()
        print(f"The price of the product is: {price_text}")
        return price_text
