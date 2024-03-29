from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stock, SP500, Nasdaq, TSX, Commoditie, ETF, Crypto, Indexe, EuroStock, IncomeStatement, CashFlowStatement, BalanceSheet, FundamentalAttributes, ProfileStock

# Register your models here.
@admin.register(Stock)
class StockAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'exchange', 'is_featured', 'universe')
    search_fields = ('symbol', 'name', 'is_featured', 'universe')

@admin.register(SP500)
class SP500Admin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'sector', 'date_first_added', 'cik', 'universe')
    search_fields = ('symbol', 'name', 'sector')

@admin.register(Indexe)
class IndexAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'is_featured', 'is_for_homepage')
    search_fields = ('symbol', 'name', 'is_featured', 'is_for_homepage')

@admin.register(Nasdaq)
class NasdaqAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'sector', 'founded', 'universe')
    search_fields = ('symbol', 'name', 'sector')

@admin.register(TSX)
class TSXAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'exchange', 'currency', 'universe')
    search_fields = ('symbol', 'name', 'currency')

@admin.register(Commoditie)
class CommoditiesAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'exchange', 'currency', 'exchange_short')
    search_fields = ('symbol', 'name', 'currency', 'exchange_short')

@admin.register(ETF)
class ETFAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'exchange', 'exchange_short', 'universe')
    search_fields = ('symbol', 'name', 'exchange_short')

@admin.register(Crypto)
class CryptoAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'exchange', 'currency')
    search_fields = ('symbol', 'name', 'currency', 'exchange')

@admin.register(EuroStock)
class Eurodmin(ImportExportModelAdmin):
    list_display = ('symbol', 'name', 'exchange', 'currency', 'universe')
    search_fields = ('symbol', 'name', 'currency', 'exchange')

@admin.register(IncomeStatement)
class ISAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'date', 'currency', 'period')
    search_fields = ('symbol', 'date', 'currency', 'period')

@admin.register(CashFlowStatement)
class CFAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'date', 'currency', 'period')
    search_fields = ('symbol', 'date', 'currency', 'period')

@admin.register(BalanceSheet)
class BSAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'date', 'currency', 'period')
    search_fields = ('symbol', 'date', 'currency', 'period')


@admin.register(FundamentalAttributes)
class FaAdmin(ImportExportModelAdmin):
    list_display = ('symbol',)
    search_fields = ('symbol',)