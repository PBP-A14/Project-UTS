from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Like, View, Review
from home.models import Book

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not View.objects.filter(book=book, user=request.user).exists():
        View.objects.create(book=book, user=request.user)
    context = {
        'book': book,
        'likes_count': Like.objects.filter(book=book).count(),
        'views_count': View.objects.filter(book=book).count(),
        'reviews': Review.objects.filter(book=book)
    }
    return render(request, 'detail_buku.html', context)

@csrf_exempt
@login_required
def like_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, id=book_id)
        if Like.objects.filter(book=book, user=request.user).exists():
            Like.objects.filter(book=book, user=request.user).delete()
            result = 'unliked'
        else:
            Like.objects.create(book=book, user=request.user)
            result = 'liked'
        return JsonResponse({'result': result})

@csrf_exempt
@login_required
def add_review(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        review_text = request.POST.get('review')
        book = get_object_or_404(Book, id=book_id)
        Review.objects.create(book=book, user=request.user, review=review_text)
        return JsonResponse({'result': 'review added'})
