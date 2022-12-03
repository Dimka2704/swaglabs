import time
from base.base_class import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    """Добавление товара в корзину"""
    def t_shirt_add_to_cart(self):
        self.get_current_url()
        self.scroll_down()
        self.assert_text_check(self.get_t_shirt_red(), "Test.allTheThings() T-Shirt (Red)")
        self.assert_text_check(self.get_t_shirt_price(), "$15.99")
        self.click_add_to_cart_button()
        self.scroll_ap()
        self.get_screenshot()

    """Переход в корзину с товаром"""
    def go_to_the_shopping_cart(self):
        self.get_current_url()
        self.scroll_down()
        self.click_add_to_cart_button()
        self.scroll_ap()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        time.sleep(1.5)
        self.click_menu()
        self.click_link_about()
        self.assert_url("https://saucelabs.com/")
