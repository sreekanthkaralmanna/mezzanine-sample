from django.conf.urls.defaults import patterns, url, include
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('zone.views',
    url(r'^zone/$', 'zone'),
    url(r'^expand/$', 'main'),
    url(r'^thankyou/', 'thankyou'),
    url(r'^contact/', 'contactview'),
    url(r'^reach_us/$', 'reach_us'),

)