from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Log(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    date_added = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)
    description = models.TextField()