from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# from my_library.models import Bookmark
from .models import Book, BookView, BookLike, BookReview, BookBookmark, BookRating, Bookmark, Review
from .forms import BookReviewForm, LikeBookForm, BookmarkBookForm

# Create your views here.
def detail_buku(request, book_id):
    # Get the specific book based on its ID or any other identifier
    book = get_object_or_404(Book, pk=book_id)

    # Get the number of views for this book
    view_count = BookView.objects.filter(book=book).count()

    # Get the number of likes for this book
    like_count = BookLike.objects.filter(book=book).count()

    # Get the reviews for this book
    # reviews = BookReview.objects.filter(book=book)
    reviews = Review.objects.filter(book=book).order_by('-created_at')

    # Get the bookmarks for this book
    bookmarks = BookBookmark.objects.filter(book=book)

    # Get the average rating for this book
    ratings = BookRating.objects.filter(book=book)
    total_ratings = ratings.count()
    if total_ratings > 0:
        average_rating = sum(rating.rating for rating in ratings) / total_ratings
    else:
        average_rating = 0

    context = {
        'book': book,
        'view_count': view_count,
        'like_count': like_count,
        'reviews': reviews,
        'bookmarks': bookmarks,
        'average_rating': average_rating,
    }

    return render(request, 'detail_buku.html', context)

@login_required
def submit_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.reviewed_by = request.user
            review.save()
            return redirect('detail_buku', book_id=book_id)
    else:
        form = BookReviewForm()
    
    return render(request, 'submit_review.html', {'form': form})

def like_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        # Process the like request
        book.likes += 1
        book.save()
        return redirect('detail_buku', book_id=book_id)
    
    like_count = book.likes

    return render(request, 'detail_buku.html', {'book': book, 'like_count': like_count})

@login_required
def add_to_bookmarks(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        # Check if the user has already bookmarked the book
        bookmark, created = Bookmark.objects.get_or_create(user=request.user, book=book)
        if created:
            # The book was successfully bookmarked
            return redirect('detail_buku', book_id=book_id)

    # Handle the case where the user has already bookmarked the book or it's not a POST request
    return redirect('detail_buku', book_id=book_id)
