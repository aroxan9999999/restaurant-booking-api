from django.db import models

class Table(models.Model):
    name = models.CharField(max_length=100)
    seats = models.IntegerField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.seats} seats)"
