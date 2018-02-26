from django.contrib import admin
from .models import LocalizationItem

class LocalizationItemAdmin(admin.ModelAdmin):
    list_display = ['localization', 'item', 'date_of_placement']

admin.site.register(LocalizationItem, LocalizationItemAdmin)

# Register your models here.
