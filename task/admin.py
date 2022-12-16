from django.contrib import admin

from task.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_time", "deadline", "marks")
    list_filter = ("created_time", "marks")
    search_fields = ("content",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
