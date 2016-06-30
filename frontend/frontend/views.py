from django.shortcuts import render
from django.http import HttpResponse    
import requests
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core import serializers
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello")
def login(request):
    return HttpResponse("login1")
@ensure_csrf_cookie
def batchrecord(request):
    if request.method =='GET':
        print request.GET
    elif request.method == 'POST':
        print request.path
        print request.body
        #print request.POST
    return HttpResponse(request.body)
def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)
def user(request):
    r = requests.get('http://127.0.0.1:8001/api/v1/user')
    return HttpResponse(r.text)

