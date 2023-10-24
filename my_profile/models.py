from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reading_list = models.ManyToManyField('home.Book', related_name='readers', blank=True)
    history_bacaan = models.ManyToManyField('home.Book', related_name='readers_history', blank=True)
    progress_literasi = models.PositiveIntegerField(default=0)