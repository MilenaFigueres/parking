from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from parking_app.models import Car, Own
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the parking index.")