# tests/test_yandex_form.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # без GUI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    yield driver
    driver.quit()


def test_yandex_search_functionality(driver):
    driver.get("https://yandex.ru")
    assert "Яндекс" in driver.title

