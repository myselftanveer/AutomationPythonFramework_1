from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import pytest


@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_login(self):
        login = LoginPage(self.driver)
        login.getUserName().send_keys(utils.USERNAME)
        login.getPassword().send_keys(utils.PASSWORD)
        login.clickLogin().click()

    def test_logout(self):
        home = HomePage(self.driver)
        home.getDropdown()
        home.clickLogout()