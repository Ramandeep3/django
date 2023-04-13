from django.shortcuts import render,HttpResponse

# Create your views here.
def index(requset):
    return HttpResponse("THIS IS HOME PAGE")