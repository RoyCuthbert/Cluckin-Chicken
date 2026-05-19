from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_view, name='booking'),
    path('success', views.booking_success, name='booking_success')
]