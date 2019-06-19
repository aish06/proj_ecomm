"""proj_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import index,login_page,homepage,signup_page

from bouquet.views import bouquet_list_view
from cake.views import cake_list_view
from cards.views import card_list_view
from chocolates.views import chocolate_list_view
from Watches.views import watch_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_page),
    path('login/', login_page),
    path('', homepage),
    path('products/',index),
    path('bouquet/', bouquet_list_view),
    path('cake/', cake_list_view),
    path('chocolate/', chocolate_list_view),
    path('watch/', watch_list_view),
    path('card/',card_list_view ),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
