from django.urls import path
from admin_app.views import admin_app, show_user_json, get_user_json, add_book, edit_book, delete_book, delete_user

app_name = 'admin_app'

urlpatterns = [
    path('user_json/', show_user_json, name='show_user_json'),
    path('get_user/', get_user_json, name='get_user_json'),
    path('admin_app/', admin_app, name='admin_app'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:id>/', edit_book, name='edit_book'),
    path('delete_book/<int:id>/', delete_book, name='delete_book'),
    path('delete_user/<int:id>/', delete_user, name='delete_user')
]