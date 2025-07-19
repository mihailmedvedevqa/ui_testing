import os

from faker import Faker
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def fake():
    """Provide a Faker instance for generating test data."""

    return Faker()


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    """Initializes WebDriver for tests."""
    options = Options()
    # Core CI/CD settings
    options.add_argument("--headless")  # Run without GUI
    options.add_argument("--window-size=1920,1080")  # Fixed window size
    options.add_argument("--no-sandbox")  # Disable sandbox
    options.add_argument("--disable-dev-shm-usage")  # Fixes memory issues in Docker
    # Performance optimization
    options.add_argument("--disable-extensions")  # Disable extensions
    options.add_argument("--disable-gpu")  # Disable GPU in headless mode
    options.add_argument("--disable-infobars")  # Disable info bars
    # Logging
    # options.add_argument("--enable-logging")  # Enable logging
    # options.add_argument("--v=1")  # Log verbosity level
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


# @pytest.fixture(scope="function", autouse=True)
# def driver(request):
#     """Initializes Firefox WebDriver for tests."""
#     options = webdriver.FirefoxOptions()
#     # Download settings
#     options.set_preference("browser.download.folderList", 2)  # Custom download directory
#     options.set_preference("browser.download.dir", os.path.join(os.getcwd(), "downloads"))  # Download path
#     options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")  # Auto-download files
#     options.set_preference("browser.download.manager.showWhenStarting", False)  # Hide download manager
#     options.set_preference("pdfjs.disabled", True)  # Disable PDF viewer
#     # Core CI/CD settings (uncomment for headless mode)
#     # options.headless = True  # Run without GUI
#     # driver.set_window_size(1920, 1080)  # Fixed window size
#     # Security settings
#     options.accept_insecure_certs = True  # Accept self-signed certificates
#     driver = webdriver.Firefox(options=options)
#     driver.maximize_window()  # Maximize window for consistent rendering
#     request.cls.driver = driver
#     yield driver
#     driver.quit()