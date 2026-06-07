from django.shortcuts import render, redirect
from django.contrib import messages
from menu.models import MenuItem
from .models import ContactMessage

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def contact(request):
    if request.method == 'POST':

        ContactMessage.objects.create(

            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')

        )

        messages.success(
            request,
            'Your message has been sent successfully!'
        )

        return redirect('contact')

    return render(request, 'core/contact.html')

