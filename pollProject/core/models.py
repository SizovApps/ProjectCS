from django.db import models
from datetime import datetime


class Poll(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ('-date', 'title')