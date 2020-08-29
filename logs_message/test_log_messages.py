from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys





import time


link = "http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1"


class TestMainPage1():

    def test_admin_log_in(self, browser):
        wait = WebDriverWait(browser, 10)
        browser.get(link)
        # --------------------------------------------Log in------------------------------------------------------------

        # Fill out Login fields
        username_input = wait.until(
            EC.element_to_be_clickable((By.NAME, "username")))
        username_input.send_keys("admin" + Keys.TAB + "admin" + Keys.ENTER)

        # --------------------------------------------task 17-------------------------------------------------------

    def test_logs_messages(self, browser):
        wait = WebDriverWait(browser, 10)
        browser.get(link)

        subcategory = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class = 'fa fa-folder']/../a")))
        subcategory.click()

        product_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".dataTable td>a:not([title='Edit'])")))
        i = 0
        while i != len(product_items):
            item = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".dataTable td>a:not([title='Edit'])")))[i]
            item.click()

            # for l in browser.log_types:
            #     print(l)
            for l in browser.get_log("browser"):
                print(l)
            # for l in browser.get_log("performance"):
            #     print(l)

            browser.get(link)
            subcategory = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class = 'fa fa-folder']/../a")))
            subcategory.click()

            i += 1
