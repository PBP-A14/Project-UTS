from django.urls import path
from home.views import home
from home.views import show_json, get_book_json

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('json/', show_json, name='show_json'),
    path('get_book/', get_book_json, name='get_book_json'),
]