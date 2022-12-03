import time
from selenium import webdriver
from pages.authorization_page import Authorization_page
from pages.cart_page import Cart_page
from pages.main_page import Main_page
from base.base_class import Base_page


def test_remove_product_from_cart():
    driver = webdriver.Chrome(executable_path='/Users/dmitrij/PycharmProjects/resource/chromedriver')
    ap = Authorization_page(driver)
    ap.authorization()
    mp = Main_page(driver)
    mp.go_to_the_shopping_cart()
    cp = Cart_page(driver)
    cp.remove_product_from_cart()
    cp.click_continue_shopping_button()
    mp.scroll_down()
    bp = Base_page(driver)
    bp.assert_text_check(mp.get_add_to_cart_button(),"ADD TO CART")

    time.sleep(5)
