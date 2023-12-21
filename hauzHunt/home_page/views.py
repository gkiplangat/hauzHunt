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