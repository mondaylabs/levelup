from django.test import override_settings
from django.urls import reverse
from toolkit.tests.base_test import BaseTestCase
from users.tests.constants import USER_TOKEN


@override_settings(EMAIL_BACKEND='toolkit.utils.email.TestEmailBackend')
class UserTest(BaseTestCase):
    auth_token = USER_TOKEN
    fixtures = ('users_and_tokens.yaml',)

    def test_list(self):
        response = self.client.get(reverse('users:user-list'))
        self.assertEqual(200, response.status_code, response.data)
        self.assertEqual(4, response.data['count'], response.data)
        self.assertEqual(1, response.data['results'][0]['id'], response.data)
        self.assertEqual(2, response.data['results'][1]['id'], response.data)
        self.assertEqual(3, response.data['results'][2]['id'], response.data)
        self.assertEqual(4, response.data['results'][3]['id'], response.data)

    def test_search(self):
        response = self.client.get(reverse('users:user-list') + '?search=Angelina')
        self.assertEqual(200, response.status_code, response.data)
        self.assertEqual(1, response.data['count'], response.data)
        self.assertEqual(1, response.data['results'][0]['id'], response.data)

    def test_settings(self):
        response = self.client.patch(reverse('users:user-settings'), {
            'email': 'test@gmail.com',
            'first_name': 'Arnold',
            'last_name': 'Swarchenegger',
        })
        self.assertEqual(200, response.status_code, response.data)

    def test_change_password(self):
        response = self.client.put(reverse('users:change-password'), {'old_password': 'incorrect'})
        self.assertEqual(400, response.status_code, response.data)
        self.assertEqual('Incorrect old password.', response.data['old_password'][0], response.data)

        response = self.client.put(reverse('users:change-password'), {
            'old_password': 'password',
            'new_password': 'just.new.password'
        })
        self.assertEqual(200, response.status_code, response.data)
