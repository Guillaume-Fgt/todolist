from django.test import TestCase
from django.urls import reverse
from todoapp.models import Task


def create_task(name: str, priority: str) -> Task:
    return Task.objects.create(name=name, priority=priority)


class TestViews(TestCase):
    def test_index_one_task(self) -> None:
        task = create_task("pay bills", "1- Important")
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["tasks"], [task])

    def test_index_no_task(self) -> None:
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tasks!!")

    def test_add_task(self) -> None:
        url = reverse("add_task")
        self.client.post(url, {"task": "learn javascript", "priority": "2 - Medium"})
        self.assertEqual(
            Task.objects.get(name="learn javascript").name, "learn javascript"
        )

    def test_delete_task(self) -> None:
        create_task("learn typescript", "2 - Medium")
        self.assertIsInstance(Task.objects.get(name="learn typescript"), Task)
        url = reverse("delete_task", kwargs={"pk": 1})
        self.client.delete(url)
        self.assertRaises(Task.DoesNotExist, Task.objects.get, name="learn typescript")
