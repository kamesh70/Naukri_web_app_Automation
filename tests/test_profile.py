import pytest
import logging
from pages.profile_page import ProfilePage
import time

@pytest.mark.usefixtures("logged_in_driver")
class TestProfile:

    """before test excution this function automatically called """
    @pytest.fixture(autouse=True)
    def setup(self, logged_in_driver):
        """ Initialize ProfilePage once per test """
        self.profile_page = ProfilePage(logged_in_driver)
        # self.profile_page.view_profile_click()


    def test_profile(self):
        self.profile_page.view_profile_click()
        try:
            url = self.profile_page.current_page_url
            assert  url == "https://www.naukri.com/mnjuser/profile", f"excepted url {url} is not correct"
        except AssertionError:
            self.profile_page.capture_screenshot("test_profile")  # Capture screenshot on failure
            logging.error("Login failed! Screenshot captured.")
            raise

    def test_profile_percentage(self):
        self.profile_page.view_profile_click()
        try:
            profile = self.profile_page.view_profile_percentage()
            assert profile.text == "100%" ,f" profile percentage is {profile.text} "
            url = self.profile_page.current_page_url
            assert url == "https://www.naukri.com/mnjuser/profile", f"excepted url {url} is not correct"
        except AssertionError:
            self.profile_page.capture_screenshot("test_profile_percentage")  # Capture screenshot on failure
            logging.error("Login failed! Screenshot captured.")
            raise

    def test_upload_resume(self):
        self.profile_page.view_profile_click()

        try:
            msg = self.profile_page.upload_resume()
            assert msg.text == "GreenTick\nSuccess\nResume has been successfully uploaded."

        except AssertionError:
            self.profile_page.capture_screenshot("test_profile_percentage")  # Capture screenshot on failure
            logging.error("Login failed! Screenshot captured.")
            raise

    def test_delete_resume(self):
        self.profile_page.view_profile_click()
        try:
            msg = self.profile_page.delete_resume()
            assert msg.text == "GreenTick\nSuccess\nAttached Resume has been successfully deleted."
        except AssertionError:
            self.profile_page.capture_screenshot("test_profile_percentage")  # Capture screenshot on failure
            logging.error("Login failed! Screenshot captured.")
            raise

    def test_edit_photo_click(self):
        self.profile_page.view_profile_click()

        try:
            self.profile_page.edit_photo()
            self.profile_page.edit_photo_cancel()
        except Exception as e:
            self.profile_page.capture_screenshot("test_edit_photo")  # Capture screenshot on failure
            logging.error(f"test_edit_photo.{e}")
            raise



    def test_reupload_resume(self):
        self.profile_page.view_profile_click()

        try:
            msg = self.profile_page.re_uplaod_resume()
            assert msg.text == "GreenTick\nSuccess\nResume has been successfully uploaded."
        except AssertionError:
            self.profile_page.capture_screenshot("test_profile_percentage")  # Capture screenshot on failure
            logging.error("Login failed! Screenshot captured.")
            raise