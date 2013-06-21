from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Slideshow

def home(request):
    
    slideOne = Slideshow.objects.get(pk=1)
    print slideOne

    return HttpResponse('Hello')

