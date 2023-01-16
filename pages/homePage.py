from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self, driver):
        self.drievr = driver

    profile = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    logout = (By.LINK_TEXT, "Logout")

    def getDropdown(self):
        self.drievr.find_element(*HomePage.profile).click()

    def clickLogout(self):
        self.drievr.find_element(*HomePage.logout).click()
