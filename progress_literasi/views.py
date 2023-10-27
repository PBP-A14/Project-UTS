from datetime import date, datetime
from django.shortcuts import render

from .models import ProgressBaca, TargetHarian, AktivitasUser
from .forms import DailyTargetForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import AktivitasUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from my_profile.models import UserProfile

@login_required
def set_target(request):
    if request.method == 'POST':
        form = DailyTargetForm(request.POST)
        if form.is_valid():
            target_buku = form.cleaned_data['target_buku']

            # Pastikan UserProfile terkait dengan pengguna (User) ada
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)

            if user_profile.last_target_date != date.today() :
                user_profile.target_buku = None
            
            user_profile.target_buku = target_buku
            user_profile.last_target_date = date.today()
            user_profile.save()

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
    waktu_aktif_harian = [aktivitas.waktu_aktif for aktivitas in aktivitas_user]
    user_profile = UserProfile.objects.get(user=request.user)
    target_buku = user_profile.target_buku

    context = {
        'waktu_aktif_harian': waktu_aktif_harian,
        'target_buku' : target_buku,
        # 'active_time' : user_profile.active_time.total_seconds(),
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
