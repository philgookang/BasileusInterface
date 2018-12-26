from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../database')) )
from model import *
from ..helper.pagination import *

def tile(request):

    limit   = request.GET.get('limit', 210)
    page    = int(request.GET.get('page', 1))
    page    = (page - 1) if page >= 1 else 0

    pi = ProductImagesM()
    image_list = pi.getList( offset = (int(page)*int(limit)), sort_by = "idx", limit = limit)
    total_count = pi.getTotal()

    data = {
        'image_list' : image_list,
        'pagination' : pagination(total_count['cnt'], page, limit, "/images/tile?")
    }
    template = loader.get_template('images/image_tile.html')
    return HttpResponse(template.render(data, request))
