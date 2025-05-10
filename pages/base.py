from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import PageUrl

class PageBase:
    def __init__(self, driver, timeout = 5):
        self.driver = driver
        self.timeout = timeout

    def open(self, url=PageUrl.main):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def is_visible(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of_element_located(locator))
        return True

    def is_not_visible(self, locator, value):
        WebDriverWait(self.driver, self.timeout).until_not(expected_conditions.text_to_be_present_in_element(locator, value))
        return True

    def send_keys(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    def select(self, locator, index = 0):
       self.driver.find_elements(*locator)[index].click()

    def click(self, locator):
        self.is_visible(locator)
        self.driver.find_element(*locator).click()

    def scroll(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(locator))

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_windows(self):
        return self.driver.window_handles

    def switch_to_window(self, window):
        return self.driver.switch_to.window(window)

    def is_number_of_windows(self, number):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.number_of_windows_to_be(number))
        return True

    def is_url(self, url):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.url_to_be(url))
        return True