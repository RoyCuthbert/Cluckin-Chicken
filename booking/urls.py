from django.urls import path
from .views import booking_view, booking_success, cancel_booking

urlpatterns = [
    path('',  booking_view, name='booking'),
    path('success', booking_success, name='booking_success'),
    path('cancel<int:id>', cancel_booking, name='cancel_booking'),
]