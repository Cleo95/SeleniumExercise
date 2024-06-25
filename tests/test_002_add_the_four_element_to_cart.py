import time
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage
from pages.ResultsPage import ResultsPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    @allure.title("Add the four element to cart")
    def test_002_add_the_four_element_to_cart(self):

        global price
        log = self.getLogger()

        homepage = HomePage(self.driver)
        resultspage = ResultsPage(self.driver)
        productpage = ProductPage(self.driver)
        cartpage = CartPage(self.driver)

        time.sleep(5)
        with allure.step("Load the homepage"):
            homepage.load()
        time.sleep(5)
        with allure.step("Get the All Nav bar"):
            homepage.getAllNavBar().click()
        time.sleep(5)
        with allure.step("Click the Electronics Option"):
            homepage.getElectronicsOption().click()
        time.sleep(5)
        with allure.step("Go to Computer And Accessories"):
            homepage.getComputerAndAccessoriesOption()

        time.sleep(5)
        results = resultspage.getResults()
        # Check if enough results exist
        try:
            with allure.step("Verify if enough results exist"):
                self.search_results(num=4, results=results)
        except AssertionError as e:
            self.capture_screenshot("Not Enough Results")
            allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
            raise
        time.sleep(5)

        # Check if Price exist
        try:
            with allure.step("Verify if Product has Price"):
                newElement = productpage.getPrice()
                assert newElement is not None, "Element does not exist."
                price = self.driver.execute_script("return arguments[0].textContent;", newElement).strip()
                print(f"The price of the product is: {price}")
        except NoSuchElementException as e:
            self.capture_screenshot("No Price Exist")
            allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
            raise

        # Verify id Add to Cart button exist and click it
        try:
            with allure.step("Verify if Add to Cart Button exist"):
                element = productpage.getAddToCartButton()
                assert element is not None, "Element does not exist."
                element.click()
        except NoSuchElementException as e:
            self.capture_screenshot("No Add to Cart Button exist")
            allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
            raise

        # Assert if Item is added to Cart
        with allure.step("Verify if Items are added to Cart"):
            assert productpage.getAddedToCartMessage().text.strip() == "Added to Cart", "Item not added to Cart"

        # Press Go To Cart Button
        with allure.step("Click the go to Cart Button"):
            productpage.getGoToCartButton().click()

        # Check the Total Price of item from cart
        subtotal = cartpage.getSubTotal().text.strip()
        print(subtotal)

        # Verify Item from list has same price as Item in Cart
        with allure.step("Verify Item from list has same price as Item in Cart"):
            assert subtotal == f"{price}", "Element does not match"
