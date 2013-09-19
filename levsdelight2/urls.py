from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'levsdelight_com.views.home', name='home'),
    url(r'^test_upload/$', 'levsdelight_com.views.test_upload', name='test_upload'),
    url(r'^sign_s3_upload/$', 'levsdelight_com.views.sign_s3_upload', name='file_upload'),
    # url(r'^levsdelight2/', include('levsdelight2.foo.urls')),

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
