from django import forms

from task.models import Task, Tag


class TaskForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"},
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags", "is_marks")
