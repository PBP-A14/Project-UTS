from django.db import models
from django.contrib.auth.models import User
from home.models import Book
    
class ProgressBaca(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal = models.DateField()
    buku_selesai = models.BooleanField(default=False)

class TargetHarian(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_buku = models.PositiveIntegerField()

class BukuDibaca(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey(Book, on_delete=models.CASCADE)
    counted = models.IntegerField(default=0)
