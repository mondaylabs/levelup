from django.urls import reverse
from toolkit.tests.base_test import BaseTestCase
from users.tests.constants import USER_TOKEN


class GeneralTest(BaseTestCase):
    fixtures = ('users_and_tokens.yaml',)

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + USER_TOKEN)

    def test_general(self):
        response = self.client.get(reverse('core:general'))
        self.assertEqual(response.status_code, 200)
