from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from tables.models import Table
from reservations.models import Reservation
from datetime import datetime, timedelta
import pytz

class ReservationAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.table = Table.objects.create(name="Table 1", seats=4, location="зал")

    def test_create_reservation(self):
        reservation_time = datetime(2025, 4, 10, 18, 0, tzinfo=pytz.UTC)
        data = {
            "customer_name": "Иван",
            "table": self.table.id,
            "reservation_time": reservation_time.isoformat(),
            "duration_minutes": 60
        }
        response = self.client.post("/api/reservations/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservation.objects.count(), 1)

    def test_conflicting_reservation(self):
        reservation_time = datetime(2025, 4, 10, 18, 0, tzinfo=pytz.UTC)

        # первая бронь
        Reservation.objects.create(
            customer_name="Алексей",
            table=self.table,
            reservation_time=reservation_time,
            duration_minutes=60
        )

        # попытка пересекающейся брони
        data = {
            "customer_name": "Мария",
            "table": self.table.id,
            "reservation_time": (reservation_time + timedelta(minutes=30)).isoformat(),
            "duration_minutes": 30
        }
        response = self.client.post("/api/reservations/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Этот столик уже забронирован", str(response.data))
