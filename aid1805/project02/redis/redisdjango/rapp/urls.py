from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$', write_to_cache, name='index'),
    url(r'^show/', read_from_cache, name='show'),
    url(r'^m/', abc, name='m'),
    url(r'^hello/', hello_views),
]
