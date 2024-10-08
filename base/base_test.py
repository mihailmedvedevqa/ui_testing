from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_details_page import PersonalDetailsPage


class BaseTest:

    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_details_page: PersonalDetailsPage

    # def setup(self, driver):
