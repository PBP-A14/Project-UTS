from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from my_profile.models import UserProfile     
# Create your views here.

@login_required
def user_profile(request):
    # Mengambil objek UserProfile terkait dengan pengguna saat ini
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Anda dapat mengakses atribut UserProfile seperti yang Anda inginkan
    reading_list = user_profile.reading_list.all()
    history_bacaan = user_profile.history_bacaan.all()
    progress_literasi = user_profile.progress_literasi

    # Kemudian, Anda dapat melewatkan data ini ke tampilan template
    context = {
        'reading_list': reading_list,
        'history_bacaan': history_bacaan,
        'progress_literasi': progress_literasi,
    }

    return render(request, 'profile.html', context)