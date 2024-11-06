# app/tests.py
from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title="Test Task")
        self.assertTrue(isinstance(task, Task))
        self.assertEqual(task.__str__(), task.title)

