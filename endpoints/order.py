import requests
from random import randint

class Order:
    def __init__(self, url, ingredients):
        self.url = url
        self.ingredients = ingredients

    def create_order_without_authorization(self, order_data):
        response = requests.post(self.url, data=order_data)
        return response

    def create_order_with_authorization(self, order_data, user):
        response_login = user.login_user()
        headers = {
            'Authorization': response_login.json()["accessToken"]
        }
        response = requests.post(self.url, data=order_data, headers=headers)
        return response

    def get_data_order_by_user_name_with_authorization(self, user):
        response_login = user.login_user()
        headers = {
            'Authorization': response_login.json()["accessToken"]
        }
        response = requests.get(self.url, headers=headers)
        return response

    def get_data_order_by_user_name_without_authorization(self):
        response = requests.get(self.url)
        return response

    def gen_ingredients_data(self):
        ingredients = self.ingredients.get_list_id_ingredient()
        selected = []

        for i in range(1, randint(1, len(ingredients))):
            index = randint(0, len(ingredients) - 1)
            selected.append(ingredients[index])
            ingredients.remove(ingredients[index])
        return ({"ingredients": selected})