from django.urls import path, include
from . import views


urlpatterns = [
    path('all_indexes/', views.get_all_indexes, name='indexes'),
    path('homepage_indexes/', views.get_homepage_indexes, name='homepage_indexes'),
    path('market_indexes/', views.get_market_indexes, name='market_indexes'),
    path('universe/<str:universe>/', views.get_stock_universe, name='stock_universe'),
    path('stock-data/<str:ticker>/', views.get_stock, name='stock_data'),
    path('getgeocode/<str:address>/', views.get_company_location, name='get_company_location'),
    path('getdailydata/<str:ticker>/', views.get_daily_stock_data, name='get_daily_stock_data'),
    path('getpeerlist/<str:ticker>/<str:universe>/', views.get_stock_peer_list, name='get_stock_peer_list'),
]