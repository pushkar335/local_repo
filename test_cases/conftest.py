from selenium import webdriver
from utilities.readConfigParser import Config
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(autouse=True, scope='class')
def setup(request):

    # driver = webdriver.Chrome()
    # driver.get(Config.get_base_URL())
    # driver.maximize_window()
    # request.cls.driver = driver
    # yield
    # driver.close()
    if browser == 'chrome':
        print("Launching Chrome Browser")
        driver = webdriver.Chrome()
        driver.get(Config.get_base_URL())

    elif browser == 'firefox':
        print("Launching Firefox Browser")
        driver = webdriver.Firefox()
        driver.get(Config.get_base_URL())

    elif browser == 'edge':
        print("Launching Edge Browser")
        driver = webdriver.Edge()
        driver.get(Config.get_base_URL())
    # if browser == 'headless':
    else:
        # print("Headless mode")
        # chrome_options = webdriver.FirefoxOptions()
        # chrome_options.add_argument("headless")
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        driver.maximize_window()

    return driver
