from django.shortcuts import render, redirect
from .models import Booking
from django.contrib import messages

# Create your views here.
def booking_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        
        if not name or not email:
            return render(request, 'booking/booking.html')
        
        Booking.objects.create(
            name = name,
            email = email,
            date = date,
            time = time,
            guests = guests,
        )
        messages.success(request, "Booking Successful!")
        return redirect('booking')
        
        return redirect('booking')

    return render(request, 'booking/booking.html')
