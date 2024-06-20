from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    addToCartButtonString = "//input[@id='add-to-cart-button']"
    addToCartButton = (By.XPATH, "//input[@id='add-to-cart-button']")
    price = (By.XPATH, "//span[@class='a-price aok-align-center']//span[@class='a-offscreen']")
    goToCartButton = (By.XPATH, "//span[@id='sw-gtc']//span[@class='a-button-inner']")
    addedToCartMessage = (By.XPATH, "//h1[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']")

    def getPrice(self):
        return self.driver.find_element(*ProductPage.price)

    def getAddToCartButtonString(self):
        return self.driver.find_element(*ProductPage.addToCartButtonString)

    def getAddToCartButton(self):
        return self.driver.find_element(*ProductPage.addToCartButton)

    def getGoToCartButton(self):
        return self.driver.find_element(*ProductPage.goToCartButton)

    def getAddedToCartMessage(self):
        return self.driver.find_element(*ProductPage.addedToCartMessage)
