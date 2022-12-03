from base.base_class import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_page(Base_page):

    """Ссылаемся на драйвер из базового класса Base"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Локаторы"""
    remove_button = "//button[@id='remove-test.allthethings()-t-shirt-(red)']"
    continue_shopping_button = "//button[@id='continue-shopping']"
    checkout_button = "//button[@id='checkout']"

    """Условия применения к элементу"""
    def get_remove_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.remove_button)))

    def get_continue_shopping_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_shopping_button)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    """Действия с элементами"""
    def click_remove_button(self):
        self.get_remove_button().click()
        print("Click remove button")

    def click_continue_shopping_button(self):
        self.get_continue_shopping_button().click()
        print("Click continue shopping button")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    """Удаление товара из корзины"""
    def remove_product_from_cart(self):
        self.get_current_url()
        self.click_remove_button()
        self.get_screenshot()

    """Подтверждение, что товар добавлен"""
    def confirmation_product(self):
        self.get_current_url()
        self.click_checkout_button()


