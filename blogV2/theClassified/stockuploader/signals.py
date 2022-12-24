from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Stock, FundamentalAttributes



@receiver(pre_save, sender=FundamentalAttributes)
def add_stock_key(sender, instance, *args, **kwargs):
    if instance and not instance.stock:
        print(instance)
        stock = Stock.objects.filter(symbol=instance.symbol)[:1].get()
        instance.stock = stock
        