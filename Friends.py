from BaseClient import BaseClient
import requests
import datetime
from dateutil import parser
from itertools import groupby
import matplotlib.pyplot as plt

class Friends(BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'friends.get'
    http_method = 'GET'
    param = 'fields=bdate&user_id'

    def __init__(self, userid):
        super(Friends, self).__init__()
        self.userid = userid

    # Склейка url
    def generate_url(self):
        return '{0}{1}?{2}={3}'.format(self.BASE_URL, self.method, self.param, self.userid)

    # Отправка запроса к VK API
    def _get_data(self):
        response = requests.get(self.generate_url())
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        result=[]
        current_date = datetime.datetime.now().year
        json = response.json()
        for i in json['response']:
            try:
                idate = i['bdate']
                try:
                    dt = parser.parse(idate)
                    res_date = current_date - dt.year
                    res = res_date
                    if res > 0 and res < 50:
                        result.append(res)
                except Exception:
                    pass
            except Exception:
                pass
        return result

    def execute(self):
        self.res_list = self._get_data()
        self.res_dict = self.dict_data(self._get_data())
        return self.res_dict

    def dict_data(self, data):
        res = {}
        keyfunc = lambda x: x
        data = sorted(data, key=keyfunc)
        for k, g in groupby(data, keyfunc):
            items = list(v for v in g)
            res[k] = len(items)
        return res

    def hist1(self):
        for k in sorted(self.res_dict):
            v = self.res_dict[k]
            print(k, v * '*')

    def hist2(self):
            n, bins, patches = plt.hist(self.res_list, 50, normed=1, facecolor='green', alpha=0.75)
            plt.show()