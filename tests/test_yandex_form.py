import pytest
import allure
from pages.yandex_form_page import YandexFormPage
from selenium.webdriver.common.by import By

@allure.suite("Yandex Search Tests")
class TestYandexForm:

    @allure.title("Проверка поиска Яндекс")
    @pytest.mark.parametrize("query", ["Selenium", "Python", "Pytest"])
    def test_yandex_search_functionality(self, browser, base_url, query):
        page = YandexFormPage(browser)
        page.open_page(base_url)
        first_result = page.perform_search(query)
        assert query.lower() in first_result.lower()

    @allure.title("Проверка отображения подсказок")
    def test_suggest_display(self, browser, base_url):
        page = YandexFormPage(browser)
        page.open_page(base_url)
        page.enter_text("Selenium")
        page.wait_for_suggest()
        assert len(browser.find_elements(*page.SUGGEST_LIST)) > 0

    @allure.title("Очистка поля поиска")
    def test_search_input_clear(self, browser, base_url):
        page = YandexFormPage(browser)
        page.open_page(base_url)
        page.enter_text("Python")
        browser.find_element(*page.SEARCH_INPUT).clear()
        assert browser.find_element(*page.SEARCH_INPUT).get_attribute("value") == ""
