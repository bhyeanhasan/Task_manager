from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PRIORITY_CHOICES = (
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High"),
)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=10,
                                choices=PRIORITY_CHOICES,
                                default="low")
    complete = models.BooleanField(default=False)
    creation_time = models.DateTimeField(blank=True,null=True)
    last_update = models.DateTimeField(auto_now=True)


class TaskImages(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='task', null=True, blank=True)
