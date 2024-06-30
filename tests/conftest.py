import configparser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions

driver = None

config = configparser.ConfigParser()
config.read('config/config.ini')

implicit_wait = config['timeouts']['implicit_wait']


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    options = Options()
    # options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("start-maximized")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/87.0.4280.88 Safari/537.36")

    firefoxOptions = FirefoxOptions()
    # firefoxOptions.add_argument("--headless=new")
    firefoxOptions.add_argument("--window-size=1920,1080")
    firefoxOptions.add_argument("start-maximized")
    firefoxOptions.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/87.0.4280.88 Safari/537.36")

    edgeOptions = EdgeOptions()
    # edgeOptions.add_argument("--headless=new")
    edgeOptions.add_argument("--window-size=1920,1080")
    edgeOptions.add_argument("start-maximized")
    edgeOptions.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/87.0.4280.88 Safari/537.36")
    service_obj = Service()

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj, options=firefoxOptions)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=service_obj, options=edgeOptions)
    driver.implicitly_wait(float(implicit_wait))
    request.cls.driver = driver
    yield
    driver.close()
