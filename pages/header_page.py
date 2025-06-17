from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage

class HeaderPage(BasePage):
    JOBS=(By.XPATH,"//a/div[text()='Jobs']")
    COMPANIES=(By.XPATH,"//a/div[text()='Companies']")
    SERVICES=(By.XPATH,"//a/div[text()='Services']")



