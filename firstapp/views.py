from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello world")

def htm(request):
    return render(request,'sample.html')

def sample(request):
    return render(request, 'sample1.html')