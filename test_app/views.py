# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("welcome!")


def login(request):
    # 1. 优先去项目根目录的templates中寻找（需要在settings.py中的TEMPLATES DIR中添加
    #       os.path.join(BASE_DIR,"templates")）
    # 去app目录下的templates目录寻找html模板文件，根据app的注册顺序去逐一寻找
    return render(request, 'login.html')
