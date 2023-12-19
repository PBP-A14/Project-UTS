from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Like, View, Review, Rating
from home.models import Book
from django.db import IntegrityError
from .forms import ReviewForm, RatingForm
from django.urls import reverse
from django.contrib import messages
from django.forms.models import model_to_dict

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not View.objects.filter(book=book, user=request.user).exists():
        View.objects.create(book=book, user=request.user)
    context = {
        'book': book,
        'book_id': book_id,
        'likes_count': Like.objects.filter(book=book).count(),
        'views_count': View.objects.filter(book=book).count(),
        'reviews': Review.objects.filter(book=book)
    }
    return render(request, 'detail_buku.html', context)

@login_required
def like_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        user = request.user

        like, created = Like.objects.get_or_create(book=book, user=user)

        if not created:
            like.delete()
            result = 'unliked'
        else:
            result = 'liked'

        likes_count = Like.objects.filter(book=book).count()

        return JsonResponse({'result': result, 'likes_count': likes_count})

def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return HttpResponseRedirect(reverse('detail_buku:book_detail', args=[str(book_id)]))
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

def give_rating(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user = request.user

    # Check if the user has already given a rating for this book
    if Rating.objects.filter(book=book, user=user).exists():
        messages.error(request, "You have already given a rating for this book.")
        return redirect('detail_buku:book_detail', book_id=book_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']

            # Calculate the updated rating
            new_rating = ((book.rating * book.rating_count) + rating) / (book.rating_count + 1)

            # Update the book instance in the database
            book.rating = new_rating
            book.rating_count += 1
            book.save()

            # Save the user's rating to prevent them from rating again
            Rating.objects.create(book=book, user=user, rating=rating)

            messages.success(request, "Rating added successfully.")
            return HttpResponseRedirect(reverse('detail_buku:book_detail', args=[str(book_id)]))
        else:
            # Form is not valid, return error message
            messages.error(request, "Invalid rating value.")
            return redirect('detail_buku:give_rating', book_id=book_id)
    else:
        form = RatingForm()
        return render(request, 'give_rating.html', {'form': form, 'book_id': book_id})

def show_json(request):
    # Fetch all reviews
    reviews = Review.objects.all()

    # Serialize the reviews data to JSON
    reviews_data = [{'book_id': review.book.id, 'user': review.user.username, 'review': review.review} for review in reviews]

    # Serialize the likes data to JSON
    likes_data = [{'book_id': like.book.id, 'user': like.user.username, 'likes_count': like.likes_count} for like in Like.objects.all()]

    # Serialize the views data to JSON
    views_data = [{'book_id': view.book.id, 'user': view.user.username} for view in View.objects.all()]

    # Serialize the ratings data to JSON
    ratings_data = [{'book_id': rating.book.id, 'user': rating.user.username, 'rating': rating.rating} for rating in Rating.objects.all()]

    return JsonResponse({'reviews': reviews_data, 'likes': likes_data, 'views': views_data, 'ratings': ratings_data})
