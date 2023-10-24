from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Book

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_book_json(request):
    book_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book_item))