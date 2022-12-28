from base.base_class import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure


class Payment_page(Base_page):

    """Ссылаемся на драйвер из базового класса Base"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Локаторы"""
    header_checkout = "//span[@class='title']"
    t_shirt_red_finish = "//div[@class='inventory_item_name']"
    t_shirt_price_finish = "//div[@class='inventory_item_price']"
    finish_button = "//button[@id='finish']"

    """Условия применения к элементу"""
    def get_header_checkout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.header_checkout)))

    def get_t_shirt_red_finish(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.t_shirt_red_finish)))

    def get_t_shirt_price_finish(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.t_shirt_price_finish)))

    def get_finish_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    """Действия с элементами"""
    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")

    """Оплата товара"""
    def payment(self):
        with allure.step("Payment"):
            Logger.add_start_step(method="payment")
            self.get_current_url()
            self.assert_text_check(self.get_header_checkout(), "CHECKOUT: OVERVIEW")
            self.assert_text_check(self.get_t_shirt_red_finish(), "Test.allTheThings() T-Shirt (Red)")
            self.assert_text_check(self.get_t_shirt_price_finish(), "$15.99")
            self.click_finish_button()
            Logger.add_end_step(url=self.driver.current_url, method="payment")
