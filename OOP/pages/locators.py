from selenium.webdriver.common.by import By


class MainPageLocators():
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product a.link")
    CART_ITEMS_QUANTITY = (By.CSS_SELECTOR, "span.quantity")
    ADD_ITEM = (By.CSS_SELECTOR, ".product a.link")


class ProductPageLocators():
    i = (By.CSS_SELECTOR, "span.quantity")
    CART_ITEMS_QUANTITY = (By.CSS_SELECTOR, "span.quantity")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[name='add_cart_product']")


class CartPageLocators():
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#cart .link")
    LIST_ITEM = (By.CSS_SELECTOR, ".dataTable tr:not(.header) .item")
    ITEM = (By.CSS_SELECTOR, "button[name='remove_cart_item']")
    EMPTY_CART = (By.CSS_SELECTOR, "#checkout-cart-wrapper em")