from locators.login_locators import LoginLocators
from config.appium_config import CREDENTIALS  # Import credentials from config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = LoginLocators.USERNAME_FIELD
        self.password_field = LoginLocators.PASSWORD_FIELD
        self.login_button = LoginLocators.LOGIN_BUTTON
        self.error_message = LoginLocators.ERROR_MESSAGE
        self.error_button=LoginLocators.ERROR_BUTTON
        print("In init of login", self.driver)


    def enter_username(self, username):
        print("In enter_username of login", self.driver)
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()


    def is_error_message_displayed(self):
        try:
            self.driver.find_element(*self.error_message)
            return True  # Returns True if the element is visible
        except Exception as e:
            print(f"Error message not displayed: {e}")
            return False

    def click_error_popup_button(self):
        self.driver.find_element(*self.error_button).click()


    def validate_login_page(self):
        try:
            element = self.driver.find_element(*self.login_button)
            return element.is_displayed()  # Returns True if the element is visible
        except Exception as e:
            print(f"Error message not displayed: {e}")
            return False

    def login(self, username=None, password=None):
        if username is None:
            username = CREDENTIALS["username"]
        if password is None:
            password = CREDENTIALS["password"]
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
