import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout, poll_frequency=1)

    def open(self):
        """Open the page specified by PAGE_URL."""

        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        """Verify that the page with PAGE_URL is opened."""

        with allure.step(f"Verify that {self.PAGE_URL} page is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def find_element(self, locator, timeout=None):
        """Find a visible element by locator with optional timeout."""

        with allure.step(f"Find element with locator {locator}"):
            wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=1)
            return wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator, timeout=None):
        """Find all visible elements by locator with optional timeout."""

        with allure.step(f"Find elements with locator {locator}"):
            wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=1)
            return wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        """Click an element when it becomes clickable."""

        with allure.step(f"Click element with locator {locator}"):
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill_input(self, locator, value):
        """Clear and fill an input field with the specified value."""

        with allure.step(f"Fill input {locator} with value '{value}'"):
            element = self.find_element(locator)
            element.clear()
            if element.get_attribute("value") not in ["", None]:
                with allure.step("Clear field using Ctrl+A and Backspace"):
                    element.send_keys(Keys.CONTROL + "A")
                    element.send_keys(Keys.BACKSPACE)
                    assert element.get_attribute("value") in ["", None], "The input field was not cleared"
            element.send_keys(value)
            assert element.get_attribute("value") == value, f"Expected '{value}', got '{element.get_attribute('value')}'"

    def get_element_text(self, locator):
        """Get text from a visible element."""

        with allure.step(f"Get text from element with locator {locator}"):
            return self.find_element(locator).text

    def take_screenshot(self, screenshot_name):
        """Take a screenshot and attach it to Allure report."""

        with allure.step(f"Take screenshot: {screenshot_name}"):
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=screenshot_name,
                attachment_type=AttachmentType.PNG
            )

    def is_element_visible(self, locator, timeout=None):
        """Check if an element is visible."""

        with allure.step(f"Check if element {locator} is visible"):
            try:
                self.find_element(locator, timeout)
                return True
            except:
                return False

    def is_element_not_visible(self, locator, timeout=None):
        """Check if an element is not visible."""

        with allure.step(f"Check if element {locator} is not visible"):
            wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=1)
            try:
                wait.until(EC.invisibility_of_element_located(locator))
                return True
            except:
                return False

    def is_element_present(self, locator, timeout=None):
        """Check if an element is present in the DOM."""

        with allure.step(f"Check if element {locator} is present in DOM"):
            try:
                wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=1)
                wait.until(EC.presence_of_element_located(locator))
                return True
            except:
                return False
