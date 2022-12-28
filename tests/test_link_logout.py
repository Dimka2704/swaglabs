import time
from selenium import webdriver
from pages.authorization_page import Authorization_page
from pages.main_page import Main_page
import allure


@allure.description("Test link logout")
def test_link_logout(set_up):
    driver = webdriver.Chrome(executable_path='/Users/dmitrij/PycharmProjects/resource/chromedriver')
    ap = Authorization_page(driver)
    ap.authorization()
    mp = Main_page(driver)
    mp.select_menu_logout()

    time.sleep(5)