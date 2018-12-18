from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../database')) )
from model import *

def index(request):

    limit   = request.GET.get('limit', 20)
    page    = request.GET.get('page', 1)

    pm = ProductsM()
    product_list = pm.getList( offset=(int(page)*int(limit)), limit=limit  )

    data = {
        'product_list'  : product_list,
        'pagination'    : Paginator(product_list, limit)
    }
    template = loader.get_template('products/product_list.html')
    return HttpResponse(template.render(data, request))
