from django.urls import path
from . import views

app_name = 'detail_buku'

urlpatterns = [
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('like_book/', views.like_book, name='like_book'),
    path('add_review/', views.add_review, name='add_review'),
]
