from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    subtotal = (By.XPATH, "//span[@id='sc-subtotal-amount-activecart']//span["
                          "@class='a-size-medium a-color-base sc-price "
                          "sc-white-space-nowrap']")

    delete = (By.XPATH, "//input[@data-action='delete']")
    amazonCartText = (By.XPATH, "//h1[@class='a-spacing-mini a-spacing-top-base']")
    subtotalQuantityText = (By.XPATH, "//span[@id='sc-subtotal-label-activecart']")

    def getSubTotal(self):
        return self.driver.find_element(*CartPage.subtotal)

    def getDeleteItemFromCart(self):
        return self.driver.find_element(*CartPage.delete)

    def getEmptyAmazonCart(self):
        return self.driver.find_element(*CartPage.amazonCartText)

    def getSubtotalQuantityText(self):
        return self.driver.find_element(*CartPage.subtotalQuantityText)
