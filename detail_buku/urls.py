from django.urls import path
from . import views

app_name = 'detail_buku'

urlpatterns = [
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/like_book/', views.like_book, name='like_book'),
    path('book/<int:book_id>/add_review/', views.add_review, name='add_review'),
    path('book/<int:book_id>/give_rating/', views.give_rating, name='give_rating'),
    path('book/<int:book_id>/give_rating_flutter/', views.give_rating_flutter, name='give_rating_flutter'),
    path('book/json/', views.show_json, name='show_json'),
]
