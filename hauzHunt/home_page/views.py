from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
         'mymembers': mymembers,
    }
    #template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'users': ['Abel', 'Brian', 'Carol'],   
  }
  return HttpResponse(template.render(context, request))