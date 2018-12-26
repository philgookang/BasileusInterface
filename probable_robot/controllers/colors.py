from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../database')) )
from model import *

def index(request):

    color_replacement = {
        "black"     : "블랙",
        "beige"     : "베이지",
        "mint"      : "민트",
        "white"     : "화이트",
        "red"       : "빨간색",
        "brown"     : "갈색",
        "navy"      : "네이비",
        "grey"      : "",
        "yellow" : "노란색",
        "light blue" : "라이트 블루",
        "PINK" : "",
        "(옐로우)" : "",

        "[ORANGE]" : "",
        "(그레이)" : "",
        "(브라운)" : "",
        "(Lime)" : "",
        "[와인]" : "",
        " [페일 민트]" : "",
        " [골드]" : "",

        "[민트]" : "",

        "(카멜)" : "",
        "(BLUE)" : "블루",
        "(Green)" : "초록색",
        "(오렌지)" : "오렌지",
        "(검정)"      : "검정",
        "(로맨스 그레이)" : "로맨스 그레이",
        "(화이트)" : "화이트",
        "(핑크)" : "핑크",
        "[페일 베이지]" : "페일 베이지",
        "[아이보리]" : "아이보리",
        "(블루)" : "블루",
        "[카키]" : "",
        "metal silver " : ""
    }
    # []
    # ()




    data = {
        'color_list': []
    }
    template = loader.get_template('colors/color_list.html')
    return HttpResponse(template.render(data, request))
