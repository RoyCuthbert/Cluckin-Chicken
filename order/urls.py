from django.urls import path

from .views import (
    add_to_cart,
    decrease_cart,
    remove_from_cart,
)

urlpatterns = [

    path('add/<int:id>/',
         add_to_cart,
         name='add_to_cart'),

    path('decrease/<int:id>/',
         decrease_cart,
         name='decrease_cart'),

    path('remove/<int:id>/',
         remove_from_cart,
         name='remove_from_cart'),
]