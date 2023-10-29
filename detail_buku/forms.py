from django import forms
from .models import BookReview, BookRating

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['review_text']

class BookRatingForm(forms.ModelForm):
    class Meta:
        model = BookRating
        fields = ['rating']

class LikeBookForm(forms.Form):
    # This form can be empty because liking doesn't require user input
    pass
