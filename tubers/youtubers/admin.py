from django.contrib import admin
from .models import *


class YtAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'sub_count', 'is_featured')
    list_filter = ('camera_type', 'city')
    list_display_links = ('first_name', 'last_name')
    ordering = ('id',)

# Register your models here.
admin.site.register(Youtuber, YtAdmin)
