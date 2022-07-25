# coding=utf-8
import logging

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

logging.basicConfig(
    level=logging.DEBUG
)


# Create your views here.

def index(request):
    return HttpResponse("welcome!")


def login(request):
    # request 是一个对象，封装了用户请求页面时发送过来的所有数据

    # 获取请求方法
    logging.warning(f"接收到用户的{request.method}请求")

    # POST请求
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        return JsonResponse({
            "username": username,
            "pwd": pwd
        })

    # 重定向
    # return redirect("https://blog.2fanbaby.cn")

    # 1. 优先去项目根目录的templates中寻找（需要在settings.py中的TEMPLATES DIR中添加
    #       os.path.join(BASE_DIR,"templates")）
    # 去app目录下的templates目录寻找html模板文件，根据app的注册顺序去逐一寻找
    return render(request, 'login.html')
