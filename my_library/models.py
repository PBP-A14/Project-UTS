from django.contrib.auth.models import User
from django.db import models
# from details_buku import Book

# Create your models here.
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    finished_reading = models.BooleanField(default=False)