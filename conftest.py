import os
import pytest
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def driver(request, browser="chrome"):
    """Initializes WebDriver for tests."""

    driver = None
    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": os.path.join(os.getcwd(), "downloads")}
        options.add_experimental_option("prefs", prefs)
        # options.add_argument("--no-sandbox")  # For Docker or CI/CD
        # options.add_argument("--disable-shm-usage")  # For stability in CI/CD
        # options.add_argument("--headless")  # For headless mode
        # options.add_argument("--window-size=1920,1080")  # Fixed window size
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", os.path.join(os.getcwd(), "downloads"))
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("pdfjs.disabled", True)
        # options.headless = True  # For headless mode
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        options.accept_insecure_certs = True
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    request.cls.driver = driver
    yield driver
    driver.quit()
