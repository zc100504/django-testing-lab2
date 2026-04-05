from django.test import TestCase
from .models import Task
from django.urls import reverse
from unittest.mock import patch

class MockTest(TestCase):

    @patch('tasks.models.Task.objects.create')
    def test_mock_create(self, mock_create):
        mock_create.return_value.title = "Mock Task"
        task = mock_create(title="Mock Task")
        self.assertEqual(task.title, "Mock Task")

class TaskModelTest(TestCase):

    def test_create_task(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.completed)

class TaskViewTest(TestCase):

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class TaskAPITest(TestCase):

    def test_api_returns_tasks(self):
        Task.objects.create(title="API Task")
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "API Task")