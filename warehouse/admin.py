from django.contrib import admin
from .models import Category, SemiFinishedItem, FinishedProduct


class SemiFinishedItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'producer','quantity', 'price']

admin.site.register(SemiFinishedItem, SemiFinishedItemAdmin)

class FinishedProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price']

admin.site.register(FinishedProduct, FinishedProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)