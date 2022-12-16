from rest_framework import serializers
from stockuploader.models import EuroStock, Stock, SP500, Nasdaq, TSX, Commoditie, ETF, ProfileStock, Crypto, Indexe

class StockSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    class Meta:
        model=Stock
        fields = '__all__'


class SP500Serializer(serializers.ModelSerializer):

    class Meta:
        model=SP500
        fields = '__all__'

class NasdaqSerializer(serializers.ModelSerializer):

    class Meta:
        model=Nasdaq
        fields = '__all__'

class TSXSerializer(serializers.ModelSerializer):

    class Meta:
        model=TSX
        fields = '__all__'

class CommoditieSerializer(serializers.ModelSerializer):

    class Meta:
        model=Commoditie
        fields = '__all__'

class CryptoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Crypto
        fields = '__all__'

class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model=Indexe
        fields = '__all__'


class ETFSerializer(serializers.ModelSerializer):

    class Meta:
        model=ETF
        fields = '__all__'

class EuroSerializer(serializers.ModelSerializer):

    class Meta:
        model=EuroStock
        fields = '__all__'


class ScreenerSerializer(serializers.Serializer):
    market_cap_max = serializers.IntegerField(default=None)
    market_cap_min=serializers.IntegerField(default=0)
    volume_max = serializers.IntegerField(default=None)
    volume_min = serializers.IntegerField(default=None)
    dividend_max = serializers.IntegerField(default=None)
    dividend_min = serializers.IntegerField(default=None)
    price_max = serializers.IntegerField(default=None)
    price_min = serializers.IntegerField(default=None)
    beta_max = serializers.IntegerField(default=None)
    beta_min = serializers.IntegerField(default=None)
    sector = serializers.IntegerField(default=None)
    sub_industry = serializers.IntegerField(default=None)
    is_etf = serializers.IntegerField(default=True)
    country = serializers.IntegerField(default=None)
    limit = serializers.IntegerField(default=None)
