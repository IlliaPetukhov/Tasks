from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.content}, {self.created_at}"

    def formatted_created_at(self):
        print(self.created_at)
        if self.created_at:
            return self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return "Date not available"
