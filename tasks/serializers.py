from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title",
                  "description",
                  "due_date",
                  "priority",
                  "complete",
                  "creation_time",
                  "last_update",
                  ]
