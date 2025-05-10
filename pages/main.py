import allure
import random
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base import PageBase

class PageMain(PageBase):
    # Кнопка "Войти в аккаунт" 
    locator_entrance_in_account_button = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    # Кнопка "Войти в аккаунт"
    locator_make_order_button = (By.XPATH, "//button[text()='Оформить заказ']")
    # Заголовок 'Соберите бургер'
    locator_title_container_ingredients = (By.XPATH, "// h1[text() = 'Соберите бургер']")
    # заголовок модального окна "Детали ингридиента"
    locator_title_ingredient_details_window = (By.XPATH, "//h2[contains(@class,'Modal_modal__title_modified')]")
    # номер заказа из модального окна "Детали ингридиента"
    locator_order_number_details_window = (By.XPATH, "//h2[contains(@class,'text_type_digits-large')]")
    # область корзины
    locator_basket = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket')]")
    # контейнер ингридиенnов
    locator_container_ingredients = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")
    # счетчик для конкретного ингридиента
    locator_ingredient_counter = (By.XPATH, ".//p[contains(@class, 'counter_counter')]")
    # кнопка "Закрыть" заголовок модального окна "Детали ингридиента" и "Детали заказа"
    locator_close_button_details_window = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    # заголовок модального окна "Идентификатор заказа"
    locator_title_order_details_window = (By.XPATH, "//div[contains(@class,'Modal_modal__contentBox')]/p[contains(@class,'text_type_main')]")
    # Кнопка "Личный кабинет"
    locator_account_personal_button = (By.XPATH, ".//a[@href='/account']")
    # Кнопка "Конструктор"
    locator_constructor_button = (By.XPATH, ".//li/a[@href='/']")
    # Кнопка "Лист заказов"
    locator_orders_feed_button = (By.XPATH, ".//a[@href='/feed']")

    @allure.step('Ждем пока загрузится главная страница')
    def is_visible_main_page(self):
        self.is_visible(self.locator_title_container_ingredients)

    @allure.step('Ищем заголовок "Соберите бургер"')
    def check_title_container_ingredients(self):
        return self.find(self.locator_title_container_ingredients)

    @allure.step('Кликаем на произвольный ингридиент')
    def click_random_ingredient(self):
        ingredient = random.choice(self.find_all(self.locator_container_ingredients))
        ingredient.click()

    @allure.step('Нажимаем кнопку "Лента заказов"')
    def click_feed_orders(self):
        self.is_visible(self.locator_orders_feed_button)
        self.click(self.locator_orders_feed_button)

    @allure.step('Нажимаем кнопку "Конструктор заказов"')
    def click_constructor(self):
        self.click(self.locator_constructor_button)

    @allure.step('Всплывающее окно с деталями ингридиентов')
    def is_visible_ingredient_details_window(self):
        return self.is_visible(self.locator_title_ingredient_details_window)

    @allure.step('Всплывающее окно с деталями заказа')
    def is_visible_order_details_window(self):
        return self.is_visible(self.locator_title_order_details_window)

    @allure.step('Закрываем всплывающее окно с деталями ингридиентов')
    def close_ingredient_details_window(self):
        self.click(self.locator_close_button_details_window)

    @allure.step('Добавляем произвольный ингридиент в заказ')
    def add_random_ingredient_in_order(self):
        ingredient = random.choice(self.find_all(self.locator_container_ingredients))
        basket = self.find(self.locator_basket)
        actions = ActionChains(self.driver)

        actions.drag_and_drop(self.find(self.locator_container_ingredients), basket).perform()
        actions.drag_and_drop(ingredient, basket).perform()
        return int(self.find(self.locator_ingredient_counter).text)

    @allure.step('Нажимаем кнопку "Личный кабинет"')
    def click_personal_area(self):
        self.click(self.locator_account_personal_button)

    @allure.step('Нажимаем кнопку "Оформить заказ"')
    def click_make_order(self):
        self.click(self.locator_make_order_button)

    @allure.step('Получаем номер заказа из окна с деталями заказа')
    def get_order_number_details_window(self):
        self.is_not_visible(self.locator_order_number_details_window, '9999')
        return (self.find(self.locator_order_number_details_window).text)

    @allure.step('Закрываем всплывающее окно с деталями заказа')
    def close_order_details_window(self):
        self.click(self.locator_close_button_details_window)
