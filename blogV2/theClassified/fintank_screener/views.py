from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from pytz import timezone
from requests import get
from django.conf import settings
from utils.StockCalculations import GetData
from utils.UniverseCalculations import UniverseData, StockScreener
from utils.PeerCalculations import PeerSpecificData
import urllib.parse
from rest_framework import status, mixins, generics, viewsets, parsers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from stockuploader.models import EuroStock, Stock, SP500, Nasdaq, TSX, Commoditie, ETF, ProfileStock, Crypto, Indexe
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import EuroSerializer, SP500Serializer, StockSerializer, ETFSerializer, NasdaqSerializer, TSXSerializer, CommoditieSerializer, IndexSerializer, CryptoSerializer, ScreenerSerializer
from django.db.models import Avg, Min, Max, Count
from .filters import SP500Filter, StockFilter, ETFFilter, NasdaqFilter, TSXFilter, CommoditiesFilter, IndexeFilter, CryptoFilter, EuroFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.

fmp_api_key = settings.FMP_API

@api_view(['GET'])
def get_all_stock_names_available(request):
    # Replace with new models just for stock names, not linked to user. 
    stocks = Stock.objects.all()
    serializer = StockSerializer(stocks, many=True)

    context = {
        'stocks':serializer.data
    }

    return Response(context)


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

@api_view(['POST'])
def run_stock_screener(request):
    
    market_cap_max_usr = request.data['market_cap_max'] != 'undefined' or None
    market_cap_min_usr = request.data['market_cap_min'] != 'undefined'or 0
    beta_max_usr = request.data['beta_max'] != 'undefined' or None
    beta_min_usr = request.data['beta_min'] != 'undefined' or None
    dividend_min_usr = request.data['dividend_min'] != 'undefined' or None
    sector_usr = request.data['sector'] != 'undefined' or None
    sub_industry_usr = request.data['sub_industry'] != 'undefined' or None
    price_max_usr = request.data['price_max'] != 'undefined' or None
    price_min_usr = request.data['price_min'] != 'undefined' or None
    country_usr = request.data['country'] != 'undefined' or None


    screener = StockScreener(market_cap_max=market_cap_max_usr, market_cap_min=market_cap_min_usr, 
                            dividend_min=dividend_min_usr,beta_max=beta_max_usr, beta_min=beta_min_usr,sector=sector_usr, 
                            sub_industry=sub_industry_usr,country=country_usr, price_max=price_max_usr, price_min=price_min_usr,
                            volume_max=None, volume_min=None, limit=10000)

    screen_results = screener.get_screen_results()

    context = {
        "screen_results":screen_results
    }


    return Response(context, status=status.HTTP_200_OK)

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
        serializer = SP500Serializer(queryset, many=True)
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

@api_view(['GET'])
def get_index_history(request, ticker):
    fmp_api_key = settings.FMP_API
    data_init = GetData(ticker, fmp_api_key, is_index=True)
    index_data = data_init.get_daily_index_stats()
    print(index_data.head())
    index_dates = [str(x)[0:10] for x in list(index_data.index)]
    index_prices = [x for x in list(index_data['close'])]

    context = {
        'index_dates':index_dates,
        'index_prices':index_prices
    }

    return Response(context)


@api_view(['GET'])
def get_daily_stock_data(request, ticker):
    fmp_api_key = settings.FMP_API

    data_init = GetData(ticker, fmp_api_key)
    data = data_init.get_daily_stats()
    daily_data = data[0]
    monthly_data = data[1]
    daily_dates = [str(x)[0:10] for x in list(daily_data.index)]
    daily_prices = [x for x in list(daily_data['close'])]

    day_30_returns = daily_data['30d_returns'].dropna()
    day_60_returns = daily_data['60d_returns'].dropna()
    day_90_returns = daily_data['90d_returns'].dropna()
    day_120_returns = daily_data['120d_returns'].dropna()
    year_1_returns = monthly_data['yearly_returns'].dropna()
    quarter_returns = monthly_data['quarterly_returns'].dropna()

    day_30_date_list = [str(x)[0:10] for x in list(day_30_returns.index)]
    day_30_return_list = [str(x)[0:10] for x in list(day_30_returns)]

    day_60_date_list = [str(x)[0:10] for x in list(day_60_returns.index)]
    day_60_return_list = [str(x)[0:10] for x in list(day_60_returns)]

    day_90_date_list = [str(x)[0:10] for x in list(day_90_returns.index)]
    day_90_return_list = [str(x)[0:10] for x in list(day_90_returns)]

    day_120_date_list = [str(x)[0:10] for x in list(day_120_returns.index)]
    day_120_return_list = [str(x)[0:10] for x in list(day_120_returns)]

    year_1_date_list = [str(x)[0:10] for x in list(year_1_returns.index)]
    year_1_return_list = [str(x)[0:10] for x in list(year_1_returns)]

    quarter_date_list = [str(x)[0:10] for x in list(quarter_returns.index)]
    quarter_return_list = [str(x)[0:10] for x in list(quarter_returns)]


    context = {
        'dates':daily_dates,
        'prices':daily_prices,
        'day_30_date_list':day_30_date_list,
        'day_30_return_list':day_30_return_list,
        'day_60_date_list':day_60_date_list,
        'day_60_return_list':day_60_return_list,
        'day_90_date_list':day_90_date_list,
        'day_90_return_list':day_90_return_list,
        'day_120_date_list':day_120_date_list,
        'day_120_return_list':day_120_return_list,
        'year_1_date_list':year_1_date_list,
        'year_1_return_list':year_1_return_list,
        'quarter_date_list':quarter_date_list,
        'quarter_return_list':quarter_return_list,
    }

    return Response(context)



@api_view(['GET'])
def get_weekly_stock_data(request, ticker):
    fmp_api_key = settings.FMP_API

    data_init = GetData(ticker, fmp_api_key)
    weekly_data = data_init.get_weekly_stats()

    return weekly_data

@api_view(['GET'])
def get_monthly_stock_data(request, ticker):
    fmp_api_key = settings.FMP_API


    data_init = GetData(ticker, fmp_api_key)
    monthly_data = data_init.get_monthly_stats()

    return monthly_data

@api_view(['GET'])
def get_stock_peer_list(request, ticker, universe):

    data_init = PeerSpecificData(ticker, universe)
    try:
        available_stocks = data_init.get_peer_chart_data()
        return Response(available_stocks)
    except:
        return Response('No Data Found for Peer Stocks Matching your Search, We continue to develop and build our resources to better serve you.')

@api_view(['GET'])
def get_sector_performance(request):

    data_init = UniverseData(fmp_api_key)
    sector_data = data_init.get_sector_returns()

    context = {
        'sector_data':sector_data[0],
        'sector_message':sector_data[1],
    }
    
    return Response(context)

@api_view(['GET'])
def get_sector_timeseries_data(request, frq):

    data_init = UniverseData(fmp_api_key)
    sector_return_time_series = data_init.get_sector_return_timeseries(frq)
    sector_vol_time_series = data_init.get_sector_vol_timeseries(frq)

    sector_time_series_context = {
        'return_time_series':sector_return_time_series,
        'vol_time_series':sector_vol_time_series
    }
    
    return Response(sector_time_series_context)

@api_view(['GET'])
def get_daily_gainer_loser_active(request):

    data_init = UniverseData(fmp_api_key)
    most_gainer, most_loser, most_active = data_init.get_most_gainer_loser_active()
    context = {
        'most_gainer':most_gainer,
        'most_loser':most_loser,
        'most_active':most_active
    }
    
    return Response(context)