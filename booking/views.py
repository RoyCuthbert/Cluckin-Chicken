from django.shortcuts import render, redirect
from .models import Booking
from django.contrib import messages

# Create your views here.
def booking_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        guests = request.POST.get('guests')
        
        if not name or not email:
            return render(request, 'booking/booking.html')
        
        Booking.objects.create(
            name = name,
            email = email,
            date = date,
            start_time = start_time,
            end_time = end_time,
            guests = guests,
        )

        # existing_booking = Booking.objects.filter(
        # date = date,
        # start_time = start_time,
        # end_time = end_time
        # ).exists()

        # if existing_booking:

        #     messages.error(request, "This time slot is already booked!")

        #     return redirect('/booking/')
        

        messages.success(request, "Booking Successful!")
        return redirect('booking_success')
        

    return render(request, 'booking/booking.html')

def booking_success(request):
    return render(request, 'booking/success.html')


