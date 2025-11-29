from apps.gallery.models import Folder

from django.db.models import Q
from django.shortcuts import render


def gallery_index(request):
    if request.method == 'GET':
        folders = Folder.objects.all()

        if query := request.GET.get('q'):
            folders = folders.filter(
                Q(folder_name__icontains=query) |
                Q(description__icontains=query)
            )

        context = {
            'folders': folders
        }
        return render(request, 'gallery/index.html', context)
