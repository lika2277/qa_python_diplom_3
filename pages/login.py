import allure
from selenium.webdriver.common.by import By
from pages.base import PageBase

class PageLogin(PageBase):
    # Ссылка "Восстановить пароль"
    locator_password_recovery_link = (By.XPATH, ".//a[@href='/forgot-password']")
    # Кнопка "Войти" на форме входа
    locator_entrance_button = (By.XPATH, ".// button[text() = 'Войти']")
    # Поле ввода email при входе
    locator_input_email = (By.XPATH, ".//form/fieldset[1]//input")
    # Поле ввода пароля при входе
    locator_input_password = (By.XPATH, ".//form/fieldset[2]//input")
    # кнопка показать/скрыть в поле ввода пароля
    locator_show_hide_button = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[name()='svg']")

    @allure.step('Ждем пока загрузится страница авторизации')
    def is_visible_login_page(self):
        self.is_visible(self.locator_entrance_button)

    @allure.step('Нажимаем на ссылку "Восстановить пароль"')
    def click_password_recovery_link(self):
        self.click(self.locator_password_recovery_link)

    @allure.step('Нажимаем на кнопку показать/скрыть в поле ввода пароля')
    def click_show_hide_button(self):
        self.click(self.locator_show_hide_button)

    @allure.step('Вводим значение в поле Email')
    def set_value_email(self, email):
        self.send_keys(self.locator_input_email, email)

    @allure.step('Вводим значение в поле Пароль')
    def set_value_password(self, password):
        self.send_keys(self.locator_input_password, password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_entrance_button(self):
        self.click(self.locator_entrance_button)

    @allure.step('Входим в систему')
    def login_user(self, reg_user):
        self.is_visible_login_page()
        self.set_value_email(reg_user.email)
        self.set_value_password(reg_user.password)
        self.click_entrance_button()