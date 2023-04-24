from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
    def test_add_task(self):
        url = reverse("add_task")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        url = reverse("delete_task", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
