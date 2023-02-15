from django.contrib import admin
from django.urls import path, include
from .views import HelloWorld

urlpatterns = [
    path("admin/", admin.site.urls),
    path('helloworld/', HelloWorld.as_view()),
    path('', include('weather.urls'))
]
