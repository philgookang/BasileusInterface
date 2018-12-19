from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../database')) )
from model import *

def index(request):

    limit   = request.GET.get('limit', 30)
    page    = int(request.GET.get('page', 1))
    page    = (page - 1) if page >= 1 else 0

    ml_exclude_price   = request.GET.get('ml_exclude_price', None)
    ml_exclude_lang    = request.GET.get('ml_exclude_lang', None)
    hide_orgi_name     = request.GET.get('hide_orgi_name', None)
    search_name        = request.GET.get('search_name', '')
    search_name_ori    = request.GET.get('search_name_ori', '')

    def retrieveMore(product):
        pi = ProductImagesM()
        pi.sort_idx         = 0
        pi.product_idx      = product['idx']
        product['image']    = pi.get()

        pc1 = ProductCategoriesM()
        pc1.idx = product['category_1_idx']
        product['category_1'] = pc1.get()

        pc2 = ProductCategoriesM()
        pc2.idx = product['category_2_idx']
        product['category_2'] = pc2.get()

        pb = ProductBrandsM()
        pb.idx = product['brand_idx']
        product['brand'] = pb.get()

        return product

    pm = ProductsM()
    if ml_exclude_price == '1': pm.ml_exclude_price = 0
    if ml_exclude_lang == '1':  pm.ml_exclude_lang  = 0
    if search_name != '': pm.search_name = search_name
    if search_name_ori != '': pm.search_name_ori = search_name_ori
    product_list = pm.getList( offset=(int(page)*int(limit)), limit=limit  )
    product_list = list(map(retrieveMore, product_list))
    total_count = pm.getTotal()

    def pagination(total_count, current_page, per_page):
        total_number_of_pg_num = 20
        page_num_aplha = 10
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

    data = {
        'product_list'      : product_list,
        'current_page'      : (page + 1),
        'total_count'       : total_count['cnt'],
        'ml_exclude_price'  : ml_exclude_price,
        'ml_exclude_lang'   : ml_exclude_lang,
        'hide_orgi_name'    : hide_orgi_name,
        'search_name'       : search_name,
        'search_name_ori'   : search_name_ori,
        'pagination'        : pagination(total_count['cnt'], page, limit)
    }
    template = loader.get_template('products/product_list.html')
    return HttpResponse(template.render(data, request))
