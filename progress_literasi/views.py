import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import BukuDibaca, TargetHarian
from .forms import DailyTargetForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from my_profile.models import ReadingHistory, UserProfile
from book.models import Book
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.core import serializers

@login_required
def set_target(request):
    if request.method == 'POST':
        form = DailyTargetForm(request.POST)
        if form.is_valid():
            target_buku = form.cleaned_data['target_buku']
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.target_buku = target_buku
            user_profile.save()

            request.session['daily_target'] = target_buku

            return render(request, 'progress.html', {'target_buku': target_buku})
    else:
        form = DailyTargetForm()

    return render(request, 'set_target.html', {'form': form})

@login_required
def progress(request):
    user = request.user
    user_profile = None
    target_buku = None

    try:
        user_profile = UserProfile.objects.get(user=request.user)
        target_buku = user_profile.target_buku
    except ObjectDoesNotExist:
        user_profile = None
        target_buku = 0

    context = {
        'target_buku': target_buku,
    }

    return render(request, 'progress.html', context)

@login_required
def get_text_progress(request):
    user = request.user
    user_profile = None
    target_buku = None
    book_count = 0  

    try:
        user_profile = UserProfile.objects.get(user=user)
        target_buku = user_profile.target_buku if user_profile else None
    except UserProfile.DoesNotExist:
        user_profile = None
        target_buku = 0

    try:
        reading_history = ReadingHistory.objects.get(user=user)
        book_count = reading_history.books.count() 
    except ReadingHistory.DoesNotExist:
        book_count = 0

    selisih = target_buku - book_count if target_buku is not None else None

    if target_buku is not None:
        if target_buku == 0:
            text_progress = "Segera tentukan target jelajahmu!"
        elif book_count >= target_buku:
            text_progress = "Selamat, proses jelajahmu sudah mencapai target!"
        else:
            if selisih is not None:
                if selisih > 0:
                    text_progress = f"Kamu harus membaca {selisih} buku untuk mencapai target jelajahmu!"
                else:
                    text_progress = "Ayo segera mulai petualangan imajinasimu melalui buku!"
            else:
                text_progress = "Segera tentukan target jelajahmu!"
    else:
        text_progress = "Segera tentukan target jelajahmu!"

    return JsonResponse({'text_progress': text_progress})

@login_required
def update_target(request):
    if request.method == 'POST':
        target_buku = request.POST.get('target_buku')
        
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        update_target = request.POST.get('update_target')
        if target_buku is None:
            target_buku = 0
        
        if update_target == '0':
            user_profile.target_buku = 0
        
        user_profile.target_buku = target_buku
        user_profile.save()

        response_data = {'status': 'success', 'message': 'Target harian berhasil diperbarui.'}
        return JsonResponse(response_data)
    
    response_data = {'status': 'error', 'message': 'Permintaan tidak valid.'}
    return JsonResponse(response_data)

@login_required
def reset_target(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.target_buku = 0
        user_profile.save()
        return JsonResponse({'success': True, 'message': 'Target harian berhasil direset.'})
    except UserProfile.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Profil pengguna tidak ditemukan.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@login_required
def read_book(request, book_id):
    user = get_object_or_404(User, pk=request.user.id)
    book = get_object_or_404(Book, pk=book_id)
    buku_dibaca, created = BukuDibaca.objects.get_or_create(user=user, buku=book)
    if created:
        print(f'BukuDibaca created for user {user} and book {book}')
    else:
        print(f'BukuDibaca already exists for user {user} and book {book}')
    reading_history, created = ReadingHistory.objects.get_or_create(user=user)
    reading_history.books.add(buku_dibaca)
    reading_history.save()

    return redirect('home:home')

@csrf_exempt
@login_required
def set_target_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_target = TargetHarian.objects.create(
           user = request.user,
           target_buku = data['target_buku'], 
        )

        new_target.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def read_book_mobile(request):
    data = json.loads(request.body)
    user_id = data['user_id']
    book_id = data['book_id']
    user = get_object_or_404(User, pk=user_id)
    book = get_object_or_404(Book, pk=book_id)
    buku_dibaca, created = BukuDibaca.objects.get_or_create(user=user, buku=book)
    reading_history, created = ReadingHistory.objects.get_or_create(user=user)

    reading_history.books.add(buku_dibaca)
    reading_history.save()

    return JsonResponse({'message':'Berhasil membaca buku'})

@csrf_exempt
@login_required
def set_target_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_target = TargetHarian.objects.create(
           user = request.user,
           target_buku = data['target_buku'], 
        )

        new_target.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@login_required
def show_json(request):
    data = TargetHarian.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")