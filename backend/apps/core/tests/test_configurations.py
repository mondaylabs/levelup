from django.urls import reverse

from toolkit.tests.base_test import BaseTestCase


class ConfigurationsTest(BaseTestCase):
    def test_configurations(self):
        response = self.client.get(reverse('core:configurations'))
        self.assertEqual(200, response.status_code, response.data)
