from django.test import TestCase
from .models import Booking
from .utils import get_available_slots

# Create your tests here.
class BookingModelTest(TestCase):

    def test_create_booking(self):

        booking = Booking.objects.create(

            name='John',

            email='john@test.com',

            day='Monday',

            date='2026-06-01',

            time='12:00',

            guests=2

        )

        self.assertEqual(booking.name, 'John')

        self.assertEqual(booking.guests, 2)


class BookingSlotTest(TestCase):

    def test_booked_slot_disappears(self):

        Booking.objects.create(

            name='John',

            email='john@test.com',

            day='Monday',

            date='2026-06-01',

            time='12:00',

            guests=2

        )

        slots = get_available_slots(
            'Monday',
            '2026-06-01'
        )

        self.assertNotIn('12:00', slots)