import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from text_box_page import TextBoxPage

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@pytest.fixture
def driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_text_box_scenario(driver):
    logging.info("Test started: test_text_box_scenario")

    page = TextBoxPage(driver)
    page.load()
    logging.info("Page loaded")

    # Input data
    page.set_full_name("Donald Duck")
    page.set_email("donald.duck@example.com")
    page.set_current_address("56 Main St")
    page.set_permanent_address("379 Apple Rd")
    logging.info("Form data set")

    # Submit the form
    page.submit()
    logging.info("Form submitted")

    # Assertions to verify the output
    assert "Name:Donald Duck" in page.get_output_name(), "Name verification failed"
    assert "Email:donald.duck@example.com" in page.get_output_email(), "Email verification failed"
    assert "Current Address :56 Main St" in page.get_output_current_address(), "Current address verification failed"
    assert "Permananet Address :379 Apple Rd" in page.get_output_permanent_address(), "Permanent address verification failed"

    logging.info("All assertions passed")

    logging.info("Test completed: test_text_box_scenario")
