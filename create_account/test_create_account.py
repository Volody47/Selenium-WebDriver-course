from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from random import randint
import time



link = "http://localhost/litecart/en/"

class TestMainPage1():
    def test_new_account_registration(self, browser):
        #test data
        x = randint(10, 100)
        password = "12345test"

        browser.get(link)
        # ---------------------------------------------open create Account form-----------------------------------------
        new_customers_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='login_form'] a")))
        new_customers_button.click()

        # ---------------------------------------------fill out form----------------------------------------------------
        input_1_tax_id = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='tax_id']"))).send_keys("12345")
        input_2_company = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='company']"))).send_keys("ChicagoFx")
        input_3_first_name = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='firstname']"))).send_keys("Vladimir")
        input_4_last_name = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='lastname']"))).send_keys("Sharapov")
        input_5_address_1 = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='address1']"))).send_keys("test")
        input_6_address_2 = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='address2']"))).send_keys("test")
        input_7_postcode = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='postcode']"))).send_keys("60193")
        input_8_city = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='city']"))).send_keys("Chicago")

        # Dropdown list
        select_country = Select(browser.find_element_by_css_selector("select[name='country_code']"))
        select_country.select_by_visible_text("United States")
        select_state = Select(browser.find_element_by_css_selector("select[name='zone_code']"))
        select_state.select_by_value("IL")

        input_9_email = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='email']"))).send_keys(f"qatestervv2020+{x}@gmail.com")

        save_email = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='email']"))).get_attribute("value")

        input_10_phone = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='phone']"))).send_keys("1234567890")
        newsletter_checkbox = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[value='1']")))
        newsletter_checkbox.click()
        input_11_password = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='password']"))).send_keys(password)
        input_12_confirm_password = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='customer_form'] input[name='confirmed_password']"))).send_keys(password)

        create_account_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='create_account']")))
        create_account_button.click()

        logout_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#box-account li:last-child a")))
        logout_button.click()


        # ---------------------------------------------log in into existen account--------------------------------------
        input_login_email = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='login_form'] input[name='email']"))).send_keys(save_email)
        input_login_password = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='login_form'] input[name='password']"))).send_keys(password)
        login_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']")))
        login_button.click()

        logout_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#box-account li:last-child a")))
        logout_button.click()


