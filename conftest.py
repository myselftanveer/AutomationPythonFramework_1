import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome
from selenium.webdriver.firefox.service import Service as firefox

from utils import utils as utils
# from selenium.webdriver.firefox.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def test_setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        service_obj = chrome("C:/Users/Tanveer Shaikh/Downloads/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        print("firefox")
        service_obj1 = firefox("C:/Users/Tanveer Shaikh/Downloads/geckodriver-v0.32.0-win32/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj1)
    elif browser_name == "IE":
        print("IE driver")

    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.get(utils.URL)
    # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.driver = driver
    yield
    driver.close()
