import time
from selenium import webdriver
from pages.authorization_page import Authorization_page
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_buy_product():
    driver = webdriver.Chrome(executable_path='/Users/dmitrij/PycharmProjects/resource/chromedriver')
    ap = Authorization_page(driver)
    ap.authorization()
    mp = Main_page(driver)
    mp.go_to_the_shopping_cart()
    cp = Cart_page(driver)
    cp.confirmation_product()
    cip = Client_information_page(driver)
    cip.input_information()
    pp = Payment_page(driver)
    pp.payment()
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(5)
