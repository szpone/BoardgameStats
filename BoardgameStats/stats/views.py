from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.

def index(request):
    return HttpResponse("Elo")
