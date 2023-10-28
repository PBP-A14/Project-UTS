from django.db import models

class Book (models.Model):

    title = models.CharField(("title"), max_length=255)
    description = models.TextField(("description"))
    authors = models.CharField(("authors"), max_length=255)
    isbn = models.CharField(("isbn"), max_length=150)
    num_pages = models.IntegerField(("number of pages"))
    publisher = models.CharField(("publisher"), max_length=150)
    rating_count = models.IntegerField(("rating count"))
    rating = models.FloatField(("rating"))
