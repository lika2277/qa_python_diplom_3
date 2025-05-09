import allure

class TestMain:
    @allure.title('переход по клику на «Конструктор»')
    @staticmethod
    def test_go_to_constructor_page_success(browser, main):
        main.click_feed_orders()
        main.click_constructor()
        assert browser.current_url == main.get_current_url() and main.check_title_container_ingredients()

    @allure.title('переход по клику на «Лента заказов»')
    @staticmethod
    def test_go_to_history_orders_page_success(browser, orders_feed):
        assert browser.current_url == orders_feed.get_current_url()

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @staticmethod
    def test_pop_up_window_by_click_success(main):
        main.click_random_ingredient()
        assert main.is_visible_ingredient_details_window()

    @allure.title('всплывающее окно закрывается кликом по крестику,')
    @staticmethod
    def test_close_pop_up_window_success(main):
        main.click_random_ingredient()
        main.is_visible_ingredient_details_window()
        main.close_ingredient_details_window()
        assert main.check_title_container_ingredients()

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @staticmethod
    def test_counter_increase_success(main):
        counter = (main.add_random_ingredient_in_order())
        assert int(counter) > 0

    @allure.title('залогиненный пользователь может оформить заказ')
    @staticmethod
    def test_add_order_by_auth_user_success(main, login):
        main.is_visible_main_page()
        main.add_random_ingredient_in_order()
        main.click_make_order()
        assert main.is_visible_order_details_window()
