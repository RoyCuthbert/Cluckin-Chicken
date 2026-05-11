from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} {self.time}"