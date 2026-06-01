from django.test import TestCase
from menu.models import Category, MenuItem
from .models import OrderItem, Order

# Create your tests here.
class CartTest(TestCase):

    def test_add_to_cart(self):

        category = Category.objects.create(
            name='Food'
        )

        item = MenuItem.objects.create(

            category=category,

            name='Fries',

            description='Test',

            price=3.50

        )

        order = Order.objects.create()

        cart = OrderItem.objects.create(

            order=order,

            item=item,

            quantity=2,

            price=item.price

        )

        self.assertEqual(cart.quantity, 2)