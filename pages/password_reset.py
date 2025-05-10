import allure
from pages.base import PageBase
from selenium.webdriver.common.by import By

class PagePasswordReset(PageBase):
    # Не активное поле ввода нового пароля
    locator_input_password = (By.XPATH, ".//form/fieldset//input[@type='password']")
    # Обводка активного поля ввода нового пароля
    locator_stroke_active_input_password = (By.XPATH, ".//div[contains(@class,'input_status_active')]")
    # Признак активности поле ввода нового пароля
    locator_active_input_password = (By.XPATH, ".//label[contains(@class,'input__placeholder-focused')]")
    # Поле ввода кода из письма
    locator_input_code = (By.XPATH, ".//form/fieldset//input[@type='text']")
    # Плейсхолдер для поле ввода кода из письма
    locator_input_code_place_holder = (By.XPATH, ".//form/fieldset[2]//label")
    # Кнопка "Сохранить"
    locator_save_button = (By.XPATH, ".//form/button[text()='Сохранить']")
    # кнопка показать/скрыть в поле ввода пароля
    locator_show_hide_button = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[name()='svg']")

    @allure.step('Ждем пока загрузится страница сброса пароля')
    def is_visible_reset_password_page(self):
        self.is_visible(self.locator_save_button)

    @allure.step('Получаем текст плейсхолдера в поле "Код из письма"')
    def get_place_holder_code_text(self):
        return (self.find(self.locator_input_code_place_holder).text)

    @allure.step('Нажимаем на кнопку показать/скрыть в поле ввода пароля')
    def click_show_hide(self):
        self.click(self.locator_show_hide_button)

    @allure.step('Проверяем обводку активного поля "Пароль"')
    def check_stroke_active_input_password(self):
        return self.find(self.locator_stroke_active_input_password)

    @allure.step('Проверяем, что поле "Пароль" стало активным')
    def check_active_input_password(self):
        return self.find(self.locator_active_input_password)
