from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model to represent a Book
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    synopsis = models.TextField()
    likes = models.IntegerField(default=0)\
    
    def __str__(self):
        return self.title

# Model to track Book Views
class BookView(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    viewed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now=True)

# Model to track Book Likes
class BookLike(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)

# Model for Book Reviews
class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()

# Model for Book Ratings
class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title}"
