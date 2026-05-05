from django.shortcuts import render, redirect
from .models import Booking

# Create your views here.
def booking_view(request):
    if request.method == 'POST':
        Booking.objects.create(
            date = request.POST['date'],
            time = request.POST['time'],
            guests = request.POST['guests']
        )
        return redirect('booking')

    return render(request, 'booking/booking.html')