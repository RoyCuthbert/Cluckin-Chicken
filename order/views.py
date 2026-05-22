from django.shortcuts import redirect, render
from menu.models import MenuItem


def add_to_cart(request, id):

    cart = request.session.get('cart', {})

    item_id = str(id)

    cart[item_id] = cart.get(item_id, 0) + 1

    request.session['cart'] = cart

    return redirect('/menu/?cart=open')


def decrease_cart(request, id):

    cart = request.session.get('cart', {})

    item_id = str(id)

    if item_id in cart:

        cart[item_id] -= 1

        if cart[item_id] <= 0:

            del cart[item_id]

    request.session['cart'] = cart

    return redirect('/menu/?cart=open')


def remove_from_cart(request, id):

    cart = request.session.get('cart', {})

    item_id = str(id)

    if item_id in cart:

        del cart[item_id]

    request.session['cart'] = cart

    return redirect('/menu/?cart=open')