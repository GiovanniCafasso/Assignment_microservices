from django.db import models

class Borrowing(models.Model):
    id_book = models.IntegerField(blank=False)
    id_customer = models.IntegerField(blank=False)

    class Meta:
        ordering = ['id']