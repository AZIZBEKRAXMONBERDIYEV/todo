from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User


class TaskList(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)

    def test_get(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'id': 1, 'username': 'testuser', 'tasks': []})

    def test_post(self):
        response = self.client.post('/api/tasks/', {'title': 'test task'}, format='json')
        self.assertEqual(response.status_code, 201)
        # self.assertEqual(response.data, {'id': 1, 'username': 'testuser', 'tasks': [{'id': 1, 'title': 'test task', 'description': '', 'completed': False}]})
