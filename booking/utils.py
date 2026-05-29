from datetime import datetime, timedelta
from .models import Booking


def generate_slots(start, end):

    slots = []

    current = datetime.strptime(start, "%H:%M")

    end_time = datetime.strptime(end, "%H:%M")

    while current <= end_time:

        slots.append(
            current.strftime("%H:%M")
        )

        current += timedelta(minutes=60)

    return slots


def get_available_slots(day, date):

    opening_hours = {

        'Monday': ('12:00', '22:00'),
        'Tuesday': ('12:00', '22:00'),
        'Wednesday': ('12:00', '22:00'),
        'Thursday': ('12:00', '22:00'),

        'Friday': ('12:00', '23:00'),

        'Saturday': ('10:00', '23:00'),

        'Sunday': ('10:00', '22:00'),
    }

    if day not in opening_hours:
        return []
    
    start, end = opening_hours[day]

    all_slots = generate_slots(start, end)

    booked_slots = Booking.objects.filter(
        day =day,
        date=date
    ).values_list(
        'time',
        flat=True
    )

    available = []

    for slot in all_slots:

        if slot not in booked_slots:
            available.append(slot)

    return available