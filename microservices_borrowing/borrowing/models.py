from django.db import models

class Borrowing(models.Model):
    id = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['id']