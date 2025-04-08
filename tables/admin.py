from django.contrib import admin
from .models import Table

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'seats', 'location')
    search_fields = ('name', 'location')
    list_filter = ('location',)
