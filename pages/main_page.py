import time
from base.base_class import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure


class Main_page(Base_page):

    """Ссылаемся на драйвер из базового класса Base"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Локаторы"""
    t_shirt_red = "(//div[@class='inventory_item_name'])[6]"
    add_to_cart_button = "//button[@name='add-to-cart-test.allthethings()-t-shirt-(red)']"
    t_shirt_price = "(//div[@class='inventory_item_price'])[6]"
    cart = "//a[@class='shopping_cart_link']"
    menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"
    link_logout = "//a[@id='logout_sidebar_link']"

    """Условия применения к элементу"""
    def get_t_shirt_red(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.t_shirt_red)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_t_shirt_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.t_shirt_price)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))

    def get_link_logout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_logout)))

    """Действия с элементами"""
    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0,500)")
        print("Scroll down")

    def scroll_ap(self):
        self.driver.execute_script("window.scrollTo(500,0)")
        print("Scroll up")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click add to cart button")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_menu(self):
        self.get_menu().click()
        print("Click menu")

    def click_link_about(self):
        self.get_link_about().click()
        print("Click about")

    def click_link_logout(self):
        self.get_link_logout().click()
        print("Click logout")

    """Добавление товара в корзину"""
    def t_shirt_add_to_cart(self):
        with allure.step("T-shirt add to cart"):
            Logger.add_start_step(method="t_shirt_add_to_cart")
            self.get_current_url()
            self.scroll_down()
            self.assert_text_check(self.get_t_shirt_red(), "Test.allTheThings() T-Shirt (Red)")
            self.assert_text_check(self.get_t_shirt_price(), "$15.99")
            self.click_add_to_cart_button()
            self.scroll_ap()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="t_shirt_add_to_cart")

    """Переход в корзину с товаром"""
    def go_to_the_shopping_cart(self):
        with allure.step("Go to the shopping cart"):
            Logger.add_start_step(method="go_to_the_shopping_cart")
            self.get_current_url()
            self.scroll_down()
            self.click_add_to_cart_button()
            self.scroll_ap()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="go_to_the_shopping_cart")

    '''Открытие меню О нас'''
    def select_menu_about(self):
        with allure.step("Select menu about"):
            Logger.add_start_step(method="select_menu_about")
            self.get_current_url()
            time.sleep(1.5)
            self.click_menu()
            self.click_link_about()
            self.assert_url("https://saucelabs.com/")
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_about")

    '''Разлогиниться на сайте'''
    def select_menu_logout(self):
        with allure.step("Select menu logout"):
            Logger.add_start_step(method="select_menu_logout")
            self.get_current_url()
            time.sleep(1.5)
            self.click_menu()
            self.click_link_logout()
            self.assert_url("https://www.saucedemo.com/")
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_logout")


