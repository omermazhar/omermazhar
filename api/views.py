from django.shortcuts import render

from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
from django.views.generic import ListView


class HeroViewSet(ListView):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
    template_name = './list.html'
