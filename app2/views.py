from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hari(request):
    return HttpResponse('<h1>Hari is my brother</h1>')
def anil(request):
    return HttpResponse('<h1>Anil is very tall boy</h1>')