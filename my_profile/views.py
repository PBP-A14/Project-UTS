from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from my_profile.models import UserProfile, ReadingHistory
from progress_literasi.models import BukuDibaca    
# Create your views here.

@login_required
def user_profile(request):
    # Mengambil objek UserProfile terkait dengan pengguna saat ini
    user = request.user

    reading_history, created = ReadingHistory.objects.get_or_create(user=user)

    context = {
        'reading_history': reading_history,
    }

    return render(request, 'profile.html', context)

@login_required
def get_reading_history_json(request):
    user = request.user
    reading_history = ReadingHistory.objects.get(user=user)
    
    # Ambil semua objek BukuDibaca yang terkait dengan objek ReadingHistory
    buku_dibaca_list = reading_history.books.all()

    # Ambil objek Book yang terkait dengan setiap objek BukuDibaca
    book_list = [buku_dibaca.buku for buku_dibaca in buku_dibaca_list]

    return HttpResponse(serializers.serialize('json', book_list))