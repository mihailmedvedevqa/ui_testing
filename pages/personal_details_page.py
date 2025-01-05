from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_page import BasePage
from config.links import Links


class PersonalDetailsPage(BasePage):

    PAGE_URL = Links.PERSONAL_DETAILS_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON_1 = ("xpath", "(//button[@type='submit'])[1]")
    LOADING_SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_first_name(self, new_name):
        with allure.step(f"Change name to '{new_name}'"):
            first_name_field = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
            self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(Keys.CONTROL + "A")
            self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON_1)).click()

    @allure.step("Changes are saved")
    def changes_are_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.LOADING_SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))

