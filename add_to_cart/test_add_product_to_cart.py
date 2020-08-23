from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


link = "http://localhost/litecart/en/"


class TestMainPage1():

    def test_add_to_cart(self, browser):
        wait = WebDriverWait(browser, 5)
        browser.get(link)

        product_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product a.link")))
        i = 0
        for item in product_items:
            cart_items_quantity = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.quantity"))).get_attribute("textContent")
            if int(cart_items_quantity) != 3:
                add_item = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product a.link")))[i]
                add_item.click()
                select_size = browser.find_elements_by_css_selector("select[name='options[Size]']")
                if len(select_size) != 0:
                    select_size = Select(browser.find_element_by_css_selector("select[name='options[Size]']"))
                    select_size.select_by_index(1)
                    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='add_cart_product']")))
                    add_to_cart_button.click()

                    cart_items_quantity = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), f"{i+1}"))
                    browser.get(link)
                else:
                    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='add_cart_product']")))
                    add_to_cart_button.click()

                    cart_items_quantity = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), f"{i+1}"))
                    browser.get(link)
                i += 1
            else:
                break
                                                          # Delete items from cart
        checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#cart .link")))
        checkout_button.click()

        list_item = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".dataTable tr:not(.header) .item")))

        while len(list_item) != 0:
            item = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='remove_cart_item']"))).click()
            browser.refresh()
            wait.until(EC.staleness_of(list_item[0]))
            list_item = browser.find_elements_by_css_selector(".dataTable tr:not(.header) .item")


        empty_cart = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#checkout-cart-wrapper em"))).text
        assert empty_cart == "There are no items in your cart."








