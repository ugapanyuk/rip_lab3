from BaseClient import BaseClient
import requests

class User(BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'users.get'
    http_method = 'GET'
    param = 'user_ids'

    def __init__(self, username):
        super(User, self).__init__()
        self.username = username

    # Склейка url
    def generate_url(self):
        return '{0}{1}?{2}={3}'.format(self.BASE_URL, self.method, self.param, self.username)

    # Отправка запроса к VK API
    def _get_data(self):
        response = requests.get(self.generate_url())
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        json = response.json()
        res = json['response'][0]['uid']
        return res

    def execute(self):
        return self._get_data()
