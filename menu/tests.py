from django.test import TestCase
from .models import Category, MenuItem

# Create your tests here.
class MenuTest(TestCase):

    def test_create_menu_item(self):

        category = Category.objects.create(
            name='Burgers'
        )

        item = MenuItem.objects.create(

            category=category,

            name='Chicken Burger',

            description='Test burger',

            price=9.99

        )

        self.assertEqual(item.name, 'Chicken Burger')

        self.assertEqual(item.price, 9.99)