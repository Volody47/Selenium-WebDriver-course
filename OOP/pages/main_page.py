from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .product_page import ProductPage
from .locators import MainPageLocators



class MainPage(BasePage):


    def open(self):
        self.browser.get("http://localhost/litecart/en/")
        return self

    def select_product(self):
        product_page = ProductPage(self.browser)
        product_items = self.wait.until(EC.presence_of_all_elements_located(MainPageLocators.PRODUCT_ITEMS))
        i = 0
        for item in product_items:
            cart_items_quantity = self.wait.until(
                EC.presence_of_element_located(MainPageLocators.CART_ITEMS_QUANTITY)).get_attribute("textContent")
            if int(cart_items_quantity) != 3:
                add_item = self.wait.until(EC.presence_of_all_elements_located(MainPageLocators.ADD_ITEM))[i]
                add_item.click()
                product_page.add_product_to_cart()
                i += 1
            else:
                break

                # cart_items_quantity == 3
        cart_items_quantity = int(self.wait.until(
            EC.presence_of_element_located(MainPageLocators.CART_ITEMS_QUANTITY)).get_attribute("textContent"))
        assert cart_items_quantity == 3




