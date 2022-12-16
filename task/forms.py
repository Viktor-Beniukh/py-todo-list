from django import forms

from task.models import Task, Tag


class TaskForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"
