from django.shortcuts import render
from django.http import HttpResponse                                                                                   
from . import logic
# Create your views here.
def index(request):
    return HttpResponse("Hello")
def user(request):
    if request.method == 'GET':
        return HttpResponse(logic.userInfo(request))
    elif request.method == 'POST':
        return HttpResponse(logic.saveUserInfo(request))

    return HttpResponse("{'user':1}")
def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)




############################# function below #############
