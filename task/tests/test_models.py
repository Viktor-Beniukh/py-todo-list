from django.test import TestCase

from task.models import Task, Tag


class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Task.objects.create(
            content="Buy a car",
            created_time="2022-01-01 15:00"
        )

    def test_task_str(self):
        task = Task.objects.get(id=1)

        self.assertEqual(
            str(task),
            f"{task.content}: {task.created_time}"
        )

    def test_content_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field("content").max_length

        self.assertEqual(max_length, 255)


class TagModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(
            name="home",
        )

    def test_tag_str(self):
        tag = Tag.objects.get(id=1)

        self.assertEqual(str(tag), f"{tag.name}")

    def test_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field("name").max_length

        self.assertEqual(max_length, 255)
