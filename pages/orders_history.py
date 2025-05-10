import allure
from selenium.webdriver.common.by import By
from pages.base import PageBase

class PageOrdersHistory(PageBase):
    # список заказов пользователя
    locator_list_orders_user = (By.XPATH, ".//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits')]")
    # Кнопка "Лист заказов"
    locator_orders_feed_button = (By.XPATH, ".//a[@href='/feed']")

    @allure.step('Получаем список заказов пользователя')
    def get_list_orders_user(self):
        list_orders=[]
        for l in self.find_all(self.locator_list_orders_user):
           list_orders.append(l.text)
        return list_orders

    @allure.step('Ждем пока загрузится страница c Историей заказов Пользователя')
    def is_visible_orders_history_page(self):
        return self.is_visible(self.locator_list_orders_user)

    @allure.step('Нажимаем кнопку "Лента заказов"')
    def click_feed_orders(self):
        self.click(self.locator_orders_feed_button)

    @staticmethod
    @allure.step('Сравнение списков заказов')
    def list_compare(a, b):
        return (all(i == j for i, j in zip(a, b)))