from django.test import TestCase, override_settings
import json
from rest_framework.test import APIClient

TEST_CACHE_SETTING = {
    # ...
}


class FundamentalsTestCase(TestCase):
    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_derivate(self):
        client = APIClient()
        response = client.post(
            '/api/fundamentals/derivate/',
            {
                'funct': 'x**2'
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content), {'derivate': '2*x'})

    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_derivate_bad_request(self):
        client = APIClient()
        response = client.post(
            '/api/fundamentals/derivate/',
            {},
            format='multipart'
        )

        self.assertEqual(json.loads(response.content), {'funct': ['This field is required.']})

    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_integrate(self):
        client = APIClient()
        response = client.post(
            '/api/fundamentals/integrate/',
            {
                'funct': 'x**2'
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content), {'integrate': 'x**3/3'})

    @override_settings(CACHES=TEST_CACHE_SETTING)
    def test_integrate_bad_request(self):
        client = APIClient()
        response = client.post(
            '/api/fundamentals/integrate/',
            {
            },
            format='multipart'
        )

        self.assertEqual(json.loads(response.content), {'funct': ['This field is required.']})
