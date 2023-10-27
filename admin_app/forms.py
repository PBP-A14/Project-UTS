from django.forms import ModelForm
from home.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "authors", "isbn", "num_pages", "publisher"]