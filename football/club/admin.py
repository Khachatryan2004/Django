from django.contrib import admin
from .models import *


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'status')
    list_display_links = ('name', 'country', 'status')


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_display_links = ('name', 'status')


