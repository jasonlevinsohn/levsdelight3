from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Slideshow
from levsdelight2 import settings

def home(request, template='base.html'):
    
    slideOne = Slideshow.objects.get(pk=1)
    print slideOne
    sPath = settings.SETTINGS_ROOT
    pPath = settings.PROJECT_ROOT
    stPath = settings.STATIC_ROOT

    return render_to_response(template, {
            'slideOne' : slideOne,
            'settingsPath' : sPath,
            'projectPath' : pPath,
            'staticPath' : stPath,
        }, context_instance = RequestContext(request))

