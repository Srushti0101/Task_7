from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=PRIORITY, default='Medium')
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['done', '-id']

    def __str__(self):
        return f"{self.title} ({self.user.username})"