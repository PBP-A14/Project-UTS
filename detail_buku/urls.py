from django.urls import path
from detail_buku.views import detail_buku, submit_review, like_book

app_name = 'detail_buku'

urlpatterns = [
    path('detail_buku/<int:book_id>/', detail_buku, name='detail_buku'),
    path('detail_buku/<int:book_id>/submit_review/', submit_review, name='submit_review'),
    path('detail_buku/<int:book_id>/like/', like_book, name='like_book'),
]