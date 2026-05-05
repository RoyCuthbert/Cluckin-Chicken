from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class MenuItem(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)