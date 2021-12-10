from django.db import models

class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    age = models.IntegerField(blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['id']