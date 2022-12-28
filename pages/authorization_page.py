from selenium.webdriver import Keys
from base.base_class import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure


class Authorization_page(Base_page):

    url = "https://www.saucedemo.com/"

    """Ссылаемся на драйвер из базового класса Base"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Локаторы"""
    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    header_products = "//span[@class='title']"
    warning = "//div[@class='error-message-container error']"

    """Условия применения к элементу"""
    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_header_products(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.header_products)))

    def get_warning(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.warning)))

    """Действия с элементами"""
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def keyboard_login_button(self):
        self.get_login_button().send_keys(Keys.ENTER)
        print("Keyboard login button")

    "Авторизация"
    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name("standard_user")
            self.input_password("secret_sauce")
            self.click_login_button()
            self.assert_text_check(self.get_header_products(), "PRODUCTS")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")

    """Ошибка авторизации при неверном user_name"""
    def incorrect_authorization_user_name(self):
        with allure.step("Incorrect authorization user name"):
            Logger.add_start_step(method="incorrect_authorization_user_name")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name("standard_users")
            self.input_password("secret_sauce")
            self.keyboard_login_button()
            self.assert_text_check(self.get_warning(),
                                     "Epic sadface: Username and password do not match any user in this service")
            Logger.add_end_step(url=self.driver.current_url, method="incorrect_authorization_user_name")

    """Ошибка авторизации при неверном password"""
    def incorrect_authorization_password(self):
        with allure.step("Incorrect authorization password"):
            Logger.add_start_step(method="incorrect_authorization_password")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name("standard_user")
            self.input_password("secret_sauces")
            self.keyboard_login_button()
            self.assert_text_check(self.get_warning(),
                                     "Epic sadface: Username and password do not match any user in this service")
            Logger.add_end_step(url=self.driver.current_url, method="incorrect_authorization_password")

