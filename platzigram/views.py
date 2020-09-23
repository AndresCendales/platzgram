"""Platzigram Views."""

# Django
from django.http import HttpResponse
import json

# Utilities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse('Current server time is {}'.format(now))

def sort_integers(request):
    numbers = (request.GET['numbers'])
    
    
    numbers = numbers.split(',')
    numbers = [int(number) for number in numbers]
    
    #import pdb; pdb.set_trace()
    numbers.sort()
  
    data = {
        'status' : 'ok',
        'numbers': numbers,
        'message' : 'Integers sorted succesfully'
    }
    
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type = 'application/json'
    )

def say_hi(request, name, age):
    """Return a greeting"""

    if age < 12:
        message = 'Sorry {}, youre not allowed here'.format(name)
    else:
        message = 'Hello, {} welcome to platzigram'.format(name)

    return HttpResponse(message)