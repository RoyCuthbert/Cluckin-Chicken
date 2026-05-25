from django.shortcuts import render
from menu.models import MenuItem

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')