from django import forms
from .models import TargetHarian

class TargetHarianForm(forms.ModelForm):
    class Meta:
        model = TargetHarian
        fields = ['tanggal', 'target_buku']
