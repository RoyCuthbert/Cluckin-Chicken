from django.shortcuts import render
from .models import MenuItem, Category

# Create your views here.
def menu(request):
    categories = Category.objects.all()
    items = MenuItem.objects.all()
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    item_ids = [int(id) for id in cart.keys()]

    menu_items = MenuItem.objects.filter(id__in=item_ids)

    for item in menu_items:

        quantity = cart[str(item.id)]
        subtotal = item.price * quantity
        total_price += subtotal

        cart_items.append({
            'item': item,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'menu/menu.html', {'categories':categories, 'items':items, 'cart': cart, 'cart_items': cart_items, 'total_price': total_price})