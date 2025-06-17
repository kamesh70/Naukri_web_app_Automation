import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ServicesPage(BasePage):
    services_path= (By.XPATH,"//div[text()='Services']")
    resume_maker_path= (By.XPATH,"//li//div[text()='Resume maker']")
    resume_score_path= (By.XPATH,"//li//div[text()='Resume quality score']")
    resume_sample_path= (By.XPATH,"//li//div[text()='Resume samples']")
    resume_letter_path= (By.XPATH,"//li//div[text()='Job letter samples']")
    resume_text_path= (By.XPATH,"//li//div[text()='Text resume']")
    resume_visual_path= (By.XPATH,"//li//div[text()='Visual resume']")
    resume_critique_path= (By.XPATH,"//li//div[text()='Resume critique']")


    def services_move(self):
        self.move_element(self.services_path)

    def handle_new_tab_click(self,element_path):
        main_window = self.driver.current_window_handle
        self.click(element_path)
        # Wait for new window
        self.wait.until(EC.new_window_is_opened([main_window]))
        # Get all windows
        all_windows = self.driver.window_handles

        # Switch to new window
        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                break
        time.sleep(1)
        # Do something in the new window...
        print(self.driver.title)
        url = self.current_page_url
        time.sleep(2)

        # ✅ Switch back to main window
        self.driver.close()  # (optional) Close new window
        self.driver.switch_to.window(main_window)
        time.sleep(0.2)
        return url

    def click_on_resume_maker(self):
        self.services_move()
        url = self.handle_new_tab_click(self.resume_maker_path)
        return url

    def click_on_letter(self):
        self.services_move()
        url=self.handle_new_tab_click(self.resume_letter_path)
        return url

    def click_on_score(self):
        self.services_move()
        url=self.handle_new_tab_click(self.resume_score_path)
        return url

    def click_on_sample(self):
        self.services_move()
        url=self.handle_new_tab_click(self.resume_sample_path)
        return url

    def resume_writing(self):
        self.services_move()
        url=self.handle_new_tab_click(self.resume_text_path)
        return url

    def resume_visual(self):
        self.services_move()
        url=self.handle_new_tab_click(self.resume_visual_path)
        return url

    def resume_critique(self):
        self.services_move()
        url =self.handle_new_tab_click(self.resume_critique_path)
        return  url



