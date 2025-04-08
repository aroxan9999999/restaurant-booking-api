from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from tables.models import Table

class TableAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_table(self):
        data = {"name": "Test Table", "seats": 4, "location": "Терраса"}
        response = self.client.post("/api/tables/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Table.objects.count(), 1)
        self.assertEqual(Table.objects.get().name, "Test Table")