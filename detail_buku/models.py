from django.db import models
from django.conf import settings
from home.models import Book
from django.contrib.auth.models import User

class Like(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'user')

class View(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='views')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()

    class Meta:
        unique_together = ('book', 'user')
