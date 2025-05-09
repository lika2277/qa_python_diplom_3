import allure
from pages.base import PageBase

class Page(PageBase):
    @allure.step('Открыть страницу')
    def open(self, url = 'https://stellarburgers.nomoreparties.site/'):
        self.driver.get(url)