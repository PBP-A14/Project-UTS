from django.urls import path
from . import views

app_name = 'progress_literasi'

urlpatterns = [
    path('buku-list/', views.buku_list, name='buku_list'),
    path('history_buku/', views.history_buku, name='history_buku'),
    path('set-target/', views.set_target, name='set_target'),
    path('progress/', views.progress, name='progress'),
    path('track_user_activity/', views.track_user_activity, name='track_user_activity'),
]