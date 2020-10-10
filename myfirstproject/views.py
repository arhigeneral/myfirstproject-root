from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def hello(request):
    return HttpResponse('Bye my little friend!')

def reverce(request):
    return render(request, 'reverce.html')
