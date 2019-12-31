"""refugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from apps.mascota.views import mascotas, mascota_nuevo, mascota_list
from apps.adopcion.views import adopcion

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mascotas, name='index'),
    url(r'^nueva_mascota/$', mascota_nuevo, name='crear_mascota'),
    url(r'^ver_mascota/$', mascota_list, name='ver_mascotas'),

]
