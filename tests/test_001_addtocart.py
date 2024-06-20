import time
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest
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

        # Click computer and accessories By.XPATH, "//a[normalize-space()='Computers & Accessories']"
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((homepage.computerAndAccessoriesOption()))))

        results = resultspage.getResults()

        if len(results) >= 4:
            # Use a for loop to iterate through the results
            for index, result in enumerate(results):
                if index == 2:  # Index 3 corresponds to the 4th element (0-based indexing)
                    result.click()
                    break  # Exit the loop after clicking the 4th result
        else:
            print("Not enough search results found.")

        try:
            element = productpage.getPrice()
            # Use execute_script to return the text of the element
            price_text = self.driver.execute_script("return arguments[0].textContent;", element).strip()
            print(f"The price of the product is: {price_text}")

            # Extract numbers from the text using regular expressions
            numbers = re.findall(r"[-+]?\d*\.\d+|\d+", price_text)

            if numbers:
                # Convert extracted number strings to floats and print them
                for num in numbers:
                    print(float(num))
            else:
                print("No numbers found in the text.")

        except Exception as e:
            print(f"An error occurred: {e}")

        checkAddToCartButton = self.check_exists_by_xpath(xpath=productpage.getAddToCartButtonString())

        if checkAddToCartButton:
            productpage.getAddToCartButton().click()
        else:
            print("Add to Cart button not found")

        assert productpage.getAddedToCartMessage() == "Added to Cart", "Item not added to Cart"

        productpage.getGoToCartButton().click()

        subtotal = cartpage.getSubTotal().text.strip()
        print(subtotal)

        # Verify Item from list has same price as Item in Cart
        assert subtotal == f"{price_text}", "Element does not match"
