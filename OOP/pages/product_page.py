from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):

    def add_product_to_cart(self):

        select_size = self.browser.find_elements_by_css_selector("select[name='options[Size]']")
        if len(select_size) != 0:
            select_size = Select(self.browser.find_element_by_css_selector("select[name='options[Size]']"))
            select_size.select_by_index(1)
            i = int(self.wait.until(
                EC.presence_of_element_located(ProductPageLocators.i)).get_attribute("textContent"))

            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
            add_to_cart_button.click()

            cart_items_quantity = self.wait.until(
                EC.text_to_be_present_in_element(ProductPageLocators.CART_ITEMS_QUANTITY, f"{i+1}"))

            self.browser.get("http://localhost/litecart/en/")
        else:
            i = int(self.wait.until(
                EC.presence_of_element_located(ProductPageLocators.i)).get_attribute("textContent"))

            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
            add_to_cart_button.click()

            cart_items_quantity = self.wait.until(
                EC.text_to_be_present_in_element(ProductPageLocators.CART_ITEMS_QUANTITY, f"{i+1}"))
            self.browser.get("http://localhost/litecart/en/")





