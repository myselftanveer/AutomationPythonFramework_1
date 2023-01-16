from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    #
    #     self.userName = (By.XPATH, "//input[@name='username']")
    #     self.password = (By.XPATH, "//input[@name='password']")
    #     self.loginBtn = (By.XPATH, "//button[@type='submit']")
    #
    # def getUserName(self, name):
    #     self.driver.find_element(self.userName).clear()
    #     self.driver.find_element(self.userName).send_keys(name)
    #
    # def getPassword(self, passd):
    #     self.driver.find_element(self.password).clear()
    #     self.driver.find_element(self.password).send_keys(passd)
    #
    # def clickLogin(self):
    #     self.driver.find_element(self.loginBtn).click()

    userName = (By.XPATH, "//input[@name='username']")
    passd = (By.XPATH, "//input[@name='password']")
    loginBtn = (By.XPATH, "//button[@type='submit']")

    def getUserName(self):
        return self.driver.find_element(*LoginPage.userName)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.passd)

    def clickLogin(self):
        return self.driver.find_element(*LoginPage.loginBtn)
