from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import RetrieveAPIView
from .models import Weather
from .serializers import WeatherSerializer
from rest_framework.permissions import IsAuthenticated

class WeatherList(ListView):
    template_name = "list.html"
    model = Weather

class WeatherListAPI(RetrieveAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAuthenticated]
