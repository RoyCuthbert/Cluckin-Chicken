from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    booking = models.IntegerField(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date