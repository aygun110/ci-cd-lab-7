from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YandexFormPage:

    SEARCH_INPUT = (By.ID, "text")
    SUGGEST_LIST = (By.CSS_SELECTOR, ".mini-suggest__popup-content")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".serp-item h2 a")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def enter_text(self, text):
        el = self.driver.find_element(*self.SEARCH_INPUT)
        el.clear()
        el.send_keys(text)

    def wait_for_suggest(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.SUGGEST_LIST)
        )

    def click_search(self):
        self.driver.find_element(*self.SEARCH_INPUT).submit()

    def get_first_result(self):
        elems = self.driver.find_elements(*self.SEARCH_RESULTS)
        if not elems:
            return ""
        return elems[0].text

    def perform_search(self, text):
        self.enter_text(text)
        self.wait_for_suggest()
        self.click_search()
        return self.get_first_result()
