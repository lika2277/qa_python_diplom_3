import requests
import random
import string

class User:
    def __init__(self, urls):
        self.urls = urls
        self.name = ''
        self.password = ''
        self.email = ''
        self.accessToken = ''
        self.user_data = {}

    def create_user(self):
        user_data = self.gen_user_data()
        response = requests.post(self.urls.get('register'), data=user_data)
        if response.status_code == 200:
            self.name = user_data["name"]
            self.password = user_data["password"]
            self.email = user_data["email"]
            self.accessToken = response.json()["accessToken"]
            self.user_data = user_data
        return response

    @staticmethod
    def generate_random_string(length=0):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def gen_user_data(self):
        user_data = {
            "name": self.generate_random_string(10),
            "password": self.generate_random_string(10),
            "email": f'{self.generate_random_string(5)}@{self.generate_random_string(5)}.{self.generate_random_string(2)}'
        }
        return user_data

    def delete_user(self):
        self.login_user()
        headers = {'Authorization': self.accessToken}
        response = requests.delete(self.urls.get('user'), headers=headers)
        return response

    def login_user(self):
        user_data = {"name": self.name,
                     "password": self.password,
                     "email": self.email}
        response = requests.post(self.urls.get('login'), data=user_data)
        if response.status_code == 200:
            self.accessToken = response.json()["accessToken"]
        return response
