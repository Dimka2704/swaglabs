import time
from selenium import webdriver
from pages.authorization_page import Authorization_page
from pages.main_page import Main_page
import allure


@allure.description("Test link about")
def test_link_about(set_up):
    driver = webdriver.Chrome(executable_path='/Users/dmitrij/PycharmProjects/resource/chromedriver')
    ap = Authorization_page(driver)
    ap.authorization()
    mp = Main_page(driver)
    mp.select_menu_about()

    time.sleep(5)