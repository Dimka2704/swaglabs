from selenium import webdriver
from pages.authorization_page import Authorization_page
import allure


@allure.description("Test authorization")
def test_authorization(set_up):
    driver = webdriver.Chrome(executable_path='/Users/dmitrij/PycharmProjects/resource/chromedriver')
    ap = Authorization_page(driver)
    ap.authorization()


@allure.description("Test incorrect authorization user name")
def test_incorrect_authorization_user_name(set_up):
    driver = webdriver.Chrome(executable_path='/Users/dmitrij/PycharmProjects/resource/chromedriver')
    ap = Authorization_page(driver)
    ap.incorrect_authorization_user_name()


@allure.description("Test incorrect authorization password")
def test_incorrect_authorization_password(set_up):
    driver = webdriver.Chrome(executable_path='/Users/dmitrij/PycharmProjects/resource/chromedriver')
    ap = Authorization_page(driver)
    ap.incorrect_authorization_password()
