from django.shortcuts import render
from .models import MenuItem, Category

# Create your views here.
def menu(request):
    categories = Category.objects.all()
    items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {'categories':categories, 'items':items})