from django.shortcuts import render
from django.http import HttpResponse

def world(request):
    return HttpResponse("Hello world!")


# Views pass information to browser - Returns an HTTP Response that has the details
# Also takes in HTML with render & so on

# URL.py calls these function depending how it is defined