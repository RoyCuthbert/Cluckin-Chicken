from django.db import models
from django.contrib.auth.models import User
from menu.models import MenuItem

# Create your models here.
class Order(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"
    

class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=1)

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.item.name} x{self.quantity}"