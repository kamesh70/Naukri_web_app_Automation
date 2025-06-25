from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import config.config_page
from pages.base_page import BasePage
import time
from pynput.keyboard import Key,Controller
from config.config_page import RESUME_FILE


class ProfilePage(BasePage):
    PROFILEPATH = (By.XPATH,"//div[@class='view-profile-wrapper']")
    PROFILE_PERCENTAGE = (By.XPATH ,"//div[@class='user-percentage high']")
    RESUME = (By.XPATH, "//input[@value='Update resume']")
    MESSAGEBOX= (By.XPATH, "//div[@class='msgBox success ']")
    DELETE_RESUME = (By.XPATH,"//span[@data-title='delete-resume']/i")
    CONFIRM = (By.XPATH,"//button[@class='btn-dark-ot']")
    UPLOAD_RESUME = (By.XPATH, "//span[@class='dummyUploadNewCTA']")
    DELETE = (By.XPATH, "//div[@class='ltCont']/div[@class='lightbox model_open flipOpen']//div[@class='action right-align']/button")
    CROSSLAYER =(By.XPATH,"//div[@id='photoCropper' ]/div[@class='crossLayer']")
    MOVE_TO =(By.XPATH,"//div[@class='photoTrigger']")
    image=(By.XPATH,"//img[@class='user-img']")
    edit_icon_photo =(By.XPATH,"//div[@class='content-wrap']")


    def view_profile_click(self):
        self.click(self.PROFILEPATH)

    def view_profile_percentage(self):
        return self.find_element(self.PROFILE_PERCENTAGE)

    def upload_resume(self):
        self.click(self.RESUME)
        try:
            keyboard = Controller()
            keyboard.type(RESUME_FILE)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            return self.find_element(self.MESSAGEBOX)
        except Exception as e:
            print(f"error message {e}")
            return False

    def delete_resume(self):
        self.click(self.DELETE_RESUME)
        self.click(self.DELETE)
        return self.find_element(self.MESSAGEBOX)

    def re_uplaod_resume(self):
        self.click(self.UPLOAD_RESUME)
        try:
            keyboard = Controller()
            keyboard.type(RESUME_FILE)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            return self.find_element(self.MESSAGEBOX)
        except Exception as e:
            print(f"error message {e}")
            return False


    def edit_photo(self):
        self.move_element(self.image)
        self.click(self.edit_icon_photo)

    def edit_photo_cancel(self):
        self.click(self.CROSSLAYER)

