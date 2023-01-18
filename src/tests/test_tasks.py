from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from tasks.models import Task
from users.models import User


class TestTasksAPI(APITestCase):
    """
    Task API test case.
    """

    SETUP_USER_DATA = {
        'username': 'bob',
        'email': 'bob@example.com',
        'password': 'dog'
    }

    SETUP_TASK_DATA = {
        'description': 'Make sandwich',
        'priority': 'M'
    }

    VALID_DATA = {
        'description': 'Do 10 push-ups',
        'priority': 'H'
    }

    INVALID_DATA = {
        'priority': 'G'
    }

    INVALID_DATA_MESSAGES = {
        'description': ['This field is required.'],
        'priority': ['\"G\" is not a valid choice.'],
    }

    UPDATE_DATA = {
        'description': 'Make 10 sandwiches',
        'priority': 'H'
    }

    URL = reverse('api:tasks:tasks-list')
    STATUS_CREATED = status.HTTP_201_CREATED
    STATUS_SUCCESS = status.HTTP_200_OK
    STATUS_FAILED = status.HTTP_400_BAD_REQUEST
    STATUS_DELETED = status.HTTP_204_NO_CONTENT

    def setUp(self):
        self.user = User.objects.create_user(**self.SETUP_USER_DATA)
        self.task = Task.objects.create(user=self.user, **self.SETUP_TASK_DATA)
        self.URL_DETAIL = reverse('api:tasks:tasks-detail', kwargs={'pk': self.task.pk})

    def test_creating_task(self):
        """
        Test task creation flow with valid data.
        """
        self._provide_authentication()

        response = self.client.post(self.URL, self.VALID_DATA)
        self.assertEqual(response.status_code, self.STATUS_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_not_creating_task(self):
        """
        Test task creation flow with invalid data.
        """
        self._provide_authentication()

        response = self.client.post(self.URL, self.INVALID_DATA)
        self.assertEqual(response.status_code, self.STATUS_FAILED)

        errors = response.json()
        self.assertEqual(errors, self.INVALID_DATA_MESSAGES)

    def test_retrieving_task(self):
        """
        Test task retrieving flow.
        """
        response = self.client.get(self.URL_DETAIL)
        self.assertEqual(response.status_code, self.STATUS_SUCCESS)

        data = response.json()
        self.assertEqual(data['description'], self.task.description)
        self.assertEqual(data['priority'], self.task.priority)
        self.assertEqual(data['is_done'], self.task.is_done)
        self.assertEqual(data['user']['username'], self.task.user.username)

    def test_retrieving_list_tasks(self):
        """
        Test task list retrieving flow.
        """
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, self.STATUS_SUCCESS)

        data = response.json()
        self.assertTrue('count' in data)
        self.assertEqual(data['count'], Task.objects.count())

    def test_updating_task(self):
        """
        Test task updating flow.
        """
        self._provide_authentication()

        response = self.client.put(self.URL_DETAIL, self.UPDATE_DATA)
        self.assertEqual(response.status_code, self.STATUS_SUCCESS)

        self.task.refresh_from_db()
        data = response.json()
        self.assertEqual(data['description'], self.task.description)
        self.assertEqual(data['priority'], self.task.priority)

    def test_deleting_task(self):
        """
        Test task deleting flow.
        """
        self._provide_authentication()

        response = self.client.delete(self.URL_DETAIL)
        self.assertEqual(response.status_code, self.STATUS_DELETED)
        self.assertEqual(Task.objects.count(), 0)

    def _provide_authentication(self):
        """
        Provide token authentication for test requests.
        """
        token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
