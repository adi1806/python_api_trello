import requests
from ..utils.parser_util import ConfigParser


class ApiClient:
    def __init__(self):
        fetchdata = ConfigParser().fetch_trello_data()
        self.api_key = fetchdata['api_key']
        self.token = fetchdata['token']
        self.base_url = fetchdata['base_url']
        self.card_id = fetchdata['card_id']
        self.invalid_card_id = fetchdata['invalid_card_id']
        self.id_list = fetchdata['id_list']
        self.invalid_id_list = fetchdata['invalid_id_list']
        self.id_board = fetchdata['id_board']

    def headers(self):
        return {
            'Accept': 'application/json'
        }

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        params = {
            "key": self.api_key,
            "token": self.token
        }
        headers = self.headers()
        response = requests.get(url, params=params, headers=headers)
        return response

    def post(self, endpoint, param=None):
        url = f"{self.base_url}/{endpoint}"
        params = {
            'key': self.api_key,
            'token': self.token
        }
        params.update(param)
        headers = self.headers()
        response = requests.post(url, params=params, headers=headers)
        return response

    def put(self, endpoint, param=None):
        url = f"{self.base_url}/{endpoint}"
        params = {
            'key': self.api_key,
            'token': self.token
        }
        params.update(param)
        headers = self.headers()
        response = requests.put(url, params=params, headers=headers)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        params = {
            'key': self.api_key,
            'token': self.token
        }
        headers = self.headers()
        response = requests.delete(url, params=params, headers=headers)
        return response


