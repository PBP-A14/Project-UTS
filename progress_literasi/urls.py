from django.urls import path
from . import views

app_name = 'progress_literasi'

urlpatterns = [
    path('set-target/', views.set_target, name='set_target'),
    path('progress/', views.progress, name='progress'),
<<<<<<< HEAD
    path('get_text_progress/',views.get_text_progress, name='get_text_progress'),
=======
>>>>>>> 949a3c6412f47566f6c500ba442255e240121f9b
    path('update_target/', views.update_target, name='update_target'),
    path('reset_target/', views.reset_target, name='reset_target'),
    path('read-book/<int:book_id>/', views.read_book, name='read_book'),
]