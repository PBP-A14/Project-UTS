from django.urls import path
from home.views import home
from home.views import show_json, get_book_json, search_book, sort_book, search, sort_az, sort_za

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('json/', show_json, name='show_json'),
    path('get_book/', get_book_json, name='get_book_json'),
    path('search_book/', search_book, name='search_book'),
    path('sort_book/', sort_book, name='sort_book'),
    path('search/<str:query>/', search, name='search'),
    path('json/a-z/', sort_az, name='sort_az'),
    path('json/z-a/', sort_za, name='sort_za'),
]