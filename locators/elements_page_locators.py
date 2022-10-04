from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # contact Us form fields ss.com
    YOUR_FULL_NAME = (By.CSS_SELECTOR, 'input[name="your-name"]')
    YOUR_EMAIL = (By.CSS_SELECTOR, 'input[name="your-email"]')
    YOUR_LOCATION = (By.CSS_SELECTOR, 'input[name="your-location"]')
    YOUR_COMPANY = (By.CSS_SELECTOR, 'input[name="your-company"]')
    DESCRIBE_YOUR_PROJECT = (By.CSS_SELECTOR, 'input[name="your-description"]')
    COOKIES = By.XPATH, '//*[@id="cn-accept-cookie"]'
    UPLOAD_FILE = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[3]/div[2]/div/label')
    PRIVACY_POLICY = (By.CSS_SELECTOR, 'input[name="acceptance-box"]')
    PRIVACY_POLICY_1 = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[4]/div[1]/span')
    #PRIVACY_POLICY_1 = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[4]/div[1]/span/span/span/label/span')
    CONTACT_US = (By.CSS_SELECTOR, 'input[type="submit"]')
    #CONTACT_US = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[4]/div[2]/input')
    RESULT = (By.XPATH, '/html/body/main/div/article/div/div/h2')
    RESULT_FIELDS_HAVE_ERROR = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/div/p')


#class MainPage:
    # testing main page






    # contact Us form fields ss.com

    # YOUR_LOCATION = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[2]/div[3]')
    # NAME = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[2]/div[1]')
    # EMAIL = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[2]/div[2]')
    # COMPANY = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[2]/div[4]')
    # DESCRIBE_YOUR_PROJECT = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[3]/div[1]')
    # UPLOAD_FILE = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[3]/div[2]')
    # PRIVACY_POLICY = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[4]/div[1]')
    # CONTACT_US = (By.XPATH, '//*[@id="wpcf7-f716-o1"]/form/div[4]/div[2]')

    # created form

    # CREATED_YOUR_LOCATION = (By.CSS_SELECTOR, 'input[name="your-location"]')
    # CREATED_NAME = (By.CSS_SELECTOR, 'input[name="your-name"]')
    # CREATED_EMAIL = (By.CSS_SELECTOR, 'input[name="your-email"]')
    # CREATED_MESSAGE = (By.CSS_SELECTOR, 'input[name="your-message"]')
    # CREATED_PRIVACY_POLICY = (By.XPATH, 'input[//*[@id="wpcf7-f10029-o1"]/form/span[5]]')
    # CREATED_CONTACT_US = (By.XPATH, 'input[//*[@id="wpcf7-f10029-o1"]/form/span[5]]')
    #
    # # Thank you for your message.It has been sent.
    # CREATED_THANK_YOU = (By.XPATH, 'output[//*[@id="wpcf7-f10029-o1"]/form/div[2]]')