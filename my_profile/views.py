from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from my_profile.models import UserProfile, ReadingHistory
from progress_literasi.models import BukuDibaca    
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required
def user_profile(request):
    # Mengambil objek UserProfile terkait dengan pengguna saat ini
    user = request.user

    reading_history, created = ReadingHistory.objects.get_or_create(user=user)

    try:
        user_profile = UserProfile.objects.get(user=request.user)
        target_buku = user_profile.target_buku
    except ObjectDoesNotExist:
        user_profile = None
        target_buku = 0

    book_count = reading_history.books.count()
    
    if target_buku > 0:
        if book_count >= target_buku:
            percentage_complete = 100
        else:
            percentage_complete = (book_count * 100) / target_buku
    else:
        percentage_complete = 0

    context = {
        'target_buku': target_buku,
        'reading_history': reading_history,
        'percentage_complete': percentage_complete,
        'book_count': book_count,
    }

    return render(request, 'profile.html', context)

@login_required
def get_reading_history_json(request):
    user = request.user
    try:
        reading_history = ReadingHistory.objects.get(user=user)
        # Ambil semua objek BukuDibaca yang terkait dengan objek ReadingHistory
        buku_dibaca_list = reading_history.books.all()
        # Ambil objek Book yang terkait dengan setiap objek BukuDibaca
        book_list = [buku_dibaca.buku for buku_dibaca in buku_dibaca_list]
        return HttpResponse(serializers.serialize('json', book_list))
    except ReadingHistory.DoesNotExist:
        return HttpResponse('False', status=404, content_type='application/json')

@login_required
def get_reading_history(request):
    user = request.user
    reading_history = ReadingHistory.objects.get(user=user)
    
    # Ambil semua objek BukuDibaca yang terkait dengan objek ReadingHistory
    buku_dibaca_list = reading_history.books.all()
    
    return HttpResponse(serializers.serialize('json', buku_dibaca_list), content_type="application/json")

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Perbarui sesi autentikasi pengguna
            update_session_auth_hash(request, user)
            return JsonResponse({"success": "Password changed successfully"})
        else:
            return JsonResponse({"error": "Invalid password change request"}, status=400)
        
@csrf_exempt
def change_password_mobile(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Perbarui sesi autentikasi pengguna
            update_session_auth_hash(request, user)
            return JsonResponse({"success": "Password changed successfully", "status": True}, status=200)
        else:
            return JsonResponse({"error": "Invalid password change request", "status": False}, status=400)