from selenium import webdriver
import pytest
import os


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(os.getcwd(), "downloads")  # Universal path for all systems
    }
    options.add_experimental_option("prefs", prefs)
    # options.add_argument("--no-sandbox")  # Disables the sandbox that isolates browser processes
    # options.add_argument("--disable-shm-usage")  # Disables the use of shared memory for storing data
    # options.add_argument("--headless")  # Enables headless mode
    # options.add_argument("--window-size=1920,1080")  # Opens the browser window with a fixed size
    options.add_argument("--start-maximized")  # Opens the browser window in maximized mode
    options.add_argument("--ignore-certificate-errors")  # Ignores certificate errors
    options.add_argument("--disable-extensions")  # Disables all browser extensions
    driver = webdriver.Chrome(options=options)  # Initializes WebDriver with the specified options
    request.cls.driver = driver  # Associates the driver with the test class
    yield driver  # Returns the driver to the test for execution
    driver.quit()  # Closes the browser after the test is complete
