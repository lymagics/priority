from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class TestUserAPI(APITestCase):
    """
    User API test case.
    """

    SETUP_DATA = {
        'username': 'alice',
        'email': 'alice@example.com',
        'password': 'dog'
    }

    VALID_DATA = {
        'username': 'bob',
        'email': 'bob@example.com',
        'password': 'cat'
    }

    INVALID_DATA = {
        'username': 'alice',
        'email': 'alice@example.com',
    }

    INVALID_DATA_MESSAGES = {
        'username': ['A user with that username already exists.'],
        'email': ['A user with that email already exists.'],
        'password': ['This field is required.'],
    }

    UPDATE_DATA = {
        'username': 'chloe',
        'email': 'chloe@example.com',
        'about_me': 'Python developer.'
    }

    URL = reverse('api:users:users-list')
    STATUS_CREATED = status.HTTP_201_CREATED
    STATUS_SUCCESS = status.HTTP_200_OK
    STATUS_FAILED = status.HTTP_400_BAD_REQUEST

    def setUp(self):
        self.user = User.objects.create_user(**self.SETUP_DATA)
        self.URL_DETAIL = reverse('api:users:users-detail', kwargs={'pk': self.user.pk})

    def test_creating_user(self):
        """
        Test user creation flow with valid data.
        """
        response = self.client.post(self.URL, self.VALID_DATA)
        self.assertEqual(response.status_code, self.STATUS_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_not_creating_user(self):
        """
        Test user creation flow with invalid data.
        """
        response = self.client.post(self.URL, self.INVALID_DATA)
        self.assertEqual(response.status_code, self.STATUS_FAILED)

        errors = response.json()
        self.assertEqual(errors, self.INVALID_DATA_MESSAGES)

    def test_retrieving_user(self):
        """
        Test user retrieving flow.
        """
        response = self.client.get(self.URL_DETAIL)
        self.assertEqual(response.status_code, self.STATUS_SUCCESS)

        data = response.json()
        self.assertEqual(data['username'], self.user.username)
        self.assertEqual(data['avatar_url'], self.user.avatar_url)
        self.assertEqual(data['about_me'], self.user.about_me)

    def test_retrieving_list_users(self):
        """
        Test user list retrieving flow.
        """
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, self.STATUS_SUCCESS)

        data = response.json()
        self.assertTrue('count' in data)
        self.assertEqual(data['count'], User.objects.count())

    def test_updating_user(self):
        """
        Test user updating flow.
        """
        self._provide_authentication()
        response = self.client.put(self.URL_DETAIL, self.UPDATE_DATA)
        self.assertEqual(response.status_code, self.STATUS_SUCCESS)

        self.user.refresh_from_db()
        data = response.json()
        self.assertEqual(data['username'], self.user.username)
        self.assertEqual(data['about_me'], self.user.about_me)

    def _provide_authentication(self):
        """
        Provide token authentication for test requests.
        """
        token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
