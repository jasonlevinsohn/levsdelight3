from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Slideshow, MonthMap
from django.views.decorators.csrf import csrf_exempt
from levsdelight2 import settings
import json, os, time, base64, hmac, sha, urllib, hashlib
import re, datetime


def test_upload(request, template='testupload.html'):

    test_upload_var = 'This is the test upload var.'

    return render_to_response(template, {
            'test_upload_var': test_upload_var
        }, context_instance = RequestContext(request))

def home(request, template='slideshow.html'):

    # Redirect the home page to the current month.
    today = datetime.datetime.now()
    month = today.strftime('%B').lower()
    year = today.strftime('%Y')

    newPath = "slideshow/%s/%s" % (year, month)

    return HttpResponseRedirect(newPath)


def slideshow(request, year=None, month=None, template='slideshow.html'):

    print "The selected slideshow is %s %s" % (month, year)
    sPath = settings.SETTINGS_ROOT
    pPath = settings.PROJECT_ROOT
    stPath = settings.STATIC_ROOT
    offline = settings.OFFLINE
    staticUrl = settings.STATIC_URL
    # allSlides = Slideshow.objects.all()

    # Get the slideshow id
    # ******** NOTE: We need an exception here for invalid URL ***********
    mapObject = MonthMap.objects.filter(month=month, year=year)
        
    map_id = mapObject[0].slideshow_id
    objects_returned = mapObject.count()
    print "Slideshow Id: %s and the count is: %s" % (map_id, objects_returned)
    allSlides = Slideshow.objects.filter(slideshow_id=map_id)

    print "The value of all slides: "
    print allSlides
    # @@@@@@@@@@@ LAST MOD @@@@@@@@@@@@@@@@@@

    return render_to_response(template, {
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

@csrf_exempt
def upload_image(request):
    print "Receiving File from Mobile Device....\n\n"
    print request
    print "The Files: \n" 
    file = request.FILES['file']
    print "One File: %s" % (file)
    print "File Attr: "
    print file
    print request.FILES

    print "The Requests: \n\n"
    desc = request.REQUEST['description']
    title = request.REQUEST['title']
    month = request.REQUEST['month']
    report = "Desc: %s\n Title: %s\n Month: %s" % (desc, title, month)
    print "Desc: %s\n Title: %s\n Month: %s" % (desc, title, month)


    return HttpResponse("Hey, I appreciate the file. \n\n %s" % (report))

@csrf_exempt
def write_image_to_database(request):
    print "Write that stuff"
    filePath = request.REQUEST['path']
    title = request.REQUEST['title']
    desc = request.REQUEST['desc']
    month = request.REQUEST['month']

    # Parse out the month name
    # Match:
    # ---- ^ Starting at beginning of string
    # ---- . anything
    # ---- * zero or more occurances
    # ---- ? Lazily (not greedy)
    # ---- (?=) Asserting looking ahead
    # ---- \d match everything before a digit


    monthReg = re.compile("^.*?(?=\d)")
    m = monthReg.match(month)
    monthName = m.group()

    # Get the last 4 chars of string
    yearNumber = month[-4:]

    # Get the month map id
    monthId = MonthMap.objects.get(month=monthName, year=yearNumber)

    # Create a new slideshow object
    picture_object = Slideshow(
            title=title,
            desc=desc,
            pictureLocation=filePath,
            isActive=True,
            slideshow_id=monthId.slideshow_id,
            order_id=0,
            pub_date=datetime.datetime.now())

    picture_object.save()


    print "The file %s has a title of %s and desc: %s" % (filePath, title, desc)
    print "The Month has an id of: %s" % (monthId.slideshow_id)
    
    return HttpResponse("The server says: Picture has been persisted")

@csrf_exempt
def get_signature_for_browser(request):

    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID', False)
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', False)
    S3_BUCKET = 'levsdelight'
    S3_BUCKET_FOLDER = 'img'

    object_name = request.REQUEST.get('name')
    mime_type = request.REQUEST.get('type')

    # Policy Document
    policy = """{
            "expiration" : "2015-01-01T00:00:00Z",
            "conditions" : [
                {"bucket": "%s"},
                {"acl": "public-read"},
                ["starts-with", "$key", "img/"],
                ["starts-with", "$Content-Type", ""],
                ["content-length-range", 0, 524288000]
                ]
            }""" % (S3_BUCKET)
        
    # Encode Policy Document
    encoded_policy = base64.b64encode(policy)

    # Create Signature with Policy Document and Secret Key
    signature = base64.b64encode(hmac.new(AWS_SECRET_KEY, encoded_policy, hashlib.sha1).digest())

    result = {
        'access_id': AWS_ACCESS_KEY,
        'policy': encoded_policy,
        'sig' : signature
    }

    return HttpResponse(json.dumps(result))


    

@csrf_exempt
def sign_s3_upload(request):

        

    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID', False)
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', False)
    S3_BUCKET = 'levsdelight'
    S3_BUCKET_FOLDER = 'img'


    # Policy Document
    policy = """{
            "expiration" : "2015-01-01T00:00:00Z",
            "conditions" : [
                {"bucket": "%s"},
                {"acl": "public-read"},
                ["starts-with", "$key", "img/"],
                ["starts-with", "$Content-Type", ""],
                ["content-length-range", 0, 524288000]
                ]
            }""" % (S3_BUCKET)
        
    # Encode Policy Document
    encoded_policy = base64.b64encode(policy)

    # Create Signature with Policy Document and Secret Key
    signature = base64.b64encode(hmac.new(AWS_SECRET_KEY, encoded_policy, hashlib.sha1).digest())

    result = {
            'signature': signature,
            'acl': 'public-read',
            'bucket': S3_BUCKET,
            'policy': encoded_policy,
            'aws_key': AWS_ACCESS_KEY


            }
    print "SENDING BACK SIG"

    return HttpResponse(json.dumps(result))
