from django.contrib import admin
from django.urls import path
from .views import api_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hola/', api_home, name='api_home'),
]