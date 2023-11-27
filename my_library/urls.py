from django.urls import path
from . import views

app_name = 'my_library'
urlpatterns = [
    path('my_library/', views.my_library, name='my_library'),
    path('remove_bookmark/<int:bookmark_id>/', views.remove_bookmark, name='remove_bookmark'),
    path('mark_as_read/<int:bookmark_id>/', views.mark_as_read, name='mark_as_read'),
]