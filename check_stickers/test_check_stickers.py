from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://localhost/litecart/en/"


class TestMainPage1():

    def test_main_page(self, browser):
        browser.get(link)

        product_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product a.link")))
        i = 0
        for sticker in product_items:
            sticker = product_items[i].find_elements_by_css_selector(".sticker")
            # count_item = []
            # count_item.append(i)
            assert len(sticker) == 1, "Should be just one sticker for each item"
            i += 1





