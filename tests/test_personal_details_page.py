import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Personal details page")
class TestPersonalDetailsPage(BaseTest):
    @allure.step("Changing profile first name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_changing_profile_first_name(self, fake):
        new_name = fake.first_name()
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_details_page.is_opened()
        self.personal_details_page.change_first_name(new_name)
        self.personal_details_page.save_changes()
        self.personal_details_page.changes_are_saved(new_name)
        self.personal_details_page.take_screenshot(f"First name changed to {new_name}")