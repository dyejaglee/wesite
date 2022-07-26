from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")