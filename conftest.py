import pytest
import logging
import os
from selenium import webdriver
from pages.login_page import LoginPage
from config.config_page import EMAIL, PASSWORD

# Configure logging
LOG_FILE = "test_log.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)






@pytest.fixture
def driver():

    """Initialize WebDriver before test and quit after test."""
    logging.info("Starting WebDriver")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://www.naukri.com/nlogin/login")
    yield driver
    logging.info("Quitting WebDriver")
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Fixture to log in before tests requiring authentication."""
    logging.info("Logging in before test execution")
    login_page = LoginPage(driver)
    login_page.user(EMAIL, PASSWORD)  # Use valid credentials
    return driver  # Return the driver in logged-in state

def pytest_configure(config):
    """Ensure reports directory is created in the root project folder"""
    reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)


def pytest_html_report_title(report):
    """Set custom title for the report"""
    report.title = "Test Automation Report"

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    """Log test results"""
    if report.when == "call":
        if report.failed:
            logging.error(f"TEST FAILED: {report.nodeid}")
        elif report.passed:
            logging.info(f"TEST PASSED: {report.nodeid}")
