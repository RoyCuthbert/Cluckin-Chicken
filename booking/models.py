from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(default=User, max_length=100)
    email = models.EmailField(default=User)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def duration(self):
        # making sure time is in the future
        if self.start_time <= timezone.now():
            raise ValidationError("Bookings must be set for a future time.")
        
        # 15 min intervals
        if self.start_time.minute %15 != 0 or self.start_time.second != 0:
            raise ValidationError("Bookings must be made in 15 minute intervals.")
        
        overlapping = Booking.objects.filter(
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(pk=self.pk) # Exclude self when editing

        if overlapping.exists():
            raise ValidationError("This time slot is already booked.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.time}"