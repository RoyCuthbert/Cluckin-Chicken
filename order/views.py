from django.shortcuts import redirect, render
from menu.models import MenuItem
from .cart import Cart

# Create your views here.
def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    item_id = str(id)

    if item_id in cart:
        cart[item_id] += 1
    else:
        cart[item_id] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('menu')
