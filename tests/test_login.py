import pytest
import logging

from pages.login_page import LoginPage
import time



class TestLogin:
    def test_valid_login(self,driver):
        logging.info("Starting test: test_valid_login")
        # driver.get("https://www.naukri.com/nlogin/login")

        login_page = LoginPage(driver)
        login_page.login("kameshsulakshane@gmail.com", "Rovikamesh@70")

        try:
            login_page.login_verify()
            assert driver.title == "Home | Mynaukri" , f"Unexpected error message: {driver.title}"
            assert "https://www.naukri.com/mnjuser/homepage" in driver.current_url
            logging.info("Login successful!")
        except AssertionError:
            login_page.capture_screenshot("test_valid_login")  # Capture screenshot on failure
            logging.error("Login failed! Screenshot captured.")
            raise
    def test_invalid_username(self,driver):
        logging.info("Starting test: test_invalid_login")
        login_page = LoginPage(driver)
        login_page.login("invalid_user@gmail.com", "admin")

        # Wait for the error message to appear
        try:
            status = login_page.error_message()
            assert status.is_displayed()

            logging.info("Invalid login test passed! Error message displayed.")
        except Exception as e:
            login_page.capture_screenshot("test_invalid_username")  # Capture screenshot on failure
            logging.error(f"Invalid login test failed! Screenshot captured. Error: {e}")
            raise

    def test_empty_username(self,driver):
        logging.info("Starting test: test_empty_username")
        login_page = LoginPage(driver)
        login_page.login("", "admin")

        # Wait for the error message to appear
        try:
            user = login_page.empty_user_error()
            print(user.text)
            assert user.text == "Email ID/Username cannot be left blank" ,f"Unexpected error message: {user.text}"

            logging.info("Invalid login test passed! Error message displayed.")
        except Exception as e:
            login_page.capture_screenshot("test_invalid_username")  # Capture screenshot on failure
            logging.error(f"Invalid login test failed! Screenshot captured. Error: {e}")
            raise

    def test_empty_password(self,driver):

        login_page = LoginPage(driver)
        login_page.login("ram@gmail.com", "")

        # Wait for the error message to appear
        try:
            password = login_page.empty_password_error()
            print(password.text)
            assert password.text == "Password cannot be left blank" ,f"Unexpected error message: {password.text}"

            logging.info("Invalid login test passed! Error message displayed.")
        except Exception as e:
            login_page.capture_screenshot("test_invalid_username")  # Capture screenshot on failure
            logging.error(f"Invalid login test failed! Screenshot captured. Error: {e}")
            pytest.fail("Etest_empty_password")

    def test_empty_username_password(self,driver):
        logging.info("Starting test: test_empty_password")
        login_page = LoginPage(driver)
        login_page.login("", "")
        # Wait for the error message to appear
        try:
            user = login_page.empty_user_error()
            assert user.text == "Email ID/Username cannot be left blank" ,f"Unexpected error message: {user.text}"
            password = login_page.empty_password_error()
            assert password.text == "Password cannot be left blank" ,f"Unexpected error message: {password.text}"

            logging.info("Invalid login test passed! Error message displayed.")
        except Exception as e:
            login_page.capture_screenshot("test_invalid_username")  # Capture screenshot on failure
            # driver.capture_screenshot("screenshots/test_empty_username_password.png")
            logging.error(f"Invalid login test failed! Screenshot captured. Error: {e}")
            pytest.fail("Empty username & password test failed!")

    def test_invalid_login(self,driver):
        logging.info("Starting test: test_invalid_login")
        login_page = LoginPage(driver)
        login_page.login("invalid_user@gmail.com", "wrongpassword123")

        # Wait for the error message to appear
        try:
            status=login_page.error_message()
            assert status.is_displayed()

            logging.info("Invalid login test passed! Error message displayed.")
        except Exception as e:
            login_page.capture_screenshot("test_invalid_username")  # Capture screenshot on failure
            logging.error(f"Invalid login test failed! Screenshot captured. Error: {e}")
            raise