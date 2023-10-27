from django.urls import path
from . import views

app_name = 'progress_literasi'

urlpatterns = [
    path('set-target/', views.set_target, name='set_target'),
    path('progress/', views.progress, name='progress'),
    path('track_user_activity/', views.track_user_activity, name='track_user_activity'),
    path('realtime_data/', views.realtime_data, name='realtime_data'),
]