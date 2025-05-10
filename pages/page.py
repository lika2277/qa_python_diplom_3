import allure
from pages.base import PageBase
from data.urls import PageUrl

class Page(PageBase):
    @allure.step('Открыть страницу')
    def open(self, url = PageUrl.main):
        self.driver.get(url)