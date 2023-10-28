from django.urls import path
from . import views

app_name = 'my_profile'

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
]
