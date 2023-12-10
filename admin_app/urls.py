from django.urls import path
from admin_app.views import admin_app, show_user_json, get_user_json, get_log_json, add_book, edit_book, delete_book, delete_user, get_username_json, get_book_json, delete_cookie, update_cookie, create_book_flutter

app_name = 'admin_app'

urlpatterns = [
    path('get_book/<str:q>/', get_book_json, name='get_book_json'),
    path('user_json/', show_user_json, name='show_user_json'),
    path('get_user/', get_user_json, name='get_user_json'),
    path('get_username/<int:id>/', get_username_json, name='get_username_json'),
    path('get_log/<int:id>/', get_log_json, name='get_log_json'),
    path('admin_app/', admin_app, name='admin_app'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:id>/', edit_book, name='edit_book'),
    path('delete_book/<int:id>/', delete_book, name='delete_book'),
    path('delete_user/<int:id>/', delete_user, name='delete_user'),
    path('delete_cookie/', delete_cookie, name='delete_cookie'),
    path('update_cookie/', update_cookie, name='update_cookie'),
    path('create_flutter/', create_book_flutter, name='create_book_flutter'),
]