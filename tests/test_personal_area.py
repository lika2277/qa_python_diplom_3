import allure
from pages.orders_feed import PageOrdersFeed

class TestPersonalArea:
    @staticmethod
    @allure.title('переход по клику на «Личный кабинет»')
    def test_go_personal_area_page_by_personal_area_button_success(browser, login, personal_area):
        _, user = login
        _, data = personal_area
        assert user.name == data["name"] and user.email.upper() == data["email"].upper()

    @staticmethod
    @allure.title('переход в раздел «История заказов»')
    def test_go_history_orders_page_from_personal_area_success(browser, personal_area):
        personal_area, _ = personal_area
        personal_area.click_feed_orders()
        orders_feed = PageOrdersFeed(browser)
        orders_feed.is_visible_feed_orders_page()
        assert browser.current_url == orders_feed.get_current_url()

    @staticmethod
    @allure.title('выход из аккаунта')
    def test_exit_from_personal_area_success(browser, login, personal_area):
        login, _ = login
        personal_area, _ = personal_area
        personal_area.is_visible_personal_area_page()
        personal_area.click_exit()
        login.is_visible_login_page()
        assert browser.current_url == login.get_current_url()