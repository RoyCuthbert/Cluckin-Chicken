from django.urls import path

from .views import (update_cart)

urlpatterns = [path('update/<int:id>/<str:action>/',update_cart, name='update_cart'),]