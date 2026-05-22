from django.shortcuts import render
from .models import MenuItem, Category

# Create your views here.
def menu(request):

    categories = Category.objects.all()

    cart = request.session.get('cart', {})

    cart_items = []

    total = 0

    for item_id, quantity in cart.items():

        try:

            item = MenuItem.objects.get(id=item_id)

            subtotal = item.price * quantity

            total += subtotal

            cart_items.append({
                'item': item,
                'quantity': quantity,
                'subtotal': subtotal,
            })

        except MenuItem.DoesNotExist:

            pass

    return render(request, 'menu/menu.html', {

        'categories': categories,
        'cart_items': cart_items,
        'total_price': total,

    })