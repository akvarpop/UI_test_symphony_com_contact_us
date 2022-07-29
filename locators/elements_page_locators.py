from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # contact Us form fields

    YOUR_LOCATION = (By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/span[1]/select')
    NAME = (By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/span[2]/input')
    EMAIL = (By.CSS_SELECTOR, 'input[name="your-email"]')
    MESSAGE = (By.CSS_SELECTOR, 'input[name="your-message"]')
    PRIVACY_POLICY = (By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/span[5]/span/span/label/span')
    CONTACT_US = (By.XPATH, 'input[//*[@id="wpcf7-f10029-o1"]/form/span[5]]')

    # created form

    CREATED_YOUR_LOCATION = (By.CSS_SELECTOR, 'input[name="your-location"]')
    CREATED_NAME = (By.CSS_SELECTOR, 'input[name="your-name"]')
    CREATED_EMAIL = (By.CSS_SELECTOR, 'input[name="your-email"]')
    CREATED_MESSAGE = (By.CSS_SELECTOR, 'input[name="your-message"]')
    CREATED_PRIVACY_POLICY = (By.XPATH, 'input[//*[@id="wpcf7-f10029-o1"]/form/span[5]]')
    CREATED_CONTACT_US = (By.XPATH, 'input[//*[@id="wpcf7-f10029-o1"]/form/span[5]]')

    # Thank you for your message.It has been sent.
    CREATED_THANK_YOU = (By.XPATH, 'output[//*[@id="wpcf7-f10029-o1"]/form/div[2]]')