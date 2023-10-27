from django.shortcuts import render

from .forms import DailyTargetForm
from django.contrib.auth.decorators import login_required
from .models import AktivitasUser
from django.contrib.auth.decorators import login_required
from my_profile.models import UserProfile

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
    user_profile = UserProfile.objects.get(user=request.user)
    user = request.user
    # Ambil data aktivitas pengguna yang saat ini login
    aktivitas_user = AktivitasUser.objects.filter(user=user).order_by('-tanggal')[:7]
    waktu_aktif_harian = [aktivitas.waktu_aktif for aktivitas in aktivitas_user]
    target_buku = user_profile.target_buku
    
    context = {
        'waktu_aktif_harian': waktu_aktif_harian,
        'target_buku' : target_buku,
    }

    return render(request, 'progress.html', context)
