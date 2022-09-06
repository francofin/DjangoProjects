from django.contrib import admin
from .models import Store, Product
# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'owner')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'date_added')
    date_hierarchy = 'date_added'
    search_fields = ('name', 'owner')