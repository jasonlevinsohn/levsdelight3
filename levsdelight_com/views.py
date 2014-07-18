from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Slideshow, MonthMap, BlogPost, Comment, Author
from django.views.decorators.csrf import csrf_exempt
from levsdelight2 import settings
import json, os, time, base64, hmac, sha, urllib, hashlib
import re, datetime
from django.core import serializers

def get_comments(request):
    comments = Comment.objects.all()

    serialized_comments = serializers.serialize('json', comments)
    
    return HttpResponse(serialized_comments, mimetype='application/json')

@csrf_exempt
def save_comment(request):

    req = json.loads(request.body)
    print "Name: %s, Comment: %s" % (req['name'], req['comment'])

    #### JULY 17th, 2014 - START FROM HERE
    #### NOW WE SEND OUT AN EMAIL AND PERSIST THE COMMENT ON THE CURRENTLY
    #### RENDERED BROWSER.  BUT IT IS NOT PERSISTED UNTIL NAT OR I CHECK OFF
    #### ON IT
    return HttpResponse("%s's comment has been saved." % req['name'])


def blog(request, template='blog.html'):

    return render_to_response(template, {}, context_instance = RequestContext(request))

def top_ten_blogs(request):

    blogs = BlogPost.objects.all()

    # We need natural key arg for getting first_name & last_name
    # as foreign keys when querying BlogPost
    serialized_data = serializers.serialize('json', blogs, use_natural_keys=True)


    return HttpResponse(serialized_data, mimetype='application/json')



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
    allSlides = Slideshow.objects.filter(slideshow_id=map_id)

    # @@@@@@@@@@@ LAST MOD @@@@@@@@@@@@@@@@@@

    return render_to_response(template, {
            'settingsPath' : sPath,
            'projectPath'  : pPath,
            'staticPath'   : stPath,
            'staticUrl'    : staticUrl,
            'offline'      : offline,
            'allSlides'    : allSlides,
            'slideMonth'   : month,
            'slideYear'    : year
        }, context_instance = RequestContext(request))

def logout_page(request):
    
    logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def upload_image(request):

    file = request.FILES['file']

    desc = request.REQUEST['description']
    title = request.REQUEST['title']
    month = request.REQUEST['month']
    report = "Desc: %s\n Title: %s\n Month: %s" % (desc, title, month)


    return HttpResponse("Hey, I appreciate the file. \n\n %s" % (report))

@csrf_exempt
def write_image_to_database(request):

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

    return HttpResponse(json.dumps(result))
