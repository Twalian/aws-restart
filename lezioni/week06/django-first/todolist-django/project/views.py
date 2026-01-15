from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request

user = [
    {"id": 1, "name": "Mario"},
    {"id": 2, "name": "Luigi"}
]

def index(request):
    return HttpResponse("Hello, I am the project index!")

def pippo(request):
    return HttpResponse("Hello, I am Pippo!")

def users(request):
    return JsonResponse(user, safe=False)