import time
import pytest
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.YOUR_FULL_NAME).send_keys('test')
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys('test@test.test')
        self.element_is_visible(self.locators.YOUR_LOCATION).send_keys('test')
        self.element_is_visible(self.locators.YOUR_COMPANY).send_keys('test')
        self.element_is_visible(self.locators.DESCRIBE_YOUR_PROJECT).send_keys('test')
        self.element_is_visible(self.locators.PRIVACY_POLICY_1).click()
        # self.element_is_visible(self.locators.UPLOAD_FILE).click()
        # self.element_is_visible(self.locators.UPLOAD_FILE).send_keys('C:/automation/test.pdf')
        self.element_is_visible(self.locators.CONTACT_US).click()
        time.sleep(2)

    def check_field(self):
        result = self.element_is_visible(self.locators.RESULT).text
        return result
