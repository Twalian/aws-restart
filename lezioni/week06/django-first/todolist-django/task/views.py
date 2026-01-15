from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, I am the task index!")

# Create your views here.
