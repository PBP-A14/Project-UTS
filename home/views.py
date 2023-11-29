from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book

def home(request):
    return render(request, "home.html", {})

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_book_json(request):
    book_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book_item))

def search_book(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    data = [{'fields': {
        'title': book.title,
        'rating': book.rating,
        'isbn': book.isbn,
        'description': book.description,
        'authors': book.authors,
        'num_pages': book.num_pages,
        'publisher': book.publisher,
        'rating_count': book.rating_count,
    }} for book in books]
    return JsonResponse(data, safe=False)

def sort_book(request):
    sort_order = request.GET.get('sort', 'none')
    if sort_order == 'a_z':
        books = Book.objects.order_by('title')
    elif sort_order == 'z_a':
        books = Book.objects.order_by('-title')
    else:
        books = Book.objects.all()
    data = [{'fields': {
        'title': book.title,
        'rating': book.rating,
        'isbn': book.isbn,
        'description': book.description,
        'authors': book.authors,
        'num_pages': book.num_pages,
        'publisher': book.publisher,
        'rating_count': book.rating_count,
    }} for book in books]
    return JsonResponse(data, safe=False)

# Method untuk flutter
def search(request, query):
    books = Book.objects.filter(title__icontains=query)
    data = [{'fields': {
        'title': book.title,
        'rating': book.rating,
        'isbn': book.isbn,
        'description': book.description,
        'authors': book.authors,
        'num_pages': book.num_pages,
        'publisher': book.publisher,
        'rating_count': book.rating_count,
    }} for book in books]
    return JsonResponse(data, safe=False)

def sort_az(request):
    data = Book.objects.order_by('title')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def sort_za(request):
    data = Book.objects.order_by('-title')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")