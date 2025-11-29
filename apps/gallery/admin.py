from apps.gallery.models import Folder

from django.contrib import admin


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    ...
