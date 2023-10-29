from django.forms import ModelForm
from .models import TargetHarian

class DailyTargetForm(ModelForm):
    class Meta:
        model = TargetHarian
        fields = ['target_buku']