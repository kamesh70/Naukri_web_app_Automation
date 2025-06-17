import logging
import time

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from selenium import  webdriver
from selenium.webdriver.common.by import By
class  HomePage(BasePage):
    RECORD_HEADER = (By.XPATH, "//div[@class='reco-head']//a[@class='view-all-link']/span[text()='View all']")
    SPE_HEADER  = (By.XPATH,"//div[@class='spc__header']/a[text()='View all']")
    NVITES= (By.XPATH, "//div[@class='rmj-cont']//a[text()='View all']")
    METER = (By.XPATH, "//div[@class='whatma-header']//a[text()='View all']")
    TOP_COMPANY = (By.XPATH, "//div[@class='top-comp-container']//a[text()='View all']")
    INTERVIEW_EXP = (By.XPATH, "//div[@class='interview-exp-container']//a[text()='View all']")
    INTERVIEW_QUES = (By.XPATH, "//div[@class='interview-ques-container']//a[text()='View all']")
    BLOG = (By.XPATH, "//div[@class='blogs-container']//a[text()='View all']")
    UPDATE_CITY  = (By.XPATH ,"//em[@class='naukicon naukicon-ot-pencil']")
    SAVE = (By.XPATH,"//div[@class='naukri-drawer right open naukri-drawer-perf']//button[text()='Save']")
    MESSAGE =(By.XPATH,"//div[@class='ss-snackbar-body']")
    SHARE_INTEREST =(By.XPATH ,"//button[@class=' unshared']")
    MESSAGE_SHARE_INTEREST =  (By.XPATH,"//span[@class='apply-message typ-14Medium']")
    SHARE =(By.XPATH,"//button[@class='share-interest']")
    APPLIES=(By.XPATH, "//div[starts-with(text(),'Applies')] ")
    CHECK_BOX = (By.XPATH, "//i[@class='dspIB naukicon naukicon-ot-checkbox']")
    TEXT = (By.XPATH,"//span[@class='fright']")
    APPLY=(By.XPATH, "//button[starts-with(text(),'Apply')]")
    CROSS_ICON =(By.XPATH,"//div[@class='crossIcon chatBot chatBot-ic-cross']")


    def record_view_all(self):
        self.click(self.RECORD_HEADER)

    def sepc_view_all(self):
        self.click(self.SPE_HEADER)

    def nvite_view_all(self):
        self.click(self.NVITES)

    def user_history_view_all(self):
        self.click(self.METER)

    def top_compmay_view_all(self):
        self.click(self.TOP_COMPANY)

    def update_form(self):
        self.click(self.RECORD_HEADER)
        self.click(self.UPDATE_CITY)
        self.click(self.SAVE)
        return self.element_visible(self.MESSAGE)

    def share_interest(self):
        try:
            self.click(self.SPE_HEADER)
            share_interest_element = self.find_element(self.SHARE_INTEREST)
            share_interest_element.click()
            message = self.find_element(self.MESSAGE_SHARE_INTEREST)
            share_buttons = self.find_elements(self.SHARE)
            if share_buttons:
                for button in share_buttons:
                    if button.is_displayed():
                        button.click()
                logging.info("Successfully clicked all visible 'SHARE' buttons.")
            else:
                logging.warning("No visible 'SHARE' buttons found.")
        except Exception as e:
            self.capture_screenshot("share_interest")
            logging.error(f"Share interest error: {e}")
            raise  # Raise the exception after logging
        return message  # Return the message element

    def check_box(self):
        count = 0

        try:
            elements =self.find_elements(self.CHECK_BOX)
            if elements:
                for element in elements:
                    if element.is_displayed():
                        element.click()
                        count+=1
                        if count == 5:
                            break

            else:
                logging.error("check box not found")
        except Exception as e:
            self.capture_screenshot("share_interest")
            logging.error(f"Share interest error: {e}")
            raise  # Raise the exception after logging


    def applies(self):
        try:
            self.click(self.RECORD_HEADER)
            self.click(self.APPLIES)
            self.check_box()
            value = self.find_element(self.TEXT)
            message = value.text
            time.sleep(1)
            self.click(self.APPLY)
            self.click(self.CROSS_ICON)
        except Exception as e:
            self.capture_screenshot("job apply ")
            logging.error(f"Share interest error: {e}")
            raise  # Raise the exception after logging
        return message


