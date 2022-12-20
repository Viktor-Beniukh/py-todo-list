from django.test import TestCase
from django.urls import reverse

from task.models import Tag, Task

MAIN_PAGE_URL = reverse("task:index")
TAG_PAGE_URL = reverse("task:tag-list")
PAGINATION = 3


class TagListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="shop")

    def test_tag_page_url_exists_at_desired_location(self):
        response = self.client.get("/tags/")
        self.assertEqual(response.status_code, 200)

    def test_tag_pag_uses_correct_template(self):
        response = self.client.get(TAG_PAGE_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task/tag_list.html")


class TaskTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        number_of_task = 15

        for task_num in range(number_of_task):
            Task.objects.create(
                content=f"'Buy a car' - {task_num}",
                created_time=f"'2022-01-01 15:00' - {task_num}",
            )

    def test_main_page_url_exists_at_desired_location(self):
        response = self.client.get(MAIN_PAGE_URL)

        self.assertEqual(response.status_code, 200)

    def test_main_page_uses_correct_template(self):
        response = self.client.get(MAIN_PAGE_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task/index.html")

    def test_main_page_paginated_correctly(self):
        response = self.client.get(MAIN_PAGE_URL)

        self.assertEqual(
            len(response.context["page_obj"]), PAGINATION
        )
