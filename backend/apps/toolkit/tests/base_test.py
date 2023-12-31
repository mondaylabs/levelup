import json
from pprint import pprint
from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):
    def setUp(self):
        if hasattr(self, 'auth_token'):
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.auth_token)

    def dump(self, response):
        print('-' * 40)
        print('Response:', response.status_code)
        pprint(json.loads(json.dumps(response.data)))
        print('-' * 40)
