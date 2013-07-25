from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
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
    offline = settings.OFFLINE

    return render_to_response(template, {
            'slideOne' : slideOne,
            'settingsPath' : sPath,
            'projectPath' : pPath,
            'staticPath' : stPath,
            'offline' : offline,
        }, context_instance = RequestContext(request))

def logout_page(request):
    
    logout(request)
    print "what is happening"
    return HttpResponseRedirect('/')

