from django.urls import path
from authentication.views import register, login_user, logout_user, login, logout

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('mobile-login/', login, name='login_flutter'),
    path('mobile-logout/', logout, name='logout_flutter'),
]