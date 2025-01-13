"""
URL configuration for Modulo66 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from Estadistica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estadistica/', views.estadistica, name='estadistica'),
    path('meseros/', views.meseros, name='about'),
    path('mesas/', views.mesas, name='mesas'),
    path('productos/', views.productos, name='productos'),
]
