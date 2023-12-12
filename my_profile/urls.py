from django.urls import path
from . import views

app_name = 'my_profile'

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('get_reading_history_json/', views.get_reading_history_json, name='get_reading_history_json'),
    path('json/', views.get_reading_history, name='json'),
    path('change_password/', views.change_password, name='change_password'), 
]
