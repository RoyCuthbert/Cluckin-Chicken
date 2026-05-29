from django.shortcuts import render, redirect
from .models import Booking
from .utils import get_available_slots


def booking_view(request):

    available_slots = []

    selected_day = request.POST.get('day', '')

    selected_date = request.POST.get('date', '')

    if selected_day and selected_date:
         
        available_slots = get_available_slots(
            selected_day,
            selected_date
        )

    if request.method == 'POST' and request.POST.get('time'):

            Booking.objects.create(

                name=request.POST.get('name'),

                email=request.POST.get('email'),

                day=selected_day,

                date=selected_date,

                time=request.POST.get('time'),

                guests=request.POST.get('guests'),

            )

            return redirect('booking_success')


    return render(request, 'booking/booking.html', {

        'available_slots': available_slots,
        'selected_day': selected_day,
        'selected_date': selected_date,
        'name': request.POST.get('name', ''),
        'email': request.POST.get('email', ''),
        'guests': request.POST.get('guests', '')
    })

def booking_success(request):
    last_booking = Booking.objects.last()
    return render(request, 'booking/success.html',{
        'booking': last_booking
    })

def cancel_booking(request, id):
    booking = Booking.objects.get(id=id)
    booking.delete()
    return redirect('/booking/')