from django.shortcuts import render
from .models import Booking

# Create your views here.
def booking_view(request):
    if request.method == 'POST':
        Booking.objects.create(
            name = request.POST['name'],
            date = request.POST['date'],
            time = request.POST['time'],
            guests = request.POST['guests']
        )
    
    return render(request, 'booking/booking.html')