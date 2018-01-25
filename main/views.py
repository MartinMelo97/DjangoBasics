from django.shortcuts import render
from django.http import HttpResponse


def saludar(self):
    print("Llego")
    return HttpResponse("Hola a Django")



