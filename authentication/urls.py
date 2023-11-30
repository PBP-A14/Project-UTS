from django.urls import path
from authentication.views import register, login_user, logout_user, login_mobile, logout_mobile

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('mobile-login/', login_mobile, name='login_flutter'),
    path('mobile-logout/', logout_mobile, name='logout_flutter'),
]