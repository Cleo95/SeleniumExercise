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

    service_obj = Service('C:/Users/kleovouc/Documents/chromedriver-win64/chromedriver.exe')
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://www.amazon.com/")
    driver.maximize_window()
    driver.implicitly_wait(15)

    request.cls.driver = driver
    yield

