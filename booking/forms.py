from django import forms
from .models import Booking
from django.utils import timezone

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','email','date', 'start_time', 'end_time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time-local'}),
            'end_time': forms.TimeInput(attrs={'type': 'time-local'}),
            }

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_time")
        end = cleaned_data.get("end_time")

        if start and end:
            if start <= timezone.now():
                raise forms.ValidationError("Select a date and time in the future.")
            if start.minute % 15 != 0:
                raise forms.ValidationError("Time must be in 15-minute intervals (e.g., :00, :15, :30, :45).")
            
            # Check DB for overlaps
            overlapping = Booking.objects.filter(
                start_time__lt=end,
                end_time__gt=start
            )
            if overlapping.exists():
                raise forms.ValidationError("This time slot is already booked.")
        
        return cleaned_data