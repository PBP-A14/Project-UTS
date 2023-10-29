from django.urls import path
from detail_buku.views import detail_buku, submit_review, like_book, add_to_bookmarks

app_name = 'detail_buku'

urlpatterns = [
    path('book/<int:book_id>/', detail_buku, name='detail_buku'),
    path('book/<int:book_id>/submit_review/', submit_review, name='submit_review'),
    path('book/<int:book_id>/like/', like_book, name='like_book'),
    path('book/<int:book_id>/add_bookmark/', add_to_bookmarks, name='add_to_bookmarks'),
]