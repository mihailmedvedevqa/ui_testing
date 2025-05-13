import os
import pytest
from selenium import webdriver


# Fixture for Chrome WebDriver
@pytest.fixture(scope="function", autouse=True)
def driver(request):
    """Initializes and configures Chrome WebDriver for tests."""

    # Configure Chrome
    options = webdriver.ChromeOptions()
    # Set download directory
    prefs = {
        "download.default_directory": os.path.join(os.getcwd(), "downloads")  # Cross-platform path
    }
    options.add_experimental_option("prefs", prefs)  # Apply download settings
    # options.add_argument("--no-sandbox")  # For Docker or CI/CD
    # options.add_argument("--disable-shm-usage")  # For stability in CI/CD
    # options.add_argument("--headless")  # For headless mode
    # options.add_argument("--window-size=1920,1080")  # Fixed window size
    options.add_argument("--start-maximized")  # Maximize window
    options.add_argument("--ignore-certificate-errors")  # Ignore certificate errors
    options.add_argument("--disable-extensions")  # Disable extensions
    # Initialize WebDriver with options
    driver = webdriver.Chrome(options=options)
    # Bind driver to test class
    request.cls.driver = driver
    # Yield driver to test
    yield driver
    # Close browser
    driver.quit()

# Fixture for Firefox WebDriver
# @pytest.fixture(scope="function", autouse=True)
# def driver(request):
#     """Initializes and configures Firefox WebDriver for tests."""
#
#     # Configure Firefox
#     options = webdriver.FirefoxOptions()
#     # Set custom download directory
#     options.set_preference("browser.download.folderList", 2)
#     # Cross-platform download path
#     options.set_preference("browser.download.dir", os.path.join(os.getcwd(), "downloads"))
#     # Disable save dialog for binary files
#     options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
#     # Hide download manager on start
#     options.set_preference("browser.download.manager.showWhenStarting", False)
#     # Disable built-in PDF viewer
#     options.set_preference("pdfjs.disabled", True)
#     # options.headless = True  # For headless mode
#     # Initialize WebDriver with options
#     driver = webdriver.Firefox(options=options)
#     # Maximize window
#     driver.maximize_window()
#     # Ignore certificate errors
#     options.accept_insecure_certs = True
#     # Bind driver to test class
#     request.cls.driver = driver
#     # Yield driver to test
#     yield driver
#     # Close browser
#     driver.quit()
