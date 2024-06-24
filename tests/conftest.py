import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--headless")

    service_obj = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")

    # driver.get("https://www.amazon.com/")
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    request.cls.driver = driver
    yield
    driver.close()

