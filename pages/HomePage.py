from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    selectAll = (By.XPATH, "//a[@id='nav-hamburger-menu']")
    electronicsOption = (By.XPATH, "//a[@class='hmenu-item']//div[text()='Electronics']")
    computerAndAccessoriesOption = (By.XPATH, "//a[normalize-space()='Computers & Accessories']")

    def getAllNavBar(self):
        return self.driver.find_element(*HomePage.selectAll)

    def getElectronicsOption(self):
        return self.driver.find_element(*HomePage.electronicsOption)

    def getComputerAndAccessoriesOption(self):
        wait = WebDriverWait(self.driver, 10)
        computerAndAccessories = self.driver.execute_script("arguments[0].click();", wait.until(
            EC.element_to_be_clickable(HomePage.computerAndAccessoriesOption)))
        return computerAndAccessories
