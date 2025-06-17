import time

import pytest
from pages.services_page import ServicesPage

@pytest.mark.usefixtures("logged_in_driver")
class TestServices:
    """before test excution this function automatically called """

    @pytest.fixture(autouse=True)
    def setup(self, logged_in_driver):
        """ Initialize ProfilePage once per test """
        self.services_page = ServicesPage(logged_in_driver)

    import pytest

    @pytest.mark.smoke
    def test_free_resume_resourse(self):
        letter = self.services_page.click_on_letter()
        assert letter == "https://resume.naukri.com/job-letter-format"

        url = self.services_page.click_on_resume_maker()
        assert url == "https://www.naukri.com/resume-maker?utmTerm=ResumePro_Gnb&utmContent=gnbServices"

        score = self.services_page.click_on_score()
        assert score == "https://resume.naukri.com/resume-quality-score?fftid=101003"

        sample = self.services_page.click_on_sample()
        assert sample == "https://resume.naukri.com/sample-resume-for-freshers?fftid=101004"

    @pytest.mark.smoke
    def test_resume_writing(self):
        writing =self.services_page.resume_writing()
        assert writing == "https://resume.naukri.com/resume-writing-for-freshers-entry-level?fftid=101001"

        visual=self.services_page.resume_visual()
        assert visual== "https://resume.naukri.com/visual-resume-writing-for-freshers-entry-level?fftid=101002"

        critique=self.services_page.resume_critique()
        assert critique == "https://resume.naukri.com/resume-critique?fftid=101006"

