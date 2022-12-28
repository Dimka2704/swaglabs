import time
from selenium import webdriver
from pages.authorization_page import Authorization_page
from pages.main_page import Main_page
import allure


@allure.description("Test add to cart product")
def test_add_to_cart_product(set_up):
    driver = webdriver.Chrome(executable_path='/Users/dmitrij/PycharmProjects/resource/chromedriver')
    ap = Authorization_page(driver)
    ap.authorization()
    mp = Main_page(driver)
    mp.t_shirt_add_to_cart()

    time.sleep(5)