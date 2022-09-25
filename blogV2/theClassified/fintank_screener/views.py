from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from pytz import timezone
from requests import get
import urllib.parse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from stockuploader.models import EuroStock, Stock, SP500, Nasdaq, TSX, Commoditie, ETF, ProfileStock, Crypto, Indexe
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import EuroSerializer, SP500Serializer, StockSerializer, ETFSerializer, NasdaqSerializer, TSXSerializer, CommoditieSerializer, IndexSerializer, CryptoSerializer
from django.db.models import Avg, Min, Max, Count
from .filters import SP500Filter, StockFilter, ETFFilter, NasdaqFilter, TSXFilter, CommoditiesFilter, IndexeFilter, CryptoFilter, EuroFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.


@api_view(['GET'])
def get_all_indexes(request):
    filterSet = IndexeFilter(request.GET, queryset=Indexe.objects.all().order_by('id'))

    count = filterSet.qs.count()
    print(count)

    results_per_page = 10
    paginator = PageNumberPagination()
    paginator.page_size = results_per_page
    myPages = paginator.paginate_queryset(filterSet.qs, request)
    serializer = IndexSerializer(myPages, many=True)

    context = {
        'count':count,
        'results_per_page':results_per_page,
        'indexes': serializer.data,
    }
    return Response(context)

@api_view(['GET'])
def get_stock(request, ticker):
    filterSet = Stock.objects.filter(symbol =ticker)


    serializer = StockSerializer(filterSet, many=True)

    context = {
        'stock': serializer.data,
    }
    return Response(context)

@api_view(['GET'])
def get_homepage_indexes(request):
    filterSet = Indexe.objects.filter(is_for_homepage=True).order_by('id')

    count = filterSet.count()
    index_symbols = list(filterSet)
    symbol_strings = [str(x) for x in index_symbols]
    query_string = ",".join(symbol_strings)
    
    serializer = IndexSerializer(filterSet, many=True)

    print(query_string)

    context = {
        'count':count,
        'indexes': serializer.data,
    }
    return Response(context)

@api_view(['GET'])
def get_market_indexes(request):
    filterSet = Indexe.objects.filter(is_featured=True).order_by('id')

    count = filterSet.count()
    index_symbols = list(filterSet)
    symbol_strings = [str(x) for x in index_symbols]
    query_string = ",".join(symbol_strings)
    
    serializer = IndexSerializer(filterSet, many=True)

    print(query_string)

    context = {
        'count':count,
        'indexes': serializer.data,
    }
    return Response(context)

@api_view(['GET'])
def get_stock_universe(request, universe):
    if universe == 'sp500':
        filterSet = SP500Filter(request.GET, queryset=SP500.objects.all().order_by('id'))
    elif universe == 'nasdaq':
        filterSet = NasdaqFilter(request.GET, queryset= Nasdaq.objects.all().order_by('id'))
    elif universe == 'sptsx':
        filterSet = TSXFilter(request.GET, queryset=TSX.objects.all().order_by('id'))
    elif universe == 'eurostocks':
        filterSet = EuroFilter(request.GET, queryset=EuroStock.objects.all().order_by('id'))
    elif universe == 'etfs':
        filterSet = ETFFilter(request.GET, queryset=ETF.objects.all().order_by('id'))
    elif universe == 'allstocks':
        filterSet = StockFilter(request.GET, queryset=Stock.objects.all().order_by('id'))
    elif universe == 'commodities':
        filterSet = CommoditiesFilter(request.GET, queryset=Commoditie.objects.all().order_by('id'))
    elif universe == 'cryptos':
        filterSet = CryptoFilter(request.GET, queryset=Crypto.objects.all().order_by('id'))

    count = filterSet.qs.count()
    results_per_page = 20
    paginator = PageNumberPagination()
    paginator.page_size = results_per_page
    queryset = paginator.paginate_queryset(filterSet.qs, request)

    if universe == 'sp500':
        serializer = SP500Serializer(filterSet.qs, many=True)
    elif universe == 'nasdaq':
        serializer = NasdaqSerializer(filterSet.qs, many=True)
    elif universe == 'sptsx':
        serializer = TSXSerializer(filterSet.qs, many=True)
    elif universe == 'eurostocks':
        serializer = EuroSerializer(filterSet.qs, many=True)
    elif universe == 'etfs':
        serializer = ETFSerializer(filterSet.qs, many=True)
    elif universe == 'allstocks':
        serializer = StockSerializer(filterSet.qs, many=True)
    elif universe == 'commodities':
        serializer = CommoditieSerializer(filterSet.qs, many=True)
    elif universe == 'cryptos':
        serializer = CryptoSerializer(filterSet.qs, many=True)

    # print(serializer.data)

    context = {
        'count':count,
        'results_per_page':results_per_page,
        'items': serializer.data,
    }
    return Response(context)



@api_view(['GET'])
def get_company_location(request, address):
    address = address
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

    response = get(url).json()
    latitude = response[0]["lat"]
    longitude = response[0]["lon"]
    context={
        "long":longitude,
        "lat":latitude
    }
    return Response(context)