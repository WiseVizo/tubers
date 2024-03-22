from django.contrib import admin
from .models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "role", "created_at") # is a list but not sure why we using set
    list_display_links = ("first_name", )
# Register your models here.
admin.site.register(Slider)
admin.site.register(OurTeam, TeamAdmin)