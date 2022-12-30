from django.db import models
from django.conf import settings


# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=300)
    name = models.CharField(max_length=300, default="")
    exchange = models.CharField(max_length=300, default="", null=True)
    exchange_short = models.CharField(max_length=300, default="", null=True)
    universe = models.CharField(max_length=200, null=True, blank=True, default=None)
    stock_type = models.CharField(max_length=300,default="", null=True)
    
    is_featured = models.BooleanField(default=True, null=True)
    owner_count = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.symbol


class ProfileStock(models.Model):
    name = models.CharField(max_length=300, null=False)
    symbol = models.CharField(max_length=300, default="")
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='portfolio')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symbol


class Nasdaq(models.Model):
    symbol = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    sector = models.CharField(max_length=300)
    sub_sector = models.CharField(max_length=300)
    founded = models.CharField(max_length=300, null=True)
    cik = models.IntegerField(max_length=400, default=None, blank=True, null=True)
    universe = models.CharField(max_length=200, null=True, blank=True, default=None)

    def __str__(self):
        return self.symbol

class TSX(models.Model):
    symbol = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    currency = models.CharField(max_length=300)
    exchange = models.CharField(max_length=300, default=" ")
    universe = models.CharField(max_length=200, null=True, blank=True, default=None)

    def __str__(self):
        return self.symbol

class ETF(models.Model):
    symbol = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    exchange = models.CharField(max_length=300, default="", null=True)
    exchange_short = models.CharField(max_length=300, default="", null=True)
    universe = models.CharField(max_length=200, null=True, blank=True, default=None)
    def __str__(self):
        return self.symbol


class Commoditie(models.Model):
    symbol = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    currency = models.CharField(max_length=300)
    exchange = models.CharField(max_length=300, default="", null=True)
    exchange_short = models.CharField(max_length=300, default="", null=True)

    def __str__(self):
        return self.symbol

class Indexe(models.Model):
    symbol = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=False)
    is_for_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.symbol

class Crypto(models.Model):
    symbol = models.CharField(max_length = 200)
    name = models.CharField(max_length=300, null=True, blank=True)
    currency = models.CharField(max_length=200, null=True)
    exchange = models.CharField(max_length=300, default="", null=True)
    def __str__(self):
        return self.symbol

class EuroStock(models.Model):
    symbol = models.CharField(max_length = 200)
    name = models.CharField(max_length=300)
    currency = models.CharField(max_length=200, null=True)
    exchange = models.CharField(max_length=300, default="", null=True)
    universe = models.CharField(max_length=200, null=True, blank=True, default=None)
    def __str__(self):
        return self.symbol

class SP500(models.Model):
    symbol = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    sector = models.CharField(max_length=300, null=True)
    sub_sector = models.CharField(max_length=300, null=True)
    founded = models.CharField(max_length=300, null=True)
    date_first_added=models.DateTimeField(auto_now_add=False, null=True, blank=True)
    cik = models.IntegerField(max_length=400, default=None, blank=True, null=True)
    universe = models.CharField(max_length=200, null=True, blank=True, default=None)

    def __str__(self):
        return self.symbol


class IncomeStatement(models.Model):
    date = models.DateTimeField(auto_now_add=False, null=True)
    symbol = models.CharField(max_length=300)
    currency = models.CharField(max_length=300)
    cik = models.CharField(max_length=300, null=True)
    calendar_year = models.CharField(max_length=300, null=True)
    period = models.CharField(max_length=300, null=True)
    revenue=models.IntegerField(default=0, blank=True, null=True)
    cost_of_revenue = models.IntegerField(max_length=400, default=0, blank=True, null=True)
    gross_profit = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    gross_profit_ratio = models.FloatField(max_length=400, null=True, blank=True, default=0.0)
    research_and_development_expenses = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    general_and_administrative_expenses = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    selling_and_marketing_expenses = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    selling_general_and_admin_expenses = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_expenses = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    operating_expenses = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    cost_and_expenses = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    interest_income = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    interest_expense = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    depreciation_and_amortization = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    ebitda = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    ebitda_ratio = models.FloatField(max_length=400, null=True, blank=True, default=0.0)
    operating_income = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    operating_income_ratio = models.FloatField(max_length=400, null=True, blank=True, default=0.0)
    total_other_income_expense = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    income_before_tax = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    income_before_tax_ratio = models.FloatField(max_length=400, null=True, blank=True, default=0.0)
    income_tax_expense = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    net_income = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    net_income_ratio = models.FloatField(max_length=400, null=True, blank=True, default=0.0)
    eps = models.FloatField(max_length=400, null=True, blank=True, default=0.0)
    epsdiluted = models.FloatField(max_length=400, null=True, blank=True, default=0.0)
    weighted_average_shs_out = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    weighted_average_shs_out_dil = models.IntegerField(max_length=400, null=True, blank=True, default=0)

    def __str__(self):
        return self.symbol

