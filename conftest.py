import os
import pytest
from selenium import webdriver


# Chrome
@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()  # Initialize ChromeOptions to configure the browser
    prefs = {
        "download.default_directory": os.path.join(os.getcwd(), "downloads")  # Universal path for all systems
    }
    options.add_experimental_option("prefs", prefs)  # Apply preferences for browser behavior
    # options.add_argument("--no-sandbox")  # Disables the sandbox that isolates browser processes
    # options.add_argument("--disable-shm-usage")  # Disables shared memory usage for storing data
    # options.add_argument("--headless")  # For headless mode
    # options.add_argument("--window-size=1920,1080")  # Opens the browser window in a fixed size
    options.add_argument("--start-maximized")  # Opens the browser window maximized
    options.add_argument("--ignore-certificate-errors")  # Ignores certificate errors
    options.add_argument("--disable-extensions")  # Disables all browser extensions
    driver = webdriver.Chrome(options=options)  # Initialize WebDriver with specified options
    request.cls.driver = driver  # Binds the driver to the test class
    yield driver  # Returns the driver to the test for operation
    driver.quit()  # Closes the browser after test execution

# # Firefox
# @pytest.fixture(scope="function", autouse=True)
# def driver(request):
#     options = webdriver.FirefoxOptions()  # Initialize FirefoxOptions to configure the browser
#     # Use a custom folder for downloads
#     options.set_preference("browser.download.folderList", 2)
#     # Universal path for all systems
#     options.set_preference("browser.download.dir", os.path.join(os.getcwd(), "downloads"))
#     # Disable the save dialog
#     options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
#     # Disable the download manager window
#     options.set_preference("browser.download.manager.showWhenStarting", False)
#     options.set_preference("pdfjs.disabled", True)  # Disable the built-in PDF viewer
#     # options.headless = True # For headless mode
#     driver = webdriver.Firefox(options=options)  # Initialize WebDriver with settings
#     driver.maximize_window()  # Opens the browser window maximized
#     request.cls.driver = driver  # Binds the driver to the test class
#     yield driver  # Returns the driver to the test for operation
#     driver.quit()  # Closes the browser after test execution
