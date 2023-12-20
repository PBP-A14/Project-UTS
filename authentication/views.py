from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from my_profile.models import ReadingHistory

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    user = request.user
    try:
        reading_history = ReadingHistory.objects.get(user=user)
        reading_history.delete()
    except ReadingHistory.DoesNotExist:
        pass
    logout(request)
    return redirect('home:home')

# Method untuk flutter
@csrf_exempt
def login_mobile(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            print(request.session.session_key)
            if username == 'masbepe' or username == 'admin' or user.is_superuser:
                is_admin = True
            else:
                is_admin = False
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "user_id":user.pk,
                "status": True,
                "is_admin": is_admin,
                "message": "Sign in success!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Incorrect username or password."
        }, status=401)
    
@csrf_exempt
def register_mobile(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return JsonResponse({
            "username": user.username,
            "status": True,
            "message": "Sign up success!"
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Sign up failed."
        }, status=401)
    
@csrf_exempt
def logout_mobile(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)