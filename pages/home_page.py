from locators.home_locators import HomeLocators

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.name_label = HomeLocators.NAME_LABEL
        self.role_label = HomeLocators.ROLE_LABEL
        self.office_label = HomeLocators.OFFICE_LABEL
        self.logout_button = HomeLocators.LOGOUT_BUTTON
        self.logout_button_popup=HomeLocators.LOGOUT_BUTTON_POP_UP

    def get_name(self):
        return self.driver.find_element(*self.name_label).text

    def get_role(self):
        return self.driver.find_element(*self.role_label).text

    def get_office(self):
        return self.driver.find_element(*self.office_label).text

    def logout(self):
        self.driver.find_element(*self.logout_button).click()
        self.driver.find_element(*self.logout_button_popup).click()
