from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect

from task.forms import TaskForm
from task.models import Task, Tag


def index(request):
    task_list = Task.objects.prefetch_related("tags")
    paginator = Paginator(task_list, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "task_list": task_list,
        "page_obj": page_obj,
    }

    return render(request, "task/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    template_name = "task/tag_list.html"
    context_object_name = "tag_list"
    queryset = Tag.objects.all().order_by("name")


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "task/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "task/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "task/tag_confirm_delete.html"
    success_url = reverse_lazy("task:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "task/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "task/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task/task_confirm_delete.html"
    success_url = reverse_lazy("task:index")


def change_task_status(request, pk, status):
    task = Task.objects.get(pk=pk)
    task.is_marks = status
    task.save()
    return redirect("task:index")
