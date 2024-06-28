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

    @allure.title("E2E Test of add to cart functionality")
    def test_005_search_item_add_to_cart(self):

        global price
        log = self.getLogger()

        homepage = HomePage(self.driver)
        resultspage = ResultsPage(self.driver)
        productpage = ProductPage(self.driver)
        cartpage = CartPage(self.driver)

        log.info("Starting test")
        time.sleep(5)
        log.info("Loading Home Page")
        with allure.step("Load the homepage"):
            homepage.load()
        time.sleep(5)
        log.info("search item")
        with allure.step("Search specific item"):
            homepage.getSearchBar().send_keys("computer monitor")
        time.sleep(5)
        with allure.step("Click search"):
            homepage.getSearchIcon().click()
        time.sleep(5)
        with allure.step("Click search"):
            resultspage.getSearchResults().click()

        # Check if Price exist
        try:
            price = self.product_price(element=productpage.getPrice())
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
