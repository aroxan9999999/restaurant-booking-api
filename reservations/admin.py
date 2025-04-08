from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'table', 'reservation_time', 'duration_minutes')
    search_fields = ('customer_name',)
    list_filter = ('table', 'reservation_time')
