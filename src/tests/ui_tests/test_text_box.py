import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from text_box_page import TextBoxPage
from src.logging.log_config import setup_logging

logger = setup_logging()

@pytest.fixture
def driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_text_box_scenario(driver):
    logger.info("Test started: test_text_box_scenario")

    try:
        page = TextBoxPage(driver)
        page.load()
        logger.info("Page loaded successfully")

        # Input data
        logger.debug("Setting full name to Donald Duck")
        page.set_full_name("Donald Duck")
        logger.debug("Setting email to donald.duck@example.com")
        page.set_email("donald.duck@example.com")
        logger.debug("Setting current address to 56 Main St")
        page.set_current_address("56 Main St")
        logger.debug("Setting permanent address to 379 Apple Rd")
        page.set_permanent_address("379 Apple Rd")
        logger.info("All form data set")

        # Submit the form
        page.submit()
        logger.info("Form submitted")

        # Assertions to verify the output
        assert "Name:Donald Duck" in page.get_output_name(), "Name verification failed"
        assert "Email:donald.duck@example.com" in page.get_output_email(), "Email verification failed"
        assert "Current Address :56 Main St" in page.get_output_current_address(), "Current address verification failed"
        assert "Permananet Address :379 Apple Rd" in page.get_output_permanent_address(), "Permanent address verification failed"
        logger.info("All assertions passed successfully")

    except Exception as e:
        logger.error(f"An error occurred during the test: {e}")
        raise

    logger.info("Test completed: test_text_box_scenario")