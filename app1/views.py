from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('<h1>Best Finisher</h1>')

def raina(request):
    return HttpResponse('<h1>Mr. IPL</h1>')