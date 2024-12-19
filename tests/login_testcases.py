# tests/test_login.py
import time

import pytest
from appium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from config.appium_config import get_appium_driver, CREDENTIALS
from appium.options.common import AppiumOptions



class TestLogin:

    @pytest.fixture(scope="class")
    def setup(self):
        # Initialize the Appium driver
        self.driver = get_appium_driver()
        print("setup##########",self.driver)
        yield self.driver
        self.driver.quit()


    def test_failed_login(self, setup):
        # self.driver = get_appium_driver()
        # print("Test_fal", self.driver)
        login_page = LoginPage(setup)
        login_page.login("wrongemail@tfl.gov.uk", "wrongpassword")
        assert login_page.is_error_message_displayed(), "Error message is not displayed on failed login."
        login_page.click_error_popup_button()

    def test_successful_login(self, setup):
        login_page = LoginPage(setup)
        login_page.login()
        home_page = HomePage(setup)
        assert home_page.get_name() == "Emma Smith", f"Name does not match. Expected Emma Smith, got {home_page.get_name()}"
        assert home_page.get_role() == "Senior Test Analyst", f"Role does not match. Expected Senior Test Analyst, got {home_page.get_role()}"
        assert home_page.get_office() == "Pier Walk", f"Office does not match. Expected Pier Walk, got {home_page.get_office()}"

    def test_logout(self, setup):
        login_page = LoginPage(setup)
        login_page.login()
        home_page = HomePage(setup)
        home_page.logout()
        assert login_page.validate_login_page(), "Login screen is not displayed after logout."
