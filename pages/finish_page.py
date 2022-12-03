from base.base_class import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Finish_page(Base_page):

    """Ссылаемся на драйвер из базового класса Base"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Cравнение URL и создание скриншота на завершающей страницы оформления товара"""
    def finish(self):
        self.get_current_url()
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        self.get_screenshot()


