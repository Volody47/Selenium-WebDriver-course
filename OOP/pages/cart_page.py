from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def remove_product_from_cart(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable(CartPageLocators.CHECKOUT_BUTTON))
        checkout_button.click()

        list_item = self.wait.until(
            EC.presence_of_all_elements_located(CartPageLocators.LIST_ITEM))

        while len(list_item) != 0:
            item = self.wait.until(
                EC.element_to_be_clickable(CartPageLocators.ITEM)).click()
            self.browser.refresh()
            self.wait.until(EC.staleness_of(list_item[0]))
            list_item = self.browser.find_elements_by_css_selector(".dataTable tr:not(.header) .item")

        empty_cart = self.wait.until(
            EC.presence_of_element_located(CartPageLocators.EMPTY_CART)).text
        assert empty_cart == "There are no items in your cart."
