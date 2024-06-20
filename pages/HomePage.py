from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


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
        return self.driver.find_element(*HomePage.computerAndAccessoriesOption)
