from stockuploader.models import Stock, SP500, Nasdaq, TSX, Commoditie, ETF, Crypto, Indexe, EuroStock
from django_filters import rest_framework as filters



class StockFilter(filters.FilterSet):
    # gte is greater than ir equal to
    # lte is less than or equal to. 
    keyword = filters.CharFilter(field_name='name', lookup_expr='icontains')
    ticker = filters.CharFilter(field_name='symbol', lookup_expr='icontains')

    class Meta:
        model = Stock
        fields = ('ticker', 'keyword', 'exchange_short', 'exchange', 'universe')

class SP500Filter(filters.FilterSet):
    # gte is greater than ir equal to
    # lte is less than or equal to. 
    keyword = filters.CharFilter(field_name='name', lookup_expr='icontains')
    ticker = filters.CharFilter(field_name='symbol', lookup_expr='icontains')

    class Meta:
        model = SP500
        fields = ('ticker', 'keyword', 'sub_sector', 'sector')

class NasdaqFilter(filters.FilterSet):
    # gte is greater than ir equal to
    # lte is less than or equal to. 
    keyword = filters.CharFilter(field_name='name', lookup_expr='icontains')
    ticker = filters.CharFilter(field_name='symbol', lookup_expr='icontains')

    class Meta:
        model = Nasdaq
        fields = ('ticker', 'keyword', 'sub_sector', 'sector')


class TSXFilter(filters.FilterSet):
    # gte is greater than ir equal to
    # lte is less than or equal to. 
    keyword = filters.CharFilter(field_name='name', lookup_expr='icontains')
    ticker = filters.CharFilter(field_name='symbol', lookup_expr='icontains')
    class Meta:
        model = TSX
        fields = ('ticker', 'keyword', 'exchange')

class CommoditiesFilter(filters.FilterSet):
    # gte is greater than ir equal to
    # lte is less than or equal to. 
    keyword = filters.CharFilter(field_name='name', lookup_expr='icontains')
    ticker = filters.CharFilter(field_name='symbol', lookup_expr='icontains')

    class Meta:
        model = Commoditie
        fields = ('ticker', 'keyword', 'exchange', 'exchange_short', 'currency')

class IndexeFilter(filters.FilterSet):
    # gte is greater than ir equal to
    # lte is less than or equal to. 
    keyword = filters.CharFilter(field_name='name', lookup_expr='icontains')
    ticker = filters.CharFilter(field_name='symbol', lookup_expr='icontains')
    class Meta:
        model = Indexe
        fields = ('ticker', 'keyword')

class CryptoFilter(filters.FilterSet):
    # gte is greater than ir equal to
    # lte is less than or equal to. 
    keyword = filters.CharFilter(field_name='name', lookup_expr='icontains')
    ticker = filters.CharFilter(field_name='symbol', lookup_expr='icontains')
    class Meta:
        model = Crypto
        fields = ('ticker', 'keyword')

class ETFFilter(filters.FilterSet):
    # gte is greater than ir equal to
    # lte is less than or equal to. 
    keyword = filters.CharFilter(field_name='name', lookup_expr='icontains')
    ticker = filters.CharFilter(field_name='symbol', lookup_expr='icontains')
    class Meta:
        model = ETF
        fields = ('ticker', 'keyword', 'exchange')


class EuroFilter(filters.FilterSet):
    # gte is greater than ir equal to
    # lte is less than or equal to. 
    keyword = filters.CharFilter(field_name='name', lookup_expr='icontains')
    ticker = filters.CharFilter(field_name='symbol', lookup_expr='icontains')
    class Meta:
        model = EuroStock
        fields = ('ticker', 'keyword', 'currency')