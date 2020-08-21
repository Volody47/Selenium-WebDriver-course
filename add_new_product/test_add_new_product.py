from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
from random import randint
import time


link = "http://localhost/litecart/admin/"


class TestMainPage1():

    def test_admin_log_in(self, browser):
        browser.get(link)
        # --------------------------------------------Log in------------------------------------------------------------

        # Fill out Login fields
        username_input = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.NAME, "username")))
        username_input.send_keys("admin" + Keys.TAB + "admin" + Keys.ENTER)
        # password_input = WebDriverWait(browser, 5).until(
        #     EC.element_to_be_clickable((By.NAME, "password")))
        # password_input.send_keys("admin")
        # # Push login button
        # button_login = WebDriverWait(browser, 5).until(
        #     EC.element_to_be_clickable((By.NAME, "login")))
        # button_login.click()

        # --------------------------------------------Add new product---------------------------------------------------

    def test_admin_add_product(self, browser):
        # test data
        x = randint(10, 100)
        product_name = "Black duck" + str(x)

        browser.get(link)

        catalog = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidebar li:nth-child(2) a")))
        catalog.click()
        add_new_product = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#content>div a:last-child")))
        add_new_product.click()

        time.sleep(0.5)

                                                   # Fill out form General
        # radiobutton Status
        status_radiobutton = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label [value='1']")))
        status_radiobutton.click()

        input_name = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='name[en]']"))).send_keys(product_name)
        input_code = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='code']"))).send_keys("12345")
        # checkbox Categories
        categories_checkbox = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td>input[value='1']")))
        categories_checkbox.click()
        # dropdown menu Default Category
        default_category = Select(browser.find_element_by_css_selector("select[name='default_category_id']"))
        default_category.select_by_visible_text("Root")
        # checkbox Product Groups
        product_groups_checkbox = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='1-3']")))
        product_groups_checkbox.click()
        # Quantity table
        quantity = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='quantity']"))).send_keys(Keys.CONTROL, "a" + Keys.DELETE)
        quantity = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='quantity']"))).send_keys("1")
        # dropdown menu Quantity Unit
        quantity_unit = Select(browser.find_element_by_css_selector("select[name='quantity_unit_id']"))
        quantity_unit.select_by_visible_text("pcs")
        # dropdown menu Delivery Status
        delivery_status = Select(browser.find_element_by_css_selector("select[name='delivery_status_id']"))
        delivery_status.select_by_value("1")
        # dropdown menu Sold Out Status
        sold_out_status = Select(browser.find_element_by_css_selector("select[name='sold_out_status_id']"))
        sold_out_status.select_by_index(2)

        # Upload Images
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'black_duck.jpg')
        choose_file = browser.find_element_by_name("new_images[]").send_keys(file_path)

        # Date
        date_valid_from = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='date_valid_from']"))).send_keys("01032014")
        date_valid_to = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='date_valid_to']"))).send_keys("12012015")

        # switch to information
        information = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".index li:nth-child(2)>a")))
        information.click()
        time.sleep(0.5)
                                               # Fill out form Information
        # dropdown menu Manufacturer
        manufacturer = Select(browser.find_element_by_css_selector("select[name='manufacturer_id']"))
        manufacturer.select_by_visible_text("ACME Corp.")
        # Keywords + (TAB) + Short Description + Description + Head Title + Meta Description
        keywords = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='keywords']"))).send_keys("test" + Keys.TAB + "Short Description" + Keys.TAB + "Description" +
                                                                                               Keys.TAB + "Head Title" + Keys.TAB + "Meta Description")

        # switch to Prices
        prices = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".index li:nth-child(4)>a")))
        prices.click()
        time.sleep(0.5)

                                        # Fill out form Prices
        # Purchase Price
        purchase_price = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='purchase_price']"))).clear()
        purchase_price = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='purchase_price']"))).send_keys("3")
        us_dollars = Select(browser.find_element_by_css_selector("select[name='purchase_price_currency_code']"))
        us_dollars.select_by_visible_text("US Dollars")

        # Tax Class
        tax = Select(browser.find_element_by_css_selector("select[name='tax_class_id']"))
        tax.select_by_visible_text("Standard")

        # Price
        price = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='prices[USD]']"))).send_keys("77")

        # Save button
        save_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='save']")))
        save_button.click()

        #Check new product added
        products = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".row a:not([title='Edit'])")))

        i = len(products) - 1
        assert products[i].text == product_name

