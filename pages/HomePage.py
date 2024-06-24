from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    selectAll = (By.XPATH, "//a[@id='nav-hamburger-menu']")
    electronicsOption = (By.XPATH, "//a[@class='hmenu-item']//div[text()='Electronics']")
    computerAndAccessoriesOption = (By.XPATH, "//a[normalize-space()='Computers & Accessories']")

    def load(self):
        self.driver.get("https://www.amazon.com/")

    def getAllNavBar(self):
        wait = WebDriverWait(self.driver, 15)
        allNavBar = wait.until(EC.presence_of_element_located(HomePage.selectAll))
        return allNavBar

    def getElectronicsOption(self):
        wait = WebDriverWait(self.driver, 15)
        electronics = wait.until(EC.element_to_be_clickable(HomePage.electronicsOption))
        return electronics

    def getComputerAndAccessoriesOption(self):
        wait = WebDriverWait(self.driver, 20)
        computerAndAccessories = self.driver.execute_script("arguments[0].click();", wait.until(
            EC.element_to_be_clickable(HomePage.computerAndAccessoriesOption)))
        return computerAndAccessories
