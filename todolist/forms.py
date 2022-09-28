from asyncio import Task
from django.forms import ModelForm
from todolist.models import TaskToDoList

class TaskForm(ModelForm):
    class Meta:
        model = TaskToDoList
        fields = ['task_title', 'task_desc']