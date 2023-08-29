from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import membership



def all_members(request):
    mymembers = membership.objects.all().values()

    template = loader.get_template("all_members.html") 

    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def info(request, id):
  mymember = membership.objects.get(id=id)
  template = loader.get_template('info.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))



def mainpage(request):
    template = loader.get_template("mainpage.html")
    return HttpResponse(template.render())



def homepage(request):
    template = loader.get_template("homepage.html")
    return HttpResponse(template.render())