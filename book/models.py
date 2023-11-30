from django.db import models

class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    isbn = models.TextField(null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    rating_count = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
