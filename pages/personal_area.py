import allure
from selenium.webdriver.common.by import By
from pages.base import PageBase

class PagePersonalArea(PageBase):
    # Поле ввода Имени в профиле (в личном кабинете)
    locator_input_name = (By.XPATH, ".//div//li[1]//input")
    # Поле ввода email  в профиле (в личном кабинете)
    locator_input_email = (By.XPATH, ".//div//li[2]//input")
    # Поле ввода Пароля  в профиле (в личном кабинете)
    locator_input_password = (By.XPATH, ".//div//li[3]//input")
    # Кнопка "Выход" в личном кабинете
    locator_exit_button = (By.XPATH, ".//button[text()='Выход']")
    # Ссылка "История заказов"
    locator_history_orders_link = (By.XPATH, ".//a[@href='/account/order-history']")
    # Кнопка "Личный кабинет"
    locator_account_personal_button = (By.XPATH, ".//a[@href='/account']")
    # Кнопка "Лист заказов"
    locator_orders_feed_button = (By.XPATH, ".//a[@href='/feed']")

    @allure.step('Получаем данные пользователя в личном кабинете')
    def get_personal_area_data(self):
        self.is_visible(self.locator_input_name)
        data = {
            "name": self.find(self.locator_input_name).get_attribute("value"),
            "email": self.find(self.locator_input_email).get_attribute("value"),
            "password": self.find(self.locator_input_password).get_attribute("value")
        }
        return data

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_exit(self):
        self.click(self.locator_exit_button)

    @allure.step('Ждем пока загрузится страница личного кабинета')
    def is_visible_personal_area_page(self):
        self.is_visible(self.locator_input_password)

    @allure.step('Нажимаем на раздел "История заказов"')
    def click_history_orders(self):
        self.click(self.locator_history_orders_link)

    @allure.step('Нажимаем кнопку "Личный кабинет"')
    def click_personal_area(self):
        self.click(self.locator_account_personal_button)

    @allure.step('Нажимаем кнопку "Лента заказов"')
    def click_feed_orders(self):
        self.click(self.locator_orders_feed_button)