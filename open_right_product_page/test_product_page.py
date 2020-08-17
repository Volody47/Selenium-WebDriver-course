from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://localhost/litecart/en/"


class TestMainPage1():

    #---------------------------------------------test_product_name-----------------------------------------------------
    def test_product_name(self, browser):
        browser.get(link)

        product_item = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#box-campaigns a.link")))
        product_name = product_item.get_attribute("title")
        product_item.click()

        page_title = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#box-product .title"))).text
        assert product_name == page_title

    # ---------------------------------------------test_product_price---------------------------------------------------
    def test_product_price(self, browser):
        browser.get(link)

        regular_price_main_page = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#box-campaigns .regular-price"))).text
        campaign_price_main_page = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#box-campaigns .campaign-price"))).text

        product_item = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#box-campaigns a.link"))).click()

        regular_price_product_page = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "regular-price"))).text
        campaign_price_product_page = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "campaign-price"))).text

        assert regular_price_main_page == regular_price_product_page, "regular_price_main_page != regular_price_product_page"
        assert campaign_price_main_page == campaign_price_product_page, "campaign_price_main_page != campaign_price_product_page"

    # ---------------------------------------------test_product_price_color---------------------------------------------
    def test_product_price_color(self, browser):
        browser.get(link)
                                                    # Main page
        regular_price_main_page_color = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#box-campaigns .regular-price"))).value_of_css_property("color")
        regular_price_element_crossed_out = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#box-campaigns .regular-price"))).get_attribute("tagName")
        regular_price_main_page_size = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#box-campaigns .regular-price"))).value_of_css_property("font-size")
        # Create list
        regular_price_list_color = regular_price_main_page_color.replace("rgba(", "").replace(")", "").replace("rgb(", "").strip('][').split(', ')
        regular_price_main_page_size_number = float(regular_price_main_page_size.replace("px", ""))
        # Verification
        assert regular_price_list_color[0:3] == regular_price_list_color[0:3], "Value of 'R', 'G', 'B' not same"
        assert regular_price_element_crossed_out == "S", "element not crossed out"


        campaign_price_main_page_color = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#box-campaigns .campaign-price"))).value_of_css_property("color")
        campaign_price_element_strong = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#box-campaigns .campaign-price"))).get_attribute("tagName")
        campaign_price_main_page_size = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#box-campaigns .campaign-price"))).value_of_css_property("font-size")
        # Create list
        campaign_price_list_color = campaign_price_main_page_color.replace("rgba(", "").replace(")", "").replace("rgb(", "").strip('][').split(', ')
        campaign_price_main_page_size_number = float(campaign_price_main_page_size.replace("px", ""))
        x = ['0', '0']
        # Verification
        assert campaign_price_list_color[1:3] == x, "Value of 'G', 'B' not 0"
        assert campaign_price_element_strong == "STRONG", "element not 'strong'"
        # Verification element size
        assert regular_price_main_page_size_number < campaign_price_main_page_size_number, "New price element should be bigger "

                                                    # Click on product
        product_item = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#box-campaigns a.link"))).click()

                                                    # Product page
        regular_price_product_page_color = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "regular-price"))).value_of_css_property("color")
        regular_price_element_crossed_out = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "regular-price"))).get_attribute("tagName")
        regular_price_product_page_size = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "regular-price"))).value_of_css_property("font-size")
        # Create list
        regular_price_list_color = regular_price_product_page_color.replace("rgba(", "").replace(")", "").replace("rgb(", "").strip('][').split(', ')
        regular_price_product_page_size_number = float(regular_price_product_page_size.replace("px", ""))
        # Verification
        assert regular_price_list_color[0:3] == regular_price_list_color[0:3], "Value of 'R', 'G', 'B' not same"
        assert regular_price_element_crossed_out == "S", "element not crossed out"


        campaign_price_product_page_color = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "campaign-price"))).value_of_css_property("color")
        campaign_price_element_strong = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "campaign-price"))).get_attribute("tagName")
        campaign_price_product_page_size = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "campaign-price"))).value_of_css_property("font-size")
        # Create list
        campaign_price_list_color = campaign_price_product_page_color.replace("rgba(", "").replace(")", "").replace("rgb(", "").strip('][').split(', ')
        campaign_price_product_page_size_number = float(campaign_price_product_page_size.replace("px", ""))
        x = ['0', '0']
        # Verification
        assert campaign_price_list_color[1:3] == x, "Value of 'G', 'B' not 0"
        assert campaign_price_element_strong == "STRONG", "element not 'strong'"
        # Verification element size
        assert regular_price_product_page_size_number < campaign_price_product_page_size_number, "New price element should be bigger "






