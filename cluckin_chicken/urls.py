"""
URL configuration for cluckin_chicken project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as core_view
from core import views as contact_view
from accounts import views as accounts_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', core_view.home, name='home'),
    path('menu/', include('menu.urls')),
    path('booking/', include('booking.urls')),
    path('contact/', contact_view.contact, name = 'contact'),
    path('accounts/', accounts_view.accounts, name='accounts'),
    path('cart/', include('order.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)