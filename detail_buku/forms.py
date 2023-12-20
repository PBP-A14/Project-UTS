from django import forms
from detail_buku.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']

class RatingForm(forms.Form):
    rating = forms.FloatField(label='Rating', min_value=1, max_value=5)