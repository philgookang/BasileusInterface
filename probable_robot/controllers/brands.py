from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../database')) )
from model import *

def index(request):
    data = {
        'brand_list': ProductBrandsM().getList()
    }
    template = loader.get_template('brands/brand_list.html')
    return HttpResponse(template.render(data, request))
