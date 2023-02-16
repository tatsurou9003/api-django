from django.urls import path
from .views import WeatherList, WeatherListAPI
urlpatterns = [
    path('list/', WeatherList.as_view()),
    path('api/<int:pk>/', WeatherListAPI.as_view()),
]