from django.shortcuts import redirect, render
from menu.models import MenuItem


def update_cart(request, id, action):

    cart = request.session.get('cart', {})

    item_id = str(id)

    if action == 'add':

        cart[item_id] = cart.get(item_id, 0) + 1

    elif action == 'remove':

        if item_id in cart:

            cart[item_id] -= 1

            if cart[item_id] <= 0:

                del cart[item_id]

    elif action == 'delete':

        if item_id in cart:

            del cart[item_id]

    request.session['cart'] = cart

    return redirect('/menu/?cart=open')