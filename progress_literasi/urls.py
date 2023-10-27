from django.urls import path
from . import views

app_name = 'progress_literasi'

urlpatterns = [
    path('set-target/', views.set_target, name='set_target'),
    path('progress/', views.progress, name='progress'),
]