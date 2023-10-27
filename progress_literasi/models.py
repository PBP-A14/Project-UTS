from django.db import models
from django.contrib.auth.models import User
    
class ProgressBaca(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
