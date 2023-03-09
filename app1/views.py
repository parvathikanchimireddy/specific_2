from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sam(request):
    return HttpResponse('<h1>sam is very good girl</h1>')
def ram(request):
    return HttpResponse('<h1>ram is very good boy</h1>')