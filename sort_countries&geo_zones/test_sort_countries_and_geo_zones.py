import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://localhost/litecart/admin/?app=countries&doc=countries"


class TestMainPage1():

    def test_alphabet_countries(self, browser):
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
        # --------------------------------------------task 9.1(a)---------------------------------------------------------

        countries = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".row a:not([title='Edit'])")))

        name_countries = []
        for item in countries:
            text_item = item.text
            name_countries.append(text_item)

        sort_countries = sorted(name_countries)
        assert name_countries == sort_countries


         # --------------------------------------------task 9.1(b)--------------------------------------------------------

    def test_different_zones(self, browser):
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

        different_zones = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".row td:nth-child(6)")))
        i = 0
        list_zones = []
        for zones in different_zones:
            text_zones = zones.text
            if text_zones != "0":
                list_zones.append(i)
            i += 1

        for zone in list_zones:
            x = WebDriverWait(browser, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".row a:not([title='Edit'])")))
            x[zone].click()

            countries = WebDriverWait(browser, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#table-zones td:nth-child(3)>input:not([type='text'])")))
            name_countries = []
            for item in countries:
                text_item = item.get_attribute("value")
                name_countries.append(text_item)

            sort_countries = sorted(name_countries)
            assert name_countries == sort_countries

            time.sleep(0.5)

            browser.get(link)
            # back_to_countries = WebDriverWait(browser, 5).until(
            #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(3)>a")))
            # back_to_countries.click()

    # --------------------------------------------task 9.2--------------------------------------------------------
    def test_geo_zones(self, browser):
        link_2 = "http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones"
        browser.get(link_2)

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

        find_countries = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".row a:not([title='Edit'])")))
        i = 0
        countries = []
        for element in find_countries:
            countries.append(i)
            i += 1

        for item in countries:
            x = WebDriverWait(browser, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".row a:not([title='Edit'])")))
            time.sleep(2)
            x[item].click()

            inside_countries = WebDriverWait(browser, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#table-zones td:nth-child(3)>select option[selected]")))

            name_countries = []
            for item in inside_countries:
                # selected_item = item.get_attribute("selected")
                # if selected_item != None:
                    text_item = item.text
                    name_countries.append(text_item)

            sort_countries = sorted(name_countries)
            assert name_countries == sort_countries

            time.sleep(0.5)

            browser.get(link_2)

