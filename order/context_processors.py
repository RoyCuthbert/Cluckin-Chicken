from menu.models import MenuItem


def cart_data(request):

    cart = request.session.get('cart', {})

    cart_items = []

    total_price = 0

    for key, quantity in cart.items():

        try:

            item = MenuItem.objects.get(id=int(key))

            subtotal = item.price * quantity

            total_price += subtotal

            cart_items.append({

                'item': item,
                'quantity': quantity,
                'subtotal': subtotal,

            })

        except (MenuItem.DoesNotExist, ValueError):

            continue

    return {

        'cart_items': cart_items,
        'total_price': total_price,

    }