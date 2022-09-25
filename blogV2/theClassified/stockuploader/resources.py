from import_export import resources
from .models import Stock, SP500, Nasdaq, TSX, Commoditie, ETF, ProfileStock, Crypto, Indexe, EuroStock


class StockResource(resources.ModelResource):

    class meta:
        model = Stock

class ProfileStockResource(resources.ModelResource):

    class meta:
        model = ProfileStock

class SP500Resource(resources.ModelResource):

    class meta:
        model = SP500

class NasdaqResource(resources.ModelResource):

    class meta:
        model = Nasdaq

class TSXResource(resources.ModelResource):

    class meta:
        model = TSX

class CommoditieResource(resources.ModelResource):

    class meta:
        model = Commoditie

class ETFResource(resources.ModelResource):

    class meta:
        model = ETF

class CryptoResource(resources.ModelResource):

    class meta:
        model = Crypto

class IndexResource(resources.ModelResource):

    class meta:
        model = Indexe

class EuroResource(resources.ModelResource):

    class meta:
        model = EuroStock