class CashFlowStatement(models.Model):
    date = models.DateTimeField(auto_now_add=False, null=True)
    symbol = models.CharField(max_length=300)
    currency = models.CharField(max_length=300)
    cik = models.CharField(max_length=300, null=True)
    calendar_year = models.CharField(max_length=300, null=True)
    period = models.CharField(max_length=300, null=True)
    net_income=models.IntegerField(default=0, blank=True, null=True)
    depreciation_and_amortization = models.IntegerField(max_length=400, default=0, blank=True, null=True)
    deferred_income_tax = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    stock_based_compensation = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    change_in_working_capital = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    accounts_receivables = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    inventory = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    accounts_payables = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_working_capital = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_non_cash_items = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    net_cash_provided_by_operating_activities = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    investments_in_property_plant_and_equipment = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    acquisitions_net = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    purchases_of_investments = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    sales_maturities_of_investments = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_investing_activites = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    net_cash_used_for_investing_activites = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    debt_repayment = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    common_stock_issued = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    common_stock_repurchased = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    dividends_paid = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_financing_activites = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    net_cash_used_provided_by_financing_activities = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    effect_of_forex_changes_on_cash = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    net_change_in_cash = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    cash_at_end_of_period = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    cash_at_beginning_of_period = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    operating_cash_flow = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    capital_expenditure = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    free_cash_flow = models.IntegerField(max_length=400, null=True, blank=True, default=0)

    def __str__(self):
        return self.symbol


class BalanceSheet(models.Model):
    date = models.DateTimeField(auto_now_add=False, null=True)
    symbol = models.CharField(max_length=300)
    currency = models.CharField(max_length=300)
    cik = models.CharField(max_length=300, null=True)
    calendar_year = models.CharField(max_length=300, null=True)
    period = models.CharField(max_length=300, null=True)
    cash_and_cash_equivalents=models.IntegerField(default=0, blank=True, null=True)
    short_term_investments = models.IntegerField(max_length=400, default=0, blank=True, null=True)
    cash_and_short_term_investments = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    net_receivables = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    inventory = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_current_assets = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_current_assets = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    property_plant_equipmentNet = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    goodwill = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    intangibleAssets = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    long_term_investments = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    tax_assets = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_non_current_assets = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_non_current_assets = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_assets = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_assets = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    short_term_debt = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    tax_payables = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    deferred_revenue = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_current_liabilities = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_current_liabilities = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    long_term_debt = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    deferred_revenue_non_current = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_non_current_liabilities = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_non_current_liabilities = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_liabilities = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    capital_lease_obligations = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_liabilities = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    preferred_stock = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    common_stock = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    retained_earnings = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    accumulated_other_comprehensive_income_loss = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    other_total_stockholders_equity = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_stockholders_equity = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_liabilities_and_stockholders_equity = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    minority_interest = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_equity = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_liabilities_and_total_equity = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_investments = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    total_debt = models.IntegerField(max_length=400, null=True, blank=True, default=0)
    net_debt = models.IntegerField(max_length=400, null=True, blank=True, default=0)

    def __str__(self):
        return self.symbol


