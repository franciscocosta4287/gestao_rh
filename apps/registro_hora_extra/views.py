from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Oi Porque vc esta chegando atrazado ?????????')