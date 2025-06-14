import allure

from base.base_page import BasePage
from config.links import Links


class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    MY_INFO_LINK = ("xpath", "//span[text()='My Info']")

    @allure.step("Click 'My Info' link")
    def click_my_info_link(self):
        self.click_element(self.MY_INFO_LINK)
