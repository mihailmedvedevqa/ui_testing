from selenium import webdriver
import pytest
import os


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(os.getcwd(), "downloads")  # Универсальный путь для всех систем
    }
    options.add_experimental_option("prefs", prefs)
    # options.add_argument("--no-sandbox")  # Отключает песочницу которая изолирует процессы браузера
    # options.add_argument("--disable-shm-usage")  # Отключает использование общей памяти для хранения данных
    # options.add_argument("--headless")  # Для безголового режима
    # options.add_argument("--window-size=1920,1080")  # Открывает окно браузера в фиксированном размере
    options.add_argument("--start-maximized")  # Открывает окно браузера в максимальном размере
    options.add_argument("--ignore-certificate-errors")  # Игнорирует ошибки сертификатов
    options.add_argument("--disable-extensions")  # Отключает все расширения браузера
    driver = webdriver.Chrome(options=options)  # Инициализация WebDriver с указанными опциями
    request.cls.driver = driver  # Связывает драйвер с тестовым классом
    yield driver  # Возвращает драйвер в тест для работы
    driver.quit()  # Закрывает браузер после выполнения теста



