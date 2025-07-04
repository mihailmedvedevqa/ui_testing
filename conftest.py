import os

from faker import Faker
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def fake():
    """Provide a Faker instance for generating test data."""

    return Faker()


# def pytest_addoption(parser):
#     """Add custom command-line options for pytest."""
#
#     parser.addoption(
#         "--browser",
#         action="store",
#         default="chrome",
#         help="Browser to use for tests: chrome or firefox"
#     )


# @pytest.fixture(scope="function", autouse=True)
# def driver(request, browser="chrome"):
#     """Initializes WebDriver for tests."""
#
#     browser = request.config.getoption("--browser")
#     driver = None
#     if browser.lower() == "chrome":
#         options = webdriver.ChromeOptions()
#         prefs = {"download.default_directory": os.path.join(os.getcwd(), "downloads")}
#         options.add_experimental_option("prefs", prefs)
#         # For headless mode in CI/CD:
#         options.add_argument("--headless")  # Run without GUI
#         options.add_argument("--window-size=1920,1080")  # Fixed window size
#         options.add_argument("--no-sandbox")  # Required for Docker/CI
#         options.add_argument("--disable-shm-usage")  # Improve stability in CI
#         # options.add_argument("--start-maximized")
#         options.add_argument("--ignore-certificate-errors")
#         options.add_argument("--disable-extensions")
#         driver = webdriver.Chrome(options=options)
#     elif browser.lower() == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.set_preference("browser.download.folderList", 2)
#         options.set_preference("browser.download.dir", os.path.join(os.getcwd(), "downloads"))
#         options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
#         options.set_preference("browser.download.manager.showWhenStarting", False)
#         options.set_preference("pdfjs.disabled", True)
#         # For headless mode in CI/CD:
#         # options.headless = True  # Run without GUI
#         # driver.set_window_size(1920, 1080)  # Fixed window size
#         driver = webdriver.Firefox(options=options)
#         driver.maximize_window()
#         options.accept_insecure_certs = True
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#
#     request.cls.driver = driver
#     yield driver
#     driver.quit()

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    """Initializes WebDriver for tests."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-gpu")
    options.add_argument("--enable-logging")  # Включаем логирование
    options.add_argument("--v=1")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()