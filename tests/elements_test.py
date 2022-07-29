import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://www.symphony-solutions.eu/contact-us/')
            text_box_page.open()
            text_box_page.fill_all_fields()
