from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache  # 缓存相关
from django.views.decorators.cache import cache_page  # 页面缓存相关
import json


# Create your views here.
def write_to_cache(request):
    key = 'hello'  # key值可以从前端获取
    cache.set(key, json.dumps('hello world!'), settings.NEVER_REDIS_TIMEOUT)
    return render(request, 'test.html')

def read_from_cache(request):
    key = 'hello'
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return render(request, 'test.html', locals())

@cache_page(10)
def abc(request):
    print('##########')
    return render(request, 'test.html')

def hello_views(request):
    return render(request, 'hello.html')
