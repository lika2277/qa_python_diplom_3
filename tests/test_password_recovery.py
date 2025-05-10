import allure

class TestPasswordRecovery:
    @staticmethod
    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_password_recovery_page_by_recover_password_button_success(browser, password_forget):
        assert browser.current_url == password_forget.get_current_url()

    @staticmethod
    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_recover_button_success(browser, password_reset):
        assert (browser.current_url == password_reset.get_current_url()
                and password_reset.get_place_holder_code_text() == 'Введите код из письма')

    @staticmethod
    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_activity_check_input_password_success(browser, password_reset):
        password_reset.click_show_hide()
        assert password_reset.check_active_input_password() and password_reset.check_stroke_active_input_password()
