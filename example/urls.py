from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^', include('example.website.urls')),
)