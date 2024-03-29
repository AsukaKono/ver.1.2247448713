from django.db import models
from django.db.models import CASCADE


class TodoList(models.Model):
    title = models.CharField(null=False, max_length=255, default='')
    description = models.CharField(null=False, max_length=1000, default='')

    def __str__(self):
        return f'{self.id}. {self.title}'


class Todo(models.Model):
    title = models.CharField(null=False, max_length=100, default='')
    description = models.TextField(null=False, max_length=1000, default='')
    due_date = models.DateField(null=False)
    status = models.BooleanField(default=False, blank=True, null=True)
    category = models.ForeignKey(TodoList, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'{self.id}. {self.title}'