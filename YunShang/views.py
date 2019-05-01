from django.shortcuts import render
from django.http import HttpResponse
from .import views
import captcha
def index(request):
    return render(request,'index.html')

# Create your views here.
def username(request,cl_username):
    return  HttpResponse('用户名:%s'% cl_username)


def verification(req):
    return render(req,'signup.html')