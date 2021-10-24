from django.contrib import admin
from first_app.models import *

# Register your models here.
class AdminAlbum(admin.ModelAdmin):
    list_display = ['artist', 'name', 'release_date']

admin.site.register(Musician)
admin.site.register(Album,AdminAlbum)
