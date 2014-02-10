from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Main Urls
    # %%%%%%%%%%% SHOULD DEFAULT THIS TO CURRENT YEAR AND MONTH %%%%%%%%%%%%%%
    url(r'^$', 'levsdelight_com.views.home', name='home'),
    url(r'^slideshow/(?P<year>\d{4})/(?P<month>[^/]+)/$', 'levsdelight_com.views.slideshow', name='slideshow'),

    url(r'^test_upload/$', 'levsdelight_com.views.test_upload', name='test_upload'),
    url(r'^sign_s3_upload/$', 'levsdelight_com.views.sign_s3_upload', name='file_upload'),
    url(r'^write_image_to_database/$', 'levsdelight_com.views.write_image_to_database', name='file_upload'),
    url(r'^get_signature_for_browser/$', 'levsdelight_com.views.get_signature_for_browser', name='get_signature'),
    # url(r'^levsdelight2/', include('levsdelight2.foo.urls')),

    # File coming from Mobile Device
    url(r'^uploadImage/$', 'levsdelight_com.views.upload_image', name='upload_image'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Login/Logout
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'levsdelight_com.views.logout_page'),


    # Needed for Heroku Deployment of Static Files
    # (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    
)
