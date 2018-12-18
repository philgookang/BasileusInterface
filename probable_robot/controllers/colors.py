from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../database')) )
from model import *

def index(request):
    data = {
        'color_list': ProductColorsM().getList()
    }
    template = loader.get_template('colors/color_list.html')
    return HttpResponse(template.render(data, request))
