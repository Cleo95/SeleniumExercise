from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    subtotal = (By.XPATH, "//span[@id='sc-subtotal-amount-activecart']//span["
                          "@class='a-size-medium a-color-base sc-price "
                          "sc-white-space-nowrap']")

    def getSubTotal(self):
        return self.driver.find_element(*CartPage.subtotal)
