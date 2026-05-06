from django.shortcuts import render, redirect
from .models import Booking

# Create your views here.
def booking_view(request):
    if request.method == 'POST':
        date = request.POST.get('date'),
        time = request.POST.get('time'),
        guests = request.POST.get('guests')

        Booking.objects.create(
            date=date,
            time=time,
            guests=guests
        )
        return redirect('booking')

    return render(request, 'booking/booking.html')
