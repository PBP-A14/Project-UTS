from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Bookmark
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

@login_required
def my_library(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'my_library/my_library.html', {'bookmarks': bookmarks})

@login_required
def remove_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, id=bookmark_id, user=request.user)
    bookmark.delete()
    return HttpResponseRedirect(reverse('my_library'))

@login_required
def mark_as_read(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, id=bookmark_id, user=request.user)
    bookmark.finished_reading = True
    bookmark.save()
    return HttpResponseRedirect(reverse('my_library'))