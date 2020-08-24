import current as current
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

link = "http://localhost/litecart/admin/?app=countries&doc=countries"


class TestMainPage1():

    def test_switch_to_window(self, browser):
        wait = WebDriverWait(browser, 10)
        browser.get(link)
        # --------------------------------------------Log in------------------------------------------------------------

        # Fill out Login fields
        username_input = wait.until(
            EC.element_to_be_clickable((By.NAME, "username")))
        username_input.send_keys("admin" + Keys.TAB + "admin" + Keys.ENTER)

        # --------------------------------------------Find countries----------------------------------------------------
        countries = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".row a:not([title='Edit']")))

        for item in countries:
            if item.text == "Argentina":
                item.click()

                external_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//i[@class='fa fa-external-link']/..")))
                for i in external_links:
                    main_window = browser.current_window_handle
                    old_windows = browser.window_handles
                    i.click()

                    wait.until(EC.number_of_windows_to_be(2))

                    new_window = browser.window_handles[1]
                    browser.switch_to.window(new_window)
                    browser.close()
                    browser.switch_to.window(main_window)


                    # current = browser.window_handles[0]
                    # i.click()
                    #
                    # wait.until(EC.number_of_windows_to_be(2))
                    #
                    # new_window = [window for window in browser.window_handles if window != current][0]
                    # browser.switch_to.window(new_window)
                    # browser.close()
                    # browser.switch_to.window(current)
                break
