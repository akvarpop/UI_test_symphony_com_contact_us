import time
import pytest
from generator.generator import generated_person, generated_person_ua
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        """Використовуємо бібліотеку Faker для заповнення форми"""
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        location = person_info.location
        company = person_info.company
        describe_your_project = person_info.describe_your_project

        self.element_is_visible(self.locators.YOUR_FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys(email)
        self.element_is_visible(self.locators.YOUR_LOCATION).send_keys(location)
        self.element_is_visible(self.locators.YOUR_COMPANY).send_keys(company)
        self.element_is_visible(self.locators.DESCRIBE_YOUR_PROJECT).send_keys(describe_your_project)
        self.element_is_visible(self.locators.COOKIES).click()
        # self.go_to_element(self.locators.CONTACT_US)
        self.element_is_presents(self.locators.PRIVACY_POLICY_1).click()
        # self.element_is_visible(self.locators.UPLOAD_FILE).click()
        # self.element_is_visible(self.locators.UPLOAD_FILE).send_keys('C:/automation/test.pdf')
        self.element_is_presents(self.locators.CONTACT_US).click()
        return full_name, email, location, company, describe_your_project

    """return повертає що було відправленно у форму, для перевірки данніх в assert"""

    def fill_all_fields_ua(self):
        """Використовуємо бібліотеку Faker для заповнення форми"""
        person_info = next(generated_person_ua())
        full_name = person_info.full_name
        email = person_info.email
        location = person_info.location
        company = person_info.company
        describe_your_project = person_info.describe_your_project

        self.element_is_visible(self.locators.YOUR_FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys(email)
        self.element_is_visible(self.locators.YOUR_LOCATION).send_keys(location)
        self.element_is_visible(self.locators.YOUR_COMPANY).send_keys(company)
        self.element_is_visible(self.locators.DESCRIBE_YOUR_PROJECT).send_keys(describe_your_project)
        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_presents(self.locators.PRIVACY_POLICY_1).click()
        self.element_is_presents(self.locators.CONTACT_US).click()
        return full_name, email, location, company, describe_your_project

    """return повертає що було відправленно у форму, для перевірки данніх в assert"""

    def fill_all_fields_large(self):
        self.element_is_visible(self.locators.YOUR_FULL_NAME).send_keys('test' * 20)
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys('test@test.test')
        self.element_is_visible(self.locators.YOUR_LOCATION).send_keys('test' * 20)
        self.element_is_visible(self.locators.YOUR_COMPANY).send_keys('test' * 20)
        self.element_is_visible(self.locators.DESCRIBE_YOUR_PROJECT).send_keys('test' * 20)
        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.PRIVACY_POLICY_1).click()
        # self.element_is_visible(self.locators.UPLOAD_FILE).click()
        # self.element_is_visible(self.locators.UPLOAD_FILE).send_keys('C:/automation/test.pdf')
        self.element_is_visible(self.locators.CONTACT_US).click()

    def check_field(self):
        result = self.element_is_visible(self.locators.RESULT).text
        return result

    def fill_all_fields_short(self):
        self.element_is_visible(self.locators.YOUR_FULL_NAME).send_keys('t')
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys('t@test.t')
        self.element_is_visible(self.locators.YOUR_LOCATION).send_keys('t')
        self.element_is_visible(self.locators.YOUR_COMPANY).send_keys('t')
        self.element_is_visible(self.locators.DESCRIBE_YOUR_PROJECT).send_keys('t')
        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.PRIVACY_POLICY_1).click()
        self.element_is_visible(self.locators.CONTACT_US).click()

    def fill_fields_without_email(self):
        self.element_is_visible(self.locators.YOUR_FULL_NAME).send_keys('test')
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys('')
        self.element_is_visible(self.locators.YOUR_LOCATION).send_keys('test')
        self.element_is_visible(self.locators.YOUR_COMPANY).send_keys('test')
        self.element_is_visible(self.locators.DESCRIBE_YOUR_PROJECT).send_keys('test')
        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.PRIVACY_POLICY_1).click()
        self.element_is_visible(self.locators.CONTACT_US).click()

    def check_field_have_error(self):
        result = self.element_is_visible(self.locators.RESULT_FIELDS_HAVE_ERROR).text
        return result


    def fill_fields_without_full_name(self):
        self.element_is_visible(self.locators.YOUR_FULL_NAME).send_keys('')
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys('test@test.test')
        self.element_is_visible(self.locators.YOUR_LOCATION).send_keys('test')
        self.element_is_visible(self.locators.YOUR_COMPANY).send_keys('test')
        self.element_is_visible(self.locators.DESCRIBE_YOUR_PROJECT).send_keys('test')
        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.PRIVACY_POLICY_1).click()
        self.element_is_visible(self.locators.CONTACT_US).click()