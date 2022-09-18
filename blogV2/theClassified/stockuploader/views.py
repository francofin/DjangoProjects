from django.shortcuts import render
import html5lib
from .models import Stock, SP500, Nasdaq, TSX, Commoditie, ETF, ProfileStock, Crypto, Indexe
from .resources import StockResource, SP500Resource, NasdaqResource, \
                        TSXResource, ETFResource, \
                        CommoditieResource, ProfileStockResource, CryptoResource, IndexResource
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset

def upload_template(request):
    if request.method == 'POST':
        stock_resource = StockResource()
        dataset = Dataset()
        new_stock = request.FILES['myfile']

        if not new_stock.name.endswith('xlsx'):
            messages.info(request, 'incorrect format')
            return render(request, 'upload.html')

        imported_dataset = dataset.load(new_stock.read(),format='xlsx')
        for data in imported_dataset:
            value = Stock(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                # data[6],
            )
            value.save()
    return render(request, 'upload.html')
# Create your views here.
