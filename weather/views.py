from django.shortcuts import render
from django.http import HttpResponse

def WeatherView(request):
    return HttpResponse("How is the weather !")
