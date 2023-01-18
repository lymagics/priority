from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from parameterized import parameterized


class TestRequest(APITestCase):
    """
    Common API features test case.
    """

    URLS = {
        'users': reverse('api:users:users-list'),
        'tasks': reverse('api:tasks:tasks-list'),
    }

    @parameterized.expand([
        (URLS['users'],
         status.HTTP_200_OK),
        (URLS['tasks'],
         status.HTTP_200_OK)
    ])
    def test_response_codes(self, endpoint, expected_status_code):
        """
        Test API response codes are valid.
        """
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, expected_status_code)
