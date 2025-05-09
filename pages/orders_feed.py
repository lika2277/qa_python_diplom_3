import random
import allure
from selenium.webdriver.common.by import By
from pages.page import Page
from pages.main import PageMain

class PageOrdersFeed(Page):
    # Заголовок 'Лента заказов'
    locator_title_order_feed = (By.XPATH, ".//h1[text() = 'Лента заказов']")
    # список всех заказов
    locator_list_all_orders = (By.XPATH, ".//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits')]")
    # Список всех заказов
    locator_container_orders = (By.XPATH, ".//a[contains(@class,'OrderHistory_link')]")
    # Всплывающее окно с деталями заказа.
    locator_pop_up_order_window = (By.XPATH, ".//div[contains(@class,'Modal_orderBox')]")
    # Счетчик "Выполнено за все время"
    locator_order_number_in_work = (By.XPATH, ".//ul[contains(@class,'OrderFeed_orderListReady')] /li")
    # Счетчик "Выполнено за все время"
    locator_all_time_counter_value = (By.XPATH, ".//p[text()='Выполнено за все время:']/../p[contains(@class,'OrderFeed_number')]")
    # Счетчик "Выполнено за сегодня"
    locator_today_counter_value = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/../p[contains(@class,'OrderFeed_number')]")
    # Кнопка "Конструктор"
    locator_constructor_button = (By.XPATH, ".//li/a[@href='/']")

    @allure.step('Ждем пока загрузится страница ленты заказов')
    def is_visible_order_feed_page(self):
        self.is_visible(self.locator_title_order_feed)

    @allure.step('Кликаем на произвольный заказ')
    def click_random_order(self):
        order = random.choice(self.find_all(self.locator_container_orders))
        order.click()

    @allure.step('Ждем всплывающее окно с деталями заказа')
    def is_visible_order_details_window(self):
        return self.is_visible(self.locator_pop_up_order_window)

    @allure.step('Ждем пока загрузится главная страница')
    def is_visible_feed_orders_page(self):
        self.is_visible(self.locator_title_order_feed)

    @allure.step('Считываем значение счетчика "Выполнено за всё время"')
    def get_count_all_time(self):
        return int(self.find(self.locator_all_time_counter_value).text)

    @allure.step('Считываем номер заказа в блоке "В работе"')
    def get_order_number_in_work(self):
        self.is_not_visible(self.locator_order_number_in_work, 'Все текущие заказы готовы!')
        return int(self.find(self.locator_order_number_in_work).text)

    @allure.step('Считываем значение счетчика "Выполнено за сегодня"')
    def get_count_today(self):
        return int(self.find(self.locator_today_counter_value).text)

    @allure.step('Нажимаем кнопку "Конструктор заказов"')
    def click_constructor_button(self):
        self.click(self.locator_constructor_button)

    @allure.step('Создаем заказ с ингридиентами')
    def make_order(self, main_page: PageMain):
        self.click_constructor_button()
        main_page.is_visible_main_page()
        main_page.add_random_ingredient_in_order()
        main_page.click_make_order()
        main_page.is_visible_order_details_window()
        order_number = main_page.get_order_number_details_window()
        main_page.close_order_details_window()
        main_page.click_feed_orders()
        return int(order_number)

    @allure.step('Получаем номера заказов из "Ленты заказов"')
    def get_list_orders(self):
        list_orders = []
        for l in self.find_all(self.locator_list_all_orders):
            list_orders.append(l.text)
        return list_orders
