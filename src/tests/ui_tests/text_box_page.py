from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TextBoxPage:
    URL = 'https://demoqa.com/text-box'

    # Locator definitions
    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def set_full_name(self, full_name):
        self.driver.find_element(*self.FULL_NAME_INPUT).send_keys(full_name)

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_current_address(self, current_address):
        self.driver.find_element(*self.CURRENT_ADDRESS_INPUT).send_keys(current_address)

    def set_permanent_address(self, permanent_address):
        self.driver.find_element(*self.PERMANENT_ADDRESS_INPUT).send_keys(permanent_address)

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_output_name(self):
        return self.driver.find_element(*self.OUTPUT_NAME).text

    def get_output_email(self):
        return self.driver.find_element(*self.OUTPUT_EMAIL).text

    def get_output_current_address(self):
        return self.driver.find_element(*self.OUTPUT_CURRENT_ADDRESS).text

    def get_output_permanent_address(self):
        return self.driver.find_element(*self.OUTPUT_PERMANENT_ADDRESS).text