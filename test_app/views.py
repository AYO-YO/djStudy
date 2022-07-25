# coding=utf-8
import logging

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View

logging.basicConfig(
    level=logging.DEBUG
)


# Create your views here.
class Login(View):
    def get(self, request: WSGIRequest):
        return render(request, "login.html")

    def post(self, request: WSGIRequest):
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        logging.info(f"{username},{pwd}")
        return JsonResponse({
            "username": username,
            "pwd": pwd
        })

    def put(self, request):
        return HttpResponseForbidden
