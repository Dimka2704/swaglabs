from selenium import webdriver
from pages.authorization_page import Authorization_page


def test_authorization():
    driver = webdriver.Chrome(executable_path='/Users/dmitrij/PycharmProjects/resource/chromedriver')
    ap = Authorization_page(driver)
    ap.authorization()


def test_incorrect_authorization_user_name():
    driver = webdriver.Chrome(executable_path='/Users/dmitrij/PycharmProjects/resource/chromedriver')
    ap = Authorization_page(driver)
    ap.incorrect_authorization_user_name()


def test_incorrect_authorization_password():
    driver = webdriver.Chrome(executable_path='/Users/dmitrij/PycharmProjects/resource/chromedriver')
    ap = Authorization_page(driver)
    ap.incorrect_authorization_password()
