from email.policy import default
from time import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TaskToDoList(models.Model):
    task_user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_date = models.DateTimeField(default=timezone.now)
    task_title = models.CharField(max_length=255)
    task_desc = models.TextField()