from django.shortcuts import render
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from home.models import Book
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.

@staff_member_required
@login_required(login_url="authentication:login")
def admin_app(request):
    return render(request, "admin_app.html", {})

def show_user_json(request):
    data = User.objects.all().order_by('username')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_user_json(request):
    users = User.objects.all().order_by('username')
    return HttpResponse(serializers.serialize('json', users))

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        authors = request.POST.get("authors")
        isbn = request.POST.get("isbn")
        num_pages = request.POST.get("num_pages")
        publisher = request.POST.get("publisher")

        new_product = Book(title=title, description=description, authors=authors, 
                           isbn=isbn, num_pages=num_pages, publisher=publisher,
                           rating_count=0, rating=0.0)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == 'POST':
        book.title = request.POST.get("title-edit")
        book.description = request.POST.get("description-edit")
        book.authors = request.POST.get("authors-edit")
        book.isbn = request.POST.get("isbn-edit")
        book.num_pages = request.POST.get("num_pages-edit")
        book.publisher = request.POST.get("publisher-edit")
        book.save()
        return JsonResponse({'success': 'Book updated successfully'})
    
    data = {
        'title': book.title,
        'description': book.description,
        'authors': book.authors,
        'isbn': book.isbn,
        'num_pages': book.num_pages,
        'publisher': book.publisher,
    }
    return JsonResponse(data)

@csrf_exempt
def delete_book(request, id):
    if request.method == 'DELETE':
        book = get_object_or_404(Book, pk=id)
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully'})
    
@csrf_exempt
def delete_user(request, id):
    if request.method == 'DELETE':
        user = get_object_or_404(User, pk=id)
        user.delete()
        return JsonResponse({'message': 'Book deleted successfully'})