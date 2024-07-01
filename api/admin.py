from django.contrib import admin
from .models import CME

# Register your models here.

@admin.register(CME)
class CMEAdmin(admin.ModelAdmin):
    list_display = ('year', 'specialty', 'hospital', 'credits', 'status')
