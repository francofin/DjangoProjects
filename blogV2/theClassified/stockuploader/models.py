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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.symbol

class ProfileStock(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


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
    name = models.CharField(max_length=300)
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
    date_first_added=models.DateTimeField(auto_now_add=False, null=True)
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

