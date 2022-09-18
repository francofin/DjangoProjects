from django.db import models
from django.conf import settings


# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=300)
    name = models.CharField(max_length=300, default="")
    exchange = models.CharField(max_length=300, default="", null=True)
    exchange_short = models.CharField(max_length=300, default="", null=True)
    stock_type = models.CharField(max_length=300,default="", null=True)
    is_featured = models.BooleanField(default=True, null=True)

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

    def __str__(self):
        return self.symbol

class TSX(models.Model):
    symbol = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    currency = models.CharField(max_length=300)
    exchange = models.CharField(max_length=300, default=" ")

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

    def __str__(self):
        return self.symbol

class Crypto(models.Model):
    symbol = models.CharField(max_length = 200)
    name = models.CharField(max_length=300)
    currency = models.CharField(max_length=200, null=True)
    exchange = models.CharField(max_length=300, default="", null=True)
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

    def __str__(self):
        return self.symbol