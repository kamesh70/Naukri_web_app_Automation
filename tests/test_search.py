import time
import pytest
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.search_page  import SearchPage

def test_search_error_message(logged_in_driver):
    """Test search functionality after logging in."""
    logging.info("Starting test: test_search_error_message")

    search_page = SearchPage(logged_in_driver)
    search_page.check_search_bar_expand()
    search_page.search_icon_click()
    actual_error_msg = search_page.error_message()
    expected_error_msg = "Please enter keywords to search relevant jobs"

    # Assert that the expected and actual messages match
    assert actual_error_msg == expected_error_msg, f"Expected '{expected_error_msg}', but got '{actual_error_msg}'"
    if actual_error_msg != expected_error_msg:
        logged_in_driver.save_screenshot("screenshot.png")
    logging.info("Search test passed successfully!")

@pytest.mark.parametrize("experience", [f"{i} years" for i in range(2, 4)])  # Testing from 1 to 30 years
def test_search_function(logged_in_driver, experience):
    time.sleep(0.2)
    logging.info(f"Starting test: test_search_function with experience: {experience}")
    search_page = SearchPage(logged_in_driver)
    search_page.search(experience=experience, skill="API Testing", city="Mumbai")
    # Extract numeric experience from "1 year", "2 years"
    experience_numeric = experience.split()[0]  # Takes only the number
    # Construct expected URL dynamically
    expected_url = f"https://www.naukri.com/api-testing-jobs-in-mumbai?k=api%20testing&l=mumbai&experience={experience_numeric}&nignbevent_src=jobsearchDeskGNB"
    # Assert that the current URL contains the expected URL pattern
    assert expected_url in logged_in_driver.current_url, f"Expected '{expected_url}' in '{logged_in_driver.current_url}'"


@pytest.mark.parametrize("skill", ['SDET', 'Manual Testing', 'Appium', 'Selenium', 'Python'])
def test_search_with_skill(logged_in_driver, skill):
    logging.info(f"Starting test: test_search_with_skill with skill: {skill}")

    search_page = SearchPage(logged_in_driver)
    search_page.check_search_bar_expand()
    search_page.skills(skill)
    search_page.location("Mumbai,pune,bangalore")
    search_page.search_icon_click()

    # Assert that the search results page URL contains the expected skill keyword
    expected_keyword = skill.lower().replace(" ", "%20")  # URL encoding for spaces
    assert expected_keyword in logged_in_driver.current_url.lower(), \
        f"Expected skill '{expected_keyword}' in URL, but got {logged_in_driver.current_url}"

def test_serch_filter(logged_in_driver):
    logging.info(f"Starting test: test_serch_filter:")
    search_page = SearchPage(logged_in_driver)
    try:
        search_page.search(experience="3 years", skill="SDET", city="Mumbai")
        search_page.role_filter()
        # search_page.record()
    except Exception as e:
        search_page.capture_screenshot("test_serch_filter")  # Capture screenshot on failure
        logging.error("test_serch_filter")
        pytest.fail("test_serch_filter")


def test_search_year_slider(logged_in_driver):
    logging.info(f"test_search_year_slider ")
    search_page = SearchPage(logged_in_driver)
    search_page.check_search_bar_expand()
    search_page.skills("SDET")
    search_page.location("Mumbai,pune,bangalore")
    search_page.search_icon_click()
    ele=search_page.slider()
    print("**********************",ele.text)
    assert "Any" in ele.text
    action = ActionChains(logged_in_driver)
    action.click_and_hold(ele).move_by_offset(-188, 0).release().perform()
    time.sleep(1)
    ele = search_page.slider()
    print("**********************", ele.text)








