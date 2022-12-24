from django.shortcuts import render
import html5lib
from .models import Stock, SP500, Nasdaq, TSX, Commoditie, ETF, ProfileStock, Crypto, Indexe, EuroStock, FundamentalAttributes
from .resources import StockResource, SP500Resource, NasdaqResource, \
                        TSXResource, ETFResource, EuroResource,\
                        CommoditieResource, ProfileStockResource, CryptoResource, IndexResource, FundamentalAttributeResource
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset

def upload_template(request):
    if request.method == 'POST':
        stock_resource = FundamentalAttributeResource()
        dataset = Dataset()
        new_stock = request.FILES['myfile']

        if not new_stock.name.endswith('xlsx'):
            messages.info(request, 'incorrect format')
            return render(request, 'upload.html')

        imported_dataset = dataset.load(new_stock.read(),format='xlsx')
        for data in imported_dataset:
            value = FundamentalAttributes(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
                data[16],
                data[17],
                data[18],
                data[19],
                data[20],
                data[21],
                data[22],
                data[23],
                data[24],
                data[25],
                data[26],
                data[27],
                data[28],
                data[29],
                data[30],
                data[31],
                data[32],
                data[33],
                data[34],
                data[35],
                data[36],
                data[37],
                data[38],
                data[39],
                data[40],
                data[41],
                data[42],
                data[43],
                data[44],
                data[45],
                data[46],
                data[47],
                data[48],
                data[49],
                data[50],
                data[51],
                data[52],
                data[53],
                data[54],
                data[55],
                data[56],
                data[57],
                data[58],
                data[59],
                data[60],
            )
            value.save()
    return render(request, 'upload.html')
# Create your views here.
