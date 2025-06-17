import logging
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException


class SearchPage(BasePage):
    SEARCH = (By.XPATH, "//span[contains(text(),'Search jobs here')]")
    VERIFY_EXPAND = (By.XPATH, "//div[@class='nI-gNb-sb__main nI-gNb-sb__main--expand']")
    YEAR_CLICK = (By.XPATH, "//div[@class='dropdownMainContainer']")
    DESIGNATION = (By.XPATH, "//input[@placeholder='Enter keyword / designation / companies']")
    LOCATION = (By.XPATH, "//input[@placeholder='Enter location']")
    SEARCH_TEXT = (By.XPATH, "//span[text()='Search']")
    ERROR_MSG = (By.XPATH, "//div[@class='nI-gNb-sb__error-msg']")
    SLIDER= (By.XPATH,"//div[@class='inside']/span")
    DEPARTMENT_VIEW_ALL =(By.XPATH,"//a[@id='functionAreaIdGid']")
    SELECT_QA_TESTING =(By.XPATH, "//label[@for='chk-Quality Assurance and Testing-glbl_qcrc-']")
    SELECT_QA = (By.XPATH, "//label[starts-with(normalize-space(@for), 'chk-Engineering - Software & QA-functionAreaIdGid')]")
    AA=(By.XPATH,"//div[@class='styles_single-select-wrapper__WkB22']//li[@title='Last 1 day']")
    ROLE_VIEW_ALL = (By.XPATH,"//a[@id='glbl_qcrc']")
    APPLY = (By.XPATH,"//div[text()='Apply']")

    @staticmethod
    def SELECT_YEAR(year):
        """
        Return the XPath locator for selecting a specific experience year.
        :param year: The experience year to select.
        :return: Locator tuple with dynamic XPath.
        """
        return (By.XPATH, f"//li[@title='{year}']")  # Example: "1 year"  3 years

    def check_search_bar_expand(self):
        self.click(self.SEARCH)
        self.find_element(self.VERIFY_EXPAND)

    def year(self, value):
        self.click(self.YEAR_CLICK)
        time.sleep(2)
        self.click(self.SELECT_YEAR(value))

    def skills(self, skill):
        self.enter_text(self.DESIGNATION, skill)

    def location(self, city):
        self.enter_text(self.LOCATION, city)

    def search_icon_click(self):
        self.click(self.SEARCH_TEXT)

    def error_message(self):
        ele = self.find_element(self.ERROR_MSG)
        return ele.text.strip()

    def slider(self):
        return self.find_element(self.SLIDER)


    def search(self, skill,experience,city):
        self.check_search_bar_expand()
        self.skills(skill)
        self.year(experience)
        self.location(city)
        self.search_icon_click()


    def department_filter(self):
        try:
            self.click(self.DEPARTMENT_VIEW_ALL)
            ele = self.element_visible(self.SELECT_QA)
            ele.click()
            self.click(self.APPLY)
        except Exception as e:
            logging.error(f"filter option error : {e}")



    def role_filter(self):
        max_attempts = 3  # Retry up to 3 times
        for attempt in range(max_attempts):
            try:
                # Re-fetch elements inside the loop to avoid stale reference
                element = self.element_visible(self.SELECT_QA_TESTING)
                data = self.element_visible(self.SELECT_QA)

                if element:
                    element.click()
                    logging.info(f"Function Name :: role_filter  Clicked on SELECT_QA_TESTING {self.SELECT_QA_TESTING}")
                else:
                    logging.error("SELECT_QA_TESTING element not found")
                    pytest.fail("SELECT_QA_TESTING not found")

                if data:
                    data.click()
                    logging.info(f"Clicked on SELECT_QA {self.SELECT_QA}")
                else:
                    logging.error("SELECT_QA element not found")
                    pytest.fail("SELECT_QA not found")

                # Verify checkbox icon inside SELECT_QA_TESTING
                try:
                    icon = element.find_element(By.XPATH, ".//i[@class='ni-icon-checked']")
                    if icon.is_displayed():
                        logging.info("Checkbox icon found inside SELECT_QA_TESTING")
                    return  # Exit loop if successful
                except NoSuchElementException:
                    logging.warning("Checkbox icon not found inside SELECT_QA_TESTING")

            except StaleElementReferenceException:
                logging.warning(f"Attempt {attempt + 1}: Stale element reference, retrying...")
                time.sleep(2)

            except Exception as e:
                logging.error(f"Role_filter option error: {e}")
                pytest.fail("test_serch_filter")

        logging.error("role_filter failed after max attempts")
        pytest.fail("role_filter failed after retries")

    def record(self):
        ele=self.element_visible(self.AA)
        ele.click()