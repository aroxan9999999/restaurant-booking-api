from rest_framework import serializers
from .models import Reservation
from datetime import timedelta

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        reservation_time = data['reservation_time']
        duration = data['duration_minutes']
        table = data['table']
        end_time = reservation_time + timedelta(minutes=duration)

        overlapping = Reservation.objects.filter(table=table).exclude(id=self.instance.id if self.instance else None)

        for reservation in overlapping:
            res_start = reservation.reservation_time
            res_end = res_start + timedelta(minutes=reservation.duration_minutes)

            # Проверка на пересечение
            if reservation_time < res_end and end_time > res_start:
                raise serializers.ValidationError("Этот столик уже забронирован на это время.")

        return data
