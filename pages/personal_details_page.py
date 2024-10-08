from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class PersonalDetailsPage(BasePage):

    PAGE_URL = Links.PERSONAL_DETAILS_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    # MIDDLE_NAME_FIELD = ("xpath", "//input[@name='middleName']")
    SAVE_BUTTON_1 = ("xpath", "(//button[@type='submit'])[1]")

    def change_name(self, new_name):
        first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
        first_name_field.clear()
        assert first_name_field.get_attribute("value") == "", "There is a text"
        first_name_field.send_keys(new_name)
        self.name = new_name

    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON_1)).click()

    def changes_are_saved(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))

