import datetime


class Base_page():

    """Метод для хранения драйвера"""
    def __init__(self, driver):
        self.driver = driver

    """Хранение текущей URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)

    """Проверка текста"""
    def assert_text_check(self, text, result):
        value_text = text.text
        assert value_text == result
        print("Success")

    """Скриншот экрана"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot('/Users/dmitrij/PycharmProjects/swaglabs/screen/' + name_screenshot)

    """Проверка URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL MATCHES")

