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
    page    = int(request.GET.get('page', 1))

    page    = (page - 1) if page >= 1 else 0

    def pagination(total_count, current_page, per_page):
        total_number_of_pg_num = 10
        page_num_aplha = 5
        if not total_count: return []
        total_pages = int(total_count / per_page) + 1
        page_list = [i for i in range(1, (total_pages + 1))]

        if len(page_list) < total_number_of_pg_num:
            return page_list

        final_list = []
        for i in page_list:
            min = (current_page-page_num_aplha)
            max = (current_page+page_num_aplha)
            if i > min and i < max:
                final_list.append(i)

        return final_list

    pb = ProductBrandsM()
    brand_list = pb.getList()
    total_count = pb.getTotal()

    data = {
        'brand_list'    : brand_list,
        'current_page'  : (page + 1),
        'total_count'   : total_count['cnt'],
        'pagination'    : pagination(total_count['cnt'], page, limit)
    }
    template = loader.get_template('brands/brand_list.html')
    return HttpResponse(template.render(data, request))
