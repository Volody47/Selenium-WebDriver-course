
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://localhost/litecart/admin/"


class TestMainPage1():

    def test_admin_log_in(self, browser):
        browser.get(link)
        # --------------------------------------------Log in------------------------------------------------------------

        # Fill out Login fields
        username_input = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.NAME, "username")))
        username_input.send_keys("admin")
        password_input = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.NAME, "password")))
        password_input.send_keys("admin")
        # Push login button
        button_login = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.NAME, "login")))
        button_login.click()

        # Side bar component
    def test_find_side_bar_elements(self, browser):
        browser.get(link)

        side_bar = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#sidebar #app-")))
        i = 0
        for x in side_bar:
            x = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#sidebar #app-")))
            x[i].click()

            inside_items = browser.find_elements_by_css_selector(".docs a")
            z = 0
            for item in inside_items:
                item = WebDriverWait(browser, 5).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
                item[z].click()

                page_title = WebDriverWait(browser, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
                assert page_title != None
                z += 1

            i += 1
