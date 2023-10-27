from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    authors = models.CharField(max_length=255)
    isbn = models.CharField(max_length=150)
    num_pages = models.IntegerField()
    publisher = models.CharField(max_length=150)
    rating_count = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return self.title
    
class ProgressBaca(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey(Book, on_delete=models.CASCADE)
    tanggal = models.DateField()
    buku_selesai = models.BooleanField(default=False)

class TargetHarian(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_buku = models.PositiveIntegerField()
    tanggal = models.DateTimeField(auto_now=True)

class AktivitasUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal = models.DateField()
    waktu_aktif = models.PositiveIntegerField(default=0)

class BukuDibaca(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey(Book, on_delete=models.CASCADE) 
    tanggal_dibaca = models.DateField(auto_now_add=True)