from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "usernameField")
    PASSWORD = (By.ID, "passwordField")
    LOGIN_BTN = (By.XPATH, "//button[text()='Login']")
    VERIFY_LOGIN = (By.XPATH, "//a[text()=' profile']")
    ERROR_MSG = (By.XPATH, "//span[@class='col s12 commonErrorMsg']")
    USER_ERROR = (By.XPATH,"//span[@id='usernameField_err']")
    PASSWORD_ERROR = (By.XPATH,"//span[@id='passwordField_err']")

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def user(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        self.find_element(self.VERIFY_LOGIN)


    def login_verify(self):
        self.find_element(self.VERIFY_LOGIN)

    def error_message(self):
        return self.find_element(self.ERROR_MSG)

    def empty_user_error(self):
        return self.find_element(self.USER_ERROR)

    def empty_password_error(self):
        return self.find_element(self.PASSWORD_ERROR)
