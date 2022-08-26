import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://symphony-solutions.com/contact-us')
            text_box_page.open()
            time.sleep(5)
            text_box_page.fill_all_fields()
            time.sleep(5)
            driver.get_screenshot_as_file("CONTACT_US.png")
