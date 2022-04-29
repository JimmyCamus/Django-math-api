from django.test import TestCase, override_settings
import json
from rest_framework.test import APIClient

TEST_CACHE_SETTING = {
    # ...
}


class NumericalMethodsTestCase(TestCase):
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

    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_newton_raphson_method(self):
        client = APIClient()
        response = client.post(
            '/api/numericalmethods/newthon-raphson/',
            {
                'initial_point': 1.4,
                'funct': 'x**3 + 4*x**2 - 10',
                'derivate': '3*x**2 + 8*x',
                'epsilon': 0.00005,
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content),
                         {'result': 1.36523001341411})

    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_fixed_point_method(self):
        client = APIClient()
        response = client.post(
            '/api/numericalmethods/fixed-point/',
            {
                'initial_point': 1,
                'epsilon': 0.00005,
                'expression': '((10 - x**3) / 4)**(1/2)',
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content),
                         {'result': 1.3652423837188388})
