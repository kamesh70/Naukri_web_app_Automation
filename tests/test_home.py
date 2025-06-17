import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("logged_in_driver")
class TestHome:

    @pytest.fixture(autouse=True)
    def Setup(self,logged_in_driver):
        self.home_page = HomePage(logged_in_driver)

    # @pytest.mark.smoke
    # def test_hello(self):
    #     print("hello")

    def test_Recommended_view_all(self):
        self.home_page.record_view_all()
        # print(self.home_page.current_page_url)
        assert self.home_page.current_page_url == "https://www.naukri.com/mnjuser/recommendedjobs",f"assert of {self.home_page.current_page_url}"

    def test_se_view_all(self):
        self.home_page.sepc_view_all()
        # print(self.home_page.current_page_url)
        assert self.home_page.current_page_url == "https://www.naukri.com/mnjuser/recommended-earjobs", f"assert of {self.home_page.current_page_url}"

    def test_Nvites_view_all(self):
        self.home_page.nvite_view_all()
        # print(self.home_page.current_page_url)
        assert self.home_page.current_page_url == "https://www.naukri.com/mnjuser/inbox", f"assert of {self.home_page.current_page_url}"

    def test_top_company_view_all(self):
        self.home_page.top_compmay_view_all()
        assert self.home_page.current_page_url == "https://www.naukri.com/companies-hiring-in-india?src=mnjCompanies_homepage_srch&title=Top+companies&subtitle=Hiring+for+Quality+Assurance+and+Testing&searchType=companySearch&qcallRoleCategory=1027&qcallDept=5&qccustomTag=195", f"assert of {self.home_page.current_page_url}"

    def test_user_history_view_all(self):
        self.home_page.user_history_view_all()
        assert self.home_page.current_page_url == "https://www.naukri.com/myapply/historypage", f"assert of {self.home_page.current_page_url}"

    def test_update_form(self):
        element = self.home_page.update_form()
        element.click()
        assert element.text == "Your preferences have been saved", f"assert of {self.home_page.current_page_url}"

    def test_share_interest(self):
        message = self.home_page.share_interest()
        assert message.text == "Interest shared successfully!"

    #  Applay jobs
    def test_applies_jobs(self):
        message = self.home_page.applies()
        print(message)
