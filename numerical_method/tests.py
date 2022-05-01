from django.test import TestCase, override_settings
import json
from rest_framework.test import APIClient

TEST_CACHE_SETTING = {
    # ...
}


class NumericalMethodsTestCase(TestCase):
    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_bisection_method_converges(self):
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
    def test_bisection_method_diverges(self):
        client = APIClient()
        response = client.post(
            '/api/numericalmethods/bisection/',
            {
                'min': -1.0,
                'max': -2.0,
                'epsilon': 0.00005,
                'expression': '(x)**(0.5)'
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content),
                         {'error': "There is not a solution"})

    def test_bisection_method_bad_request(self):
        client = APIClient()
        response = client.post(
            '/api/numericalmethods/bisection/',
            {
                'min': "a",
                'epsilon': 0.00005,
                'expression': '(x)**(0.5)'
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content),
                         {'min': ['A valid number is required.'], 'max': ['This field is required.']})

    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_newton_raphson_method_converges(self):
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
    def test_newton_raphson_method_diverges(self):
        client = APIClient()
        response = client.post(
            '/api/numericalmethods/newthon-raphson/',
            {
                'initial_point': -1.4,
                'funct': '(x)**(0.5)',
                'derivate': 'x/x**0.5',
                'epsilon': 0.00005,
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content),
                         {'error': 'There is not a solution'})

    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_newton_raphson_method_bad_request(self):
        client = APIClient()
        response = client.post(
            '/api/numericalmethods/newthon-raphson/',
            {
                'funct': 2,
                'derivate': 'x/x**0.5',
                'epsilon': 0.00005,
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content),
                         {'initial_point': ['This field is required.']})

    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_fixed_point_method_converges(self):
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

    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_fixed_point_method_diverges(self):
        client = APIClient()
        response = client.post(
            '/api/numericalmethods/fixed-point/',
            {
                'initial_point': 1,
                'epsilon': 0.00005,
                'expression': '(-4*x**2+10)**(1/3)',
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content),
                         {'error': 'There is not a solution'})

    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_fixed_point_method_bad_request(self):
        client = APIClient()
        response = client.post(
            '/api/numericalmethods/fixed-point/',
            {
                'initial_point': 'a',
                'expression': '(-4*x**2+10)**(1/3)',
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content),
                         {'initial_point': ['A valid number is required.'], 'epsilon': ['This field is required.']})
