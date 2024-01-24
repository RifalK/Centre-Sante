"""
URL configuration for myfirst project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework import routers
from Urologie.views import *
import django_filters.rest_framework
import rest_framework
from django.contrib.auth.models import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


router = routers.DefaultRouter()
router.register(r'Patient', PatientViewSet)
router.register(r'Professionnelsante', ProfessionnelsanteViewSet)


urlpatterns = [

    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
]

class PatientListView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

class ProfessionnelsanteListView(generics.ListAPIView):
    queryset = Professionnelsante.objects.all()
    serializer_class = ProfessionnelsanteSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class PatientListView(generics.ListAPIView):
    ...
    filter_backends = [DjangoFilterBackend]

class ProfessionnelsanteListView(generics.ListAPIView):
    ...
    filter_backends = [DjangoFilterBackend]