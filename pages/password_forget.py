import allure
from pages.base import PageBase
from selenium.webdriver.common.by import By

class PagePasswordForget(PageBase):
    # Поле ввода email при регистрации
    locator_input_email = (By.XPATH, ".//form/fieldset//input")
    # Кнопка "Восстановить"
    locator_recovery_button = (By.XPATH, ".//form/button[text()='Восстановить']")

    @allure.step('Ждем пока загрузится страница ввода email, для воостановления забытого пароля')
    def is_visible_login_page(self):
        self.is_visible(self.locator_input_email)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_password_recovery(self):
        self.click(self.locator_recovery_button)

    @allure.step('Вводим значение в поле EMAIL')
    def set_email(self, email):
        self.send_keys(self.locator_input_email, email)