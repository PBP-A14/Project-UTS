from django.shortcuts import render, redirect, get_object_or_404
from .models import BukuDibaca
from .forms import DailyTargetForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from my_profile.models import ReadingHistory, UserProfile
from home.models import Book
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth import logout

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
        target_buku = user_profile.target_buku if user_profile else None
    except ObjectDoesNotExist:
        user_profile = None
        target_buku = 0

    reading_history, created = ReadingHistory.objects.get_or_create(user=user)   
    book_count = reading_history.books.count()
    selisih = target_buku - book_count if target_buku is not None else None

    context = {
        'target_buku': target_buku,
        'progress': user_profile.progress if user_profile else None,
        'book_count': book_count,
        'selisih': selisih,
    }

    return render(request, 'progress.html', context)

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

    reading_history, created = ReadingHistory.objects.get_or_create(user=user)
    
    reading_history.books.add(buku_dibaca)
    reading_history.save()

    return redirect('home:home')