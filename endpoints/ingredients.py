import requests

class Ingredients:
    def __init__(self, url):
        self.url = url

    def get_list_id_ingredient(self):
        response = requests.get(self.url)
        list_ingredients = []
        for i in response.json()["data"]:
            list_ingredients.append(i['_id'])
        return list_ingredients