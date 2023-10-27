from datetime import datetime, timezone
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View
from .models import Book, ProgressBaca, TargetHarian, BukuDibaca, AktivitasUser, BukuDibaca
from .forms import DailyTargetForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AktivitasUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse

@csrf_exempt
@login_required
def buku_list(request):
    buku_list = Book.objects.all()
    user = request.user
    progress_user = ProgressBaca.objects.filter(user=user)
    target_user = TargetHarian.objects.filter(user=user)
    return render(request, 'progress.html', {'buku_list': buku_list, 'progress_user': progress_user, 'target_user': target_user})

@login_required
def set_target(request):
    if request.method == 'POST':
        form = DailyTargetForm(request.POST)
        if form.is_valid():
            target_buku = form.cleaned_data['target_buku']
            # Simpan target harian ini ke sesi pengguna atau model yang sesuai

            # Buat objek TargetHarian dan simpan ke database
            target_harian = TargetHarian(user=request.user, target_buku=target_buku, tanggal=datetime.now())
            target_harian.save()

            request.session['daily_target'] = target_buku

            return render(request, 'progress.html', {'target_buku': target_buku})
    else:
        form = DailyTargetForm()

    return render(request, 'set_target.html', {'form': form})

@login_required
def progress(request):
    user = request.user
    # Ambil data aktivitas pengguna yang saat ini login
    aktivitas_user = AktivitasUser.objects.filter(user=user).order_by('-tanggal')[:7]
    # daily_target = request.session.get('daily_target', 0)
    # daily_target = request.COOKIES.get('daily_target', None)
    # Ekstrak waktu aktif dari setiap entri aktivitas
    waktu_aktif_harian = [aktivitas.waktu_aktif for aktivitas in aktivitas_user]

    context = {
        'waktu_aktif_harian': waktu_aktif_harian,
        # 'daily_target' : daily_target,
    }

    return render(request, 'progress.html', context)

@login_required
def track_user_activity(request):
    if request.method == 'POST':
        user = request.user
        inactivity_time = int(request.POST.get('inactivity_time'))

        # Menghitung waktu aktif saat ini
        aktivitas_user, created = AktivitasUser.objects.get_or_create(user=user, tanggal=datetime.now().date())
        aktivitas_user.waktu_aktif += inactivity_time
        aktivitas_user.save()

        return JsonResponse({'status': 'sukses'})
    return HttpResponse(status=400)

@login_required
def history_buku(request):
    user = request.user
    buku_dibaca = BukuDibaca.objects.filter(user=user)
    return render(request, 'history_buku.html', {'buku_dibaca': buku_dibaca})

def realtime_data(request):
    # Periksa apakah pengguna login
    if request.user.is_authenticated:
        # Ambil waktu login dari sesi pengguna
        login_time = request.session.get('login_time')
        if login_time:
            current_time = datetime.now()
            # Hitung selisih waktu
            elapsed_time = current_time - login_time
            # Ubah selisih waktu ke format yang sesuai
            hours, remainder = divmod(elapsed_time.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            time_string = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
            return JsonResponse({'time': time_string, 'date': login_time.date()})
    return JsonResponse({'time': '00:00:00', 'date': 'YYYY-MM-DD'})
