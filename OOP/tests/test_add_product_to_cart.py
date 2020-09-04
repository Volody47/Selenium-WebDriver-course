from oop.pages.main_page import MainPage
from oop.pages.cart_page import CartPage


def test_add_product_to_cart(browser):
    main_page = MainPage(browser)
    cart_page = CartPage(browser)


    main_page.open()
    main_page.select_product()
    cart_page.remove_product_from_cart()



