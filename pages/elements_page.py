import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):

        self.element_is_visible(self.locators.NAME).send_keys('test')
        self.element_are_visible(self.locators.PRIVACY_POLICY).click()
        time.sleep(5)

    # def fill_all_fields(self):
    #     self.element_are_visible(self.locators.YOUR_LOCATION).click()
    #     self.element_are_visible(self.locators.NAME).send_keys('test')
    #     self.element_are_visible(self.locators.EMAIL).send_keys('test@test.test')
    #     self.element_are_visible(self.locators.MESSAGE).send_keys('test')
    #     self.element_are_visible(self.locators.PRIVACY_POLICY).click()
    #     self.element_are_visible(self.locators.CONTACT_US).click()
    #     time.sleep(5)
