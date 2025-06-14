import allure
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
from config.links import Links


class PersonalDetailsPage(BasePage):

    PAGE_URL = Links.PERSONAL_DETAILS_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON_1 = ("xpath", "(//button[@type='submit'])[1]")
    LOADING_SPINNER = ("xpath", "(//div[@class='oxd-loading-spinner-container'])[1]")

    def change_first_name(self, new_name):
        with allure.step(f"Change first name to '{new_name}'"):
            self.wait.until(EC.invisibility_of_element_located(self.LOADING_SPINNER))
            self.fill_input(self.FIRST_NAME_FIELD, new_name)
            return new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.click_element(self.SAVE_BUTTON_1)

    def changes_are_saved(self, expected_name):
        with allure.step(f"Verify changes are saved with name '{expected_name}'"):
            self.wait.until(EC.invisibility_of_element_located(self.LOADING_SPINNER))
            assert self.is_element_visible(self.FIRST_NAME_FIELD), "First name field is not visible"
            self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, expected_name))
