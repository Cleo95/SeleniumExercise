import time
import re

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.HomePage import HomePage
from pages.ResultsPage import ResultsPage
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        global price_text
        log = self.getLogger()

        homepage = HomePage(self.driver)
        resultspage = ResultsPage(self.driver)
        productpage = ProductPage(self.driver)
        cartpage = CartPage(self.driver)

        homepage.getAllNavBar().click()
        time.sleep(5)
        homepage.getElectronicsOption().click()

        homepage.getComputerAndAccessoriesOption()
        time.sleep(5)

        results = resultspage.getResults()
        # Check if enough results exist
        try:
            self.search_results(num=3, results=results)
        except AssertionError as e:
            print(f"Test failed: {e}")
        finally:
            self.driver.quit()

        # Check if Price exist

        try:
            self.product_price(element=productpage.getPrice())
        except AssertionError as e:
            print(f"Test failed: {e}")
        finally:
            self.driver.quit()

        time.sleep(5)
        checkAddToCartButton = self.check_exists_by_xpath(xpath=productpage.getAddToCartButtonString())

        if checkAddToCartButton:
            productpage.getAddToCartButton().click()
        else:
            print("Add to Cart button not found")

        assert productpage.getAddedToCartMessage().text.strip() == "Added to Cart", "Item not added to Cart"

        productpage.getGoToCartButton().click()

        subtotal = cartpage.getSubTotal().text.strip()
        print(subtotal)

        # Verify Item from list has same price as Item in Cart
        assert subtotal == f"{price_text}", "Element does not match"
