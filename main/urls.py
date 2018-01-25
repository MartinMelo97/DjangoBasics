from django.urls import path
from .views import saludar
urlpatterns = [
    path('hola', saludar)
]