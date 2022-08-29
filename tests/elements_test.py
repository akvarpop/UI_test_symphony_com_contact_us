import time

import pytest

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://symphony-solutions.com/contact-us')
            text_box_page.open()
            text_box_page.fill_all_fields()
            driver.get_screenshot_as_file("CONTACT_US.png")
            assert text_box_page.check_field() == 'Thank you for your interest!', print('Contact Form Send)')
            # if text_box_page.check_field() == 'Thank you for your interest!':
            #     print('Contact Form Send)')
            # else:
            #     print('Contact Form Not Send')
            #print(text_box_page.check_field())

