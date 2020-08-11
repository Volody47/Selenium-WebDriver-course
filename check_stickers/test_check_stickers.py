from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://localhost/litecart/en/"


class TestMainPage1():

    def test_main_page(self, browser):
        browser.get(link)

        product_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product a.link")))

        for sticker in product_items:
            sticker = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "sticker"))).text
            count_sticker = []
            count_sticker.append(sticker)

            assert len(count_sticker) == 1, "Should be just one sticker"



