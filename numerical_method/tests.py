from django.test import TestCase, override_settings
import json
from rest_framework.test import APIClient

TEST_CACHE_SETTING = {
    # ...
}


class FundamentalsTestCase(TestCase):
    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_bisection_method(self):
        client = APIClient()
        response = client.post(
            '/api/numericalmethods/bisection/',
            {
                'min': 1.0,
                'max': 2.0,
                'epsilon': 0.00005,
                'expression': 'x**3 +4*x**2 - 10'
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content),
                         {'result': 1.365203857421875})
