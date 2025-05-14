from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_page import BasePage
from config.links import Links


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    LOGIN_BUTTON = ("xpath", "//button[@type='submit']")

    @allure.step("Enter login")
    def enter_login(self, login):
        username_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
        username_field.clear()
        assert username_field.get_attribute("value") == "", "The input field was not cleared"
        username_field.send_keys(login)
        assert username_field.get_attribute("value") == login, \
            f"Expected: {login}, Actual: {username_field.get_attribute('value')}"

    @allure.step("Enter password")
    def enter_password(self, password):
        password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)

    @allure.step("Click 'Login' button")
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    




