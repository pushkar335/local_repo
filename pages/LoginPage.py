from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_id = (By.ID, "user-name")
    password_id = (By.ID, "password")
    login_button_id = (By.ID, 'login-button')

    # def EnterUsername(self, username):
    #     self.driver.find_element(LoginPage.username_id).send_keys(username)
    #
    # def EnterPassword(self, password):
    #     self.driver.find_element(LoginPage.password_id).send_keys(password)
    #
    # def click_login(self):
    #     self.driver.find_element(LoginPage.login_button_id).click()
    #
    def EnterUsername(self, username):
        self.driver.find_element(*LoginPage.username_id).send_keys(username)

    def EnterPassword(self, password):
        self.driver.find_element(*LoginPage.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPage.login_button_id).click()