class FundamentalAttributes(models.Model):
    symbol = models.CharField(max_length=300, null=False, blank=False)
    revenue_per_share = models.FloatField(null=True, blank=True, default=0)
    net_income_per_share = models.FloatField(null=True, blank=True, default=0)
    operating_cash_flow_per_share = models.FloatField(null=True, blank=True, default=0)
    free_cash_flow_per_share = models.FloatField(null=True, blank=True, default=0)
    cash_per_share = models.FloatField(null=True, blank=True, default=0)
    book_value_per_share = models.FloatField(null=True, blank=True, default=0)
    tangible_book_value_per_share = models.FloatField(null=True, blank=True, default=0)
    shareholders_equity_per_share = models.FloatField(null=True, blank=True, default=0)
    interest_debt_per_share = models.FloatField(null=True, blank=True, default=0)
    market_cap = models.FloatField(null=True, blank=True, default=0)
    enterprise_value = models.FloatField(null=True, blank=True, default=0)
    price_to_earnings_ratio = models.FloatField(null=True, blank=True, default=0)
    psales_ratio = models.FloatField(null=True, blank=True, default=0)
    price_to_operating_cashflow = models.FloatField(null=True, blank=True, default=0)
    price_to_cashflow = models.FloatField(null=True, blank=True, default=0)
    price_to_book_ratio = models.FloatField(null=True, blank=True, default=0)
    # drop ptbRatio
    enterprise_value_to_sales = models.FloatField(null=True, blank=True, default=0)
    enterprise_value_to_ebitda = models.FloatField(null=True, blank=True, default=0)
    ev_to_operating_cash_flow = models.FloatField(null=True, blank=True, default=0)
    ev_to_free_cash_flow = models.FloatField(null=True, blank=True, default=0)
    earnings_yield = models.FloatField(null=True, blank=True, default=0)
    free_cash_flow_yield = models.FloatField(null=True, blank=True, default=0)
    debt_to_equity = models.FloatField(null=True, blank=True, default=0)
    debt_to_assets = models.FloatField(null=True, blank=True, default=0)
    net_debt_to_ebitda = models.FloatField(null=True, blank=True, default=0)
    current_ratio = models.FloatField(null=True, blank=True, default=0)
    interest_coverage = models.FloatField(null=True, blank=True, default=0)
    income_quality = models.FloatField(null=True, blank=True, default=0)
    dividend_yield = models.FloatField(null=True, blank=True, default=0)
    dividend_yield_percent = models.FloatField(null=True, blank=True, default=0)
    payout_ratio = models.FloatField(null=True, blank=True, default=0)
    sales_and_genral_admin_to_revenue = models.FloatField(null=True, blank=True, default=0)
    research_and_development_to_revenue = models.FloatField(null=True, blank=True, default=0)
    intangibles_to_total_assets = models.FloatField(null=True, blank=True, default=0)
    capex_to_operating_cash_flow = models.FloatField(null=True, blank=True, default=0)
    capex_to_revenue = models.FloatField(null=True, blank=True, default=0)
    capex_to_depreciation = models.FloatField(null=True, blank=True, default=0)
    stock_based_copensation_to_revenue = models.FloatField(null=True, blank=True, default=0)
    graham_number = models.FloatField(null=True, blank=True, default=0)
    return_on_invested_capital = models.FloatField(null=True, blank=True, default=0)
    return_on_tangible_assets = models.FloatField(null=True, blank=True, default=0)
    net_graham_number = models.FloatField(null=True, blank=True, default=0)
    working_capital = models.FloatField(null=True, blank=True, default=0)
    tangible_asset_value = models.FloatField(null=True, blank=True, default=0)
    net_current_asset_value = models.FloatField(null=True, blank=True, default=0)
    invested_capital = models.FloatField(null=True, blank=True, default=0)
    average_recievables = models.FloatField(null=True, blank=True, default=0)
    average_payables = models.FloatField(null=True, blank=True, default=0)
    average_inventory = models.FloatField(null=True, blank=True, default=0)
    days_sales_outstanding = models.FloatField(null=True, blank=True, default=0)
    days_payables_outstanding = models.FloatField(null=True, blank=True, default=0)
    days_inventory_on_hand = models.FloatField(null=True, blank=True, default=0)
    recievables_turnover = models.FloatField(null=True, blank=True, default=0)
    payables_turnover = models.FloatField(null=True, blank=True, default=0)
    inventory_turnover = models.FloatField(null=True, blank=True, default=0)
    return_on_equity = models.FloatField(null=True, blank=True, default=0)
    capex_per_share = models.FloatField(null=True, blank=True, default=0)
    dividend_per_share = models.FloatField(null=True, blank=True, default=0)
    debt_to_market_cap = models.FloatField(null=True, blank=True, default=0)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, default=None)


    def __str__(self):
        return self.symbol

    

# Stocks to delete TRIS-WT