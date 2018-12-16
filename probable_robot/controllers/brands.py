from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {
        'latest_question_list': [ ]
    }
    template = loader.get_template('brands/brand_list.html')
    return HttpResponse(template.render(context, request))
