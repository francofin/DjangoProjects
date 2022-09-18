from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stock, SP500, Nasdaq, TSX, Commoditie, ETF, Crypto, Indexe

# Register your models here.
@admin.register(Stock)
class StockAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'exchange', 'is_featured')
    search_fields = ('symbol', 'name', 'is_featured')

@admin.register(SP500)
class SP500Admin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'sector', 'date_first_added', 'cik')
    search_fields = ('symbol', 'name', 'sector')

@admin.register(Indexe)
class IndexAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name')
    search_fields = ('symbol', 'name')

@admin.register(Nasdaq)
class NasdaqAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'sector', 'founded')
    search_fields = ('symbol', 'name', 'sector')

@admin.register(TSX)
class TSXAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'exchange', 'currency')
    search_fields = ('symbol', 'name', 'currency')

@admin.register(Commoditie)
class CommoditiesAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'exchange', 'currency', 'exchange_short')
    search_fields = ('symbol', 'name', 'currency', 'exchange_short')

@admin.register(ETF)
class ETFAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'exchange', 'exchange_short')
    search_fields = ('symbol', 'name', 'exchange_short')

@admin.register(Crypto)
class CryptoAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'exchange', 'currency')
    search_fields = ('symbol', 'name', 'currency', 'exchange')