
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

        # ------------------------------------------Appearence----------------------------------------------------------

    def test_appearence(self, browser):
        browser.get(link)
        appearence = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(1) a")))
        appearence.click()

        inside_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
        # TODO: my need sleep
        i = 0
        x = ["#doc-template a", "#doc-logotype a"]
        while i < len(inside_items):
            inside_menu = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
            inside_menu.click()

            page_title = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
            assert page_title != None
            i += 1
        # ------------------------------------------Catalog----------------------------------------------------------

    def test_catalog(self, browser):
        browser.get(link)
        catalog = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(2) a")))
        catalog.click()

        inside_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
        # TODO: my need sleep
        i = 0
        x = ["#doc-catalog a", "#doc-product_groups a", "#doc-option_groups a", "#doc-manufacturers a",
             "#doc-suppliers a", "#doc-delivery_statuses a", "#doc-sold_out_statuses a", "#doc-quantity_units a",
             "#doc-csv a"]
        while i < len(inside_items):
            inside_menu = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
            inside_menu.click()

            page_title = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
            assert page_title != None
            i += 1

        # ------------------------------------------Countries----------------------------------------------------------

    def test_countries(self, browser):
        browser.get(link)
        countries = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(3) a")))
        countries.click()
        page_title = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
        assert page_title != None

        # ------------------------------------------Currencies----------------------------------------------------------

    def test_currencies(self, browser):
        browser.get(link)
        currencies = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(4) a")))
        currencies.click()
        page_title = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
        assert page_title != None

        # ------------------------------------------Customers----------------------------------------------------------

    def test_customers(self, browser):
        browser.get(link)
        customers = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(5) a")))
        customers.click()

        inside_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
        # TODO: my need sleep
        i = 0
        x = ["#doc-customers a", "#doc-csv a", "#doc-newsletter a"]
        while i < len(inside_items):
            inside_menu = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
            inside_menu.click()

            page_title = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
            assert page_title != None
            i += 1

        # ------------------------------------------Geo Zones----------------------------------------------------------

    def test_geo_zones(self, browser):
        browser.get(link)
        geo_zones = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(6) a")))
        geo_zones.click()
        page_title = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
        assert page_title != None

        # ------------------------------------------Languages----------------------------------------------------------

    def test_languages(self, browser):
        browser.get(link)
        languages = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(7) a")))
        languages.click()

        inside_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
        # TODO: my need sleep
        i = 0
        x = ["#doc-languages a", "#doc-storage_encoding a"]
        while i < len(inside_items):
            inside_menu = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
            inside_menu.click()

            page_title = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
            assert page_title != None
            i += 1

        # ------------------------------------------Modules----------------------------------------------------------

    def test_modules(self, browser):
        browser.get(link)
        modules = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(8) a")))
        modules.click()

        inside_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
        # TODO: my need sleep
        i = 0
        x = ["#doc-jobs a", "#doc-customer a", "#doc-shipping a", "#doc-payment a",
             "#doc-order_total a", "#doc-order_success a", "#doc-order_action a"]
        while i < len(inside_items):
            inside_menu = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
            inside_menu.click()

            page_title = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
            assert page_title != None
            i += 1

        # ------------------------------------------Orders----------------------------------------------------------

    def test_orders(self, browser):
        browser.get(link)
        orders = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(9) a")))
        orders.click()

        inside_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
        # TODO: my need sleep
        i = 0
        x = ["#doc-orders a", "#doc-order_statuses a"]
        while i < len(inside_items):
            inside_menu = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
            inside_menu.click()

            page_title = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
            assert page_title != None
            i += 1

        # ------------------------------------------Pages----------------------------------------------------------

    def test_pages(self, browser):
        browser.get(link)
        pages = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(10) a")))
        pages.click()
        page_title = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
        assert page_title != None

    # ------------------------------------------Reports----------------------------------------------------------

    def test_reports(self, browser):
        browser.get(link)
        reports = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(11) a")))
        reports.click()

        inside_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
        # TODO: my need sleep
        i = 0
        x = ["#doc-monthly_sales a", "#doc-most_sold_products a", "#doc-most_shopping_customers a"]
        while i < len(inside_items):
            inside_menu = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
            inside_menu.click()

            page_title = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
            assert page_title != None
            i += 1

        # ------------------------------------------Settings----------------------------------------------------------

    def test_settings(self, browser):
        browser.get(link)
        settings = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(12) a")))
        settings.click()

        inside_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
        # TODO: my need sleep
        i = 0
        x = ["#doc-store_info a", "#doc-defaults a", "#doc-general a",
             "#doc-listings a", "#doc-images a", "#doc-checkout a",
             "#doc-advanced a", "#doc-security a"]
        while i < len(inside_items):
            inside_menu = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
            inside_menu.click()

            page_title = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
            assert page_title != None
            i += 1

        # ------------------------------------------Slides----------------------------------------------------------

    def test_slides(self, browser):
        browser.get(link)
        slides = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(13) a")))
        slides.click()
        page_title = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
        assert page_title != None

        # ------------------------------------------Tax-------------------------------------------------------------

    def test_tax(self, browser):
        browser.get(link)
        tax = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(14) a")))
        tax.click()

        inside_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
        # TODO: my need sleep
        i = 0
        x = ["#doc-tax_classes a", "#doc-tax_rates a"]
        while i < len(inside_items):
            inside_menu = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
            inside_menu.click()

            page_title = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
            assert page_title != None
            i += 1

        # ------------------------------------------Translations--------------------------------------------------------

    def test_translations(self, browser):
        browser.get(link)
        translations = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(15) a")))
        translations.click()

        inside_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
        # TODO: my need sleep
        i = 0
        x = ["#doc-search a", "#doc-scan a", "#doc-csv a"]
        while i < len(inside_items):
            inside_menu = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
            inside_menu.click()

            page_title = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
            assert page_title != None
            i += 1

        # ------------------------------------------Users--------------------------------------------------------

    def test_users(self, browser):
        browser.get(link)
        users = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(16) a")))
        users.click()
        page_title = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
        assert page_title != None

        # ------------------------------------------vQmods--------------------------------------------------------

    def test_vQmods(self, browser):
        browser.get(link)
        vQmods = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(17) a")))
        vQmods.click()

        inside_items = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docs a")))
        # TODO: my need sleep
        i = 0
        x = ["#doc-vqmods a"]
        while i < len(inside_items):
            inside_menu = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
            inside_menu.click()

            page_title = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))).text
            assert page_title != None
            i += 1

# #Left menu
#
#     #Side bar component
#     def test_find_side_bar_elements(self, browser):
#         browser.get(link)
#         side_bar = WebDriverWait(browser, 5).until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#sidebar li")))
#
#         time.sleep(0.5)
#         i = 0
#         x = ["#sidebar li:nth-child(1) a", "#sidebar li:nth-child(2) a", "#sidebar li:nth-child(3) a", "#sidebar li:nth-child(4) a",
#              "#sidebar li:nth-child(5) a", "#sidebar li:nth-child(6) a", "#sidebar li:nth-child(7) a", "#sidebar li:nth-child(8) a",
#              "#sidebar li:nth-child(9) a", "#sidebar li:nth-child(10) a", "#sidebar li:nth-child(11) a", "#sidebar li:nth-child(12) a",
#              "#sidebar li:nth-child(13) a", "#sidebar li:nth-child(14) a", "#sidebar li:nth-child(15) a", "#sidebar li:nth-child(16) a",
#              "#sidebar li:nth-child(17) a"]
#         while i < len(side_bar):
#             element_menu = WebDriverWait(browser, 5).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, f"{x[i]}")))
#             element_menu.click()
#             i += 1
