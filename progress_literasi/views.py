from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import ProgressBaca, TargetHarian, BukuDibaca, AktivitasUser, BukuDibaca
from .forms import TargetHarianForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AktivitasUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from my_profile.models import ReadingHistory
from home.models import Book
from django.contrib.auth.models import User
from django.http import Http404

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
        form = TargetHarianForm(request.POST)
        if form.is_valid():
            target = form.save(commit=False)
            target.user = request.user
            target.save()
            return redirect('progress')
    else:
        form = TargetHarianForm()
    return render(request, 'set_target.html', {'form': form})

@login_required
def progress(request):
    user = request.user
    # Ambil data aktivitas pengguna yang saat ini login
    aktivitas_user = AktivitasUser.objects.filter(user=user).order_by('-tanggal')[:7]

    # Ekstrak waktu aktif dari setiap entri aktivitas
    waktu_aktif_harian = [aktivitas.waktu_aktif for aktivitas in aktivitas_user]

    context = {
        'waktu_aktif_harian': waktu_aktif_harian,
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

@login_required
def read_book(request, book_id):
    user = get_object_or_404(User, pk=request.user.id)
    book = get_object_or_404(Book, pk=book_id)

    # # Check if any of the book's fields is null
    # if any(
    #     field is None
    #     for field in [book.title, book.description, book.authors, book.isbn, book.num_pages, book.publisher, book.rating_count, book.rating]
    # ):
    #     raise Http404("The requested book does not exist or has null values in some fields.")

    # try:
    #     BukuDibaca.objects.get(user=user, buku=book)
    # except:
    #     BukuDibaca.objects.create(user=user, buku=book)  

    buku_dibaca, created = BukuDibaca.objects.get_or_create(user=user, buku=book)

    reading_history, created = ReadingHistory.objects.get_or_create(user=user)
    reading_history.books.add(buku_dibaca)
    reading_history.save()

    return redirect('home:home')