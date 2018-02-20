from django.contrib import admin
from .models import Operiation, OperationItem

class OperationItemInline(admin.TabularInline):
    model = OperationItem
    raw_id_fields = ['item']

class OperationAdmin(admin.ModelAdmin):
    list_display = ['id', 'worker', 'created', 'operation']
    inlines = [OperationItemInline]

admin.site.register(Operiation, OperationAdmin)

# Register your models here.
