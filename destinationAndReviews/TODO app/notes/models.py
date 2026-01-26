from django.db import models

from categories.models import Category


class Note(models.Model):
    class PriorityChoices(models.IntegerChoices):
        LOW = 1, 'Low'
        MEDIUM = 2, 'Medium'
        HIGH = 3, 'High'

    title = models.CharField(max_length=30)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField()
    priority = models.IntegerField(choices=PriorityChoices.choices, default=PriorityChoices.LOW)
    category = models.ForeignKey('categories.Category',
                                 on_delete=models.CASCADE,
                                 related_name='notes',
                                 blank=True,
                                 null=True)

    def __str__(self):
        return self.title
