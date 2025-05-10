import allure
from pages.orders_feed import PageOrdersFeed
from pages.personal_area import PagePersonalArea
from pages.orders_history import PageOrdersHistory

class TestOrderFeed:
    @staticmethod
    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_pop_up_order_window_success(browser, orders_feed):
        orders_feed.click_random_order()
        assert orders_feed.is_visible_order_details_window()

    @staticmethod
    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_check_history_orders_into_orders_food_success(browser, order, main, login):
        _, user = login
        order.create_order_with_authorization(order.gen_ingredients_data(), user)
        main.click_personal_area()

        personal_area = PagePersonalArea(browser)
        personal_area.is_visible_personal_area_page()
        personal_area.click_history_orders()

        orders_history = PageOrdersHistory(browser)
        orders_history.is_visible_orders_history_page()
        list_orders_user = orders_history.get_list_orders_user()
        orders_history.click_feed_orders()

        orders_feed = PageOrdersFeed(browser)
        orders_feed.is_visible_feed_orders_page()
        list_orders_all = orders_feed.get_list_orders()

        assert orders_history.list_compare(list_orders_user, list_orders_all)

    @staticmethod
    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_check_increasing_counter_all_time_value_success(browser, main, orders_feed):
        current_count = orders_feed.get_count_all_time()
        orders_feed.make_order(main)
        main.click_feed_orders()
        orders_feed.is_visible_feed_orders_page()
        new_count = orders_feed.get_count_all_time()
        assert (new_count - current_count) == 1

    @staticmethod
    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_check_increasing_counter_today_value_success(browser, main, orders_feed):
        current_count = orders_feed.get_count_today()
        orders_feed.make_order(main)
        main.click_feed_orders()
        orders_feed.is_visible_feed_orders_page()
        new_count = orders_feed.get_count_today()
        assert (new_count - current_count) == 1

    @staticmethod
    @allure.title('после оформления заказа его номер появляется в разделе "В работе"')
    def test_check_order_number_success(browser, main, orders_feed):
        number_order1 = orders_feed.make_order(main)
        main.click_feed_orders()
        orders_feed.is_visible_feed_orders_page()
        number_order2 = orders_feed.get_order_number_in_work()
        assert number_order1 == number_order2
