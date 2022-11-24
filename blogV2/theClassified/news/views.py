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
                    mat_articles, util_articles, ind_articles, re_articles, comm_articles

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
re = re_articles.apply_async()
comm = comm_articles.apply_async()


@api_view(['GET'])
def get_comm_news(request):
    data = comm.get()
    context = {
        'data':data,
        'tag':"Communications"
    }
    
    return Response(context)

@api_view(['GET'])
def get_re_news(request):
    data = re.get()
    context = {
        'data':data,
        'tag':"Real Estate"
    }
    
    return Response(context)

@api_view(['GET'])
def get_util_news(request):
    data = util.get()
    context = {
        'data':data,
        'tag':"Utilities"
    }
    
    return Response(context)

@api_view(['GET'])
def get_indus_news(request):
    data = indus.get()
    context = {
        'data':data,
        'tag':"Industrials"
    }
    
    return Response(context)

@api_view(['GET'])
def get_cons_news(request):
    data = cons.get()
    context = {
        'data':data,
        'tag':"Consumer trends"
    }
    
    return Response(context)

@api_view(['GET'])
def get_mat_news(request):
    data = mat.get()
    context = {
        'data':data,
        'tag':"Basic Materials"
    }
    
    return Response(context)

@api_view(['GET'])
def get_energy_news(request):
    data = energy.get()
    context = {
        'data':data,
        'tag':"Energy"
    }
    
    return Response(context)

@api_view(['GET'])
def get_oil_news(request):
    data = oil.get()
    context = {
        'data':data,
        'tag':"Oil"
    }
    
    return Response(context)

@api_view(['GET'])
def get_finance_news(request):
    data = finance.get()
    context = {
        'data':data,
        'tag':"Finance"
    }
    
    return Response(context)

@api_view(['GET'])
def get_pharma_news(request):
    data = pharma.get()
    context = {
        'data':data,
        'tag':"Health Care"
    }
    
    return Response(context)

@api_view(['GET'])
def get_tech_news(request):
    data = tech.get()
    context = {
        'data':data,
        'tag':"Technology"
    }
    
    return Response(context)

@api_view(['GET'])
def get_southam_news(request):
    data = southam.get()
    context = {
        'data':data,
        'tag':"LatAm"
    }
    
    return Response(context)

@api_view(['GET'])
def get_africa_news(request):
    data = africa.get()
    context = {
        'data':data,
        'tag':"Africa"
    }
    
    return Response(context)

@api_view(['GET'])
def get_japan_news(request):
    data = japan.get()
    context = {
        'data':data,
        'tag':"Japan"
    }
    
    return Response(context)

@api_view(['GET'])
def get_germany_news(request):
    data = germany.get()
    context = {
        'data':data,
        'tag':"Germany"
    }
    
    return Response(context)


@api_view(['GET'])
def get_mid_east_news(request):
    data = mid_east.get()
    context = {
        'data':data,
        'tag':"Middle East"
    }
    
    return Response(context)

@api_view(['GET'])
def get_econ_news(request):
    data = econ.get()
    context = {
        'data':data,
        'tag':"Economy"
    }
    
    return Response(context)

@api_view(['GET'])
def get_market_news(request):
    data = market.get()
    context = {
        'data':data,
        'tag':"Markets"
    }
    
    return Response(context)

@api_view(['GET'])
def get_politics_news(request):
    data = politics.get()
    context = {
        'data':data,
        'tag':"Politics"
    }
    
    return Response(context)

@api_view(['GET'])
def get_war_news(request):
    data = war.get()
    context = {
        'data':data,
        'tag':"War"
    }
    
    return Response(context)

@api_view(['GET'])
def get_inflation_news(request):
    data = inflation.get()
    context = {
        'data':data,
        'tag':"Inflation"
    }
    
    return Response(context)

@api_view(['GET'])
def get_us_news(request):
    data = us.get()
    context = {
        'data':data,
        'tag':"US"
    }
    
    return Response(context)


@api_view(['GET'])
def get_china_news(request):
    data = china.get()
    context = {
        'data':data,
        'tag':"China"
    }
    
    return Response(context)

@api_view(['GET'])
def get_russia_news(request):
    data = russia.get()
    context = {
        'data':data,
        'tag':"Russia"
    }
    
    return Response(context)