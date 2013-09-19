from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Slideshow
from levsdelight2 import settings
import json, os, time, base64, hmac, sha, urllib
def test_upload(request, template='testupload.html'):

    test_upload_var = 'This is the test upload var.'

    return render_to_response(template, {
            'test_upload_var': test_upload_var
        }, context_instance = RequestContext(request))

def home(request, template='slideshow.html'):
    slideOne = Slideshow.objects.get(pk=1)
    print slideOne
    sPath = settings.SETTINGS_ROOT
    pPath = settings.PROJECT_ROOT
    stPath = settings.STATIC_ROOT
    offline = settings.OFFLINE
    staticUrl = settings.STATIC_URL
    allSlides = Slideshow.objects.all()

    return render_to_response(template, {
            'slideOne' : slideOne,
            'settingsPath' : sPath,
            'projectPath' : pPath,
            'staticPath' : stPath,
            'staticUrl' : staticUrl,
            'offline' : offline,
            'allSlides' : allSlides,
        }, context_instance = RequestContext(request))

def logout_page(request):
    
    logout(request)
    print "what is happening"
    return HttpResponseRedirect('/')


def sign_s3_upload(request):

        
       # Get AWS Credentials
       AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID', False)
       AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', False)
       S3_BUCKET = 'levsdelight'
       S3_BUCKET_FOLDER = 'img'

       # Collect information on the image file from the request
       object_name = request.GET.get('s3_object_name')
       mime_type = request.GET.get('s3_object_type')

       # Set the expire time of the signature (in seconds) and
       # declare the permissions of the file to be uploaded.
       expires = int(time.time()+1000)
       amz_headers = 'x-amz-acl:public-read'

       # Generate the put request that JavaScript will use
       put_request = "PUT\n\n%s\n%d\n%s\n/%s/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, S3_BUCKET_FOLDER, object_name)
    
       # Generate the signature which will sign the request
       signature = base64.encodestring(hmac.new(AWS_SECRET_KEY, put_request, sha).digest())

       # Remove surrounding whitespace and quote special characters.
       signature = urllib.quote_plus(signature.strip())

       # Build the URL of the file in anticipation of its imminent upload
       url = 'https://%s.s3.amazonaws.com/%s/%s' % (S3_BUCKET, S3_BUCKET_FOLDER, object_name)

       # Build the signed request
       signed_request = '%s?AWSAccessKeyId=%s&Expires=%d&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature)

       result = {
               'signed_request': signed_request,
               'url': url

               }
       return HttpResponse(json.dumps(result))
