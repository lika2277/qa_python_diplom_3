from typing import Any, Generator
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from endpoints.ingredients import Ingredients
from endpoints.order import Order
from endpoints.user import User
from pages.login import PageLogin
from pages.main import PageMain
from pages.password_reset import PagePasswordReset
from pages.password_forget import PagePasswordForget
from pages.personal_area import PagePersonalArea
from pages.orders_feed import PageOrdersFeed

type WebDriver = Generator[ChromeDriver | FirefoxDriver, Any, None]

url = 'https://stellarburgers.nomoreparties.site/'

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="firefox", help="supported browsers: chrome or firefox")

@pytest.fixture()
def browser(request) -> WebDriver:
    browser = request.config.getoption("--browser")
    if 'chrome' in browser.lower():
        driver = webdriver.Chrome()
    elif 'firefox' in browser.lower():
        driver = webdriver.Firefox()
    else:
        raise ValueError('Указан неверный браузер')
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def user():
    user = User(url)
    user.create_user()
    yield user
    user.delete_user()

@pytest.fixture(scope='function')
def main(browser):
    main = PageMain(browser)
    main.open()
    main.is_visible_main_page()
    return main

@pytest.fixture(scope='function')
def login(browser, main, user) -> tuple[PageLogin, User]:
    main.click_personal_area()
    login = PageLogin(browser)
    login.login_user(user)
    return login, user

@pytest.fixture(scope='function')
def orders_feed(browser, main, login):
    main.click_feed_orders()
    orders_feed = PageOrdersFeed(browser)
    orders_feed.is_visible_order_feed_page()
    return orders_feed

@pytest.fixture(scope='function')
def password_forget(browser, main) -> PagePasswordForget:
    main.click_personal_area()
    login = PageLogin(browser)
    login.click_password_recovery_link()

    password_forget = PagePasswordForget(browser)
    password_forget.is_visible_login_page()
    return password_forget

@pytest.fixture(scope='function')
def password_reset(browser, user, password_forget):
    password_forget.set_email(user.email)
    password_forget.click_password_recovery()

    password_reset = PagePasswordReset(browser)
    password_reset.is_visible_reset_password_page()
    return password_reset

@pytest.fixture(scope='function')
def personal_area(browser, login):
    personal_area = PagePersonalArea(browser)
    personal_area.click_personal_area()
    data = personal_area.get_personal_area_data()
    return personal_area, data

@pytest.fixture()
def order():
    ingredients = Ingredients(url)
    order = Order(url, ingredients)
    return order
