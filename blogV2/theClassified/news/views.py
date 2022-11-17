from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from pytz import timezone
from requests import get
from django.conf import settings
import urllib.parse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .tasks import economic_articles, market_articles, political_articles, inflation_articles, war_articles, \
                    us_articles, china_articles, russia_articles, mid_east_articles, german_articles, japan_articles, africa_articles, \
                    southam_articles, tech_articles, energy_articles, oil_articles, pharma_articles, fin_articles, cons_articles, \
                    mat_articles, util_articles, ind_articles

# Create your views here.
econ = economic_articles.apply_async()
market = market_articles.apply_async()
politics = political_articles.apply_async()
inflation = inflation_articles.apply_async()
war = war_articles.apply_async()
us = us_articles.apply_async()
china = china_articles.apply_async()
russia = russia_articles.apply_async()
mid_east = mid_east_articles.apply_async()
germany = german_articles.apply_async()
japan = japan_articles.apply_async()
africa = africa_articles.apply_async()
southam = southam_articles.apply_async()
tech = tech_articles.apply_async()
energy = energy_articles.apply_async()
oil = oil_articles.apply_async()
pharma = pharma_articles.apply_async()
finance = fin_articles.apply_async()
cons = cons_articles.apply_async()
mat = mat_articles.apply_async()
util = util_articles.apply_async()
indus = ind_articles.apply_async()

@api_view(['GET'])
def get_econ_news(request):
    data = econ.get()
    print(data)
    context = {
        'data':data,
        'tag':"Economy"
    }
    
    return Response(context)

@api_view(['GET'])
def get_market_news(request):
    data = market.get()
    print("Data", data)
    context = {
        'data':data,
        'tag':"Markets"
    }
    
    return Response(context)
