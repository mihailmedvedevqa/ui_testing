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
        self.fill_input(self.USERNAME_FIELD, login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.fill_input(self.PASSWORD_FIELD, password)

    @allure.step("Click 'Login' button")
    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)
