from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def mainpage(request):
    template = loader.get_template("mainpage.html")
    return HttpResponse(template.render())



def homepage(request):
    template = loader.get_template("homepage.html")
    return HttpResponse(template.render())