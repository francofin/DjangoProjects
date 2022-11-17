from django.urls import path, include
from . import views


urlpatterns = [
    path('newsarticles/economy', views.get_econ_news, name='econ_news'),
    path('newsarticles/markets', views.get_market_news, name='market_news'),
    # path('news-articles/econ', views.get_econ_news, name='econ_news'),
    # path('news-articles/econ', views.get_econ_news, name='econ_news'),
    # path('news-articles/econ', views.get_econ_news, name='econ_news'),
    # path('news-articles/econ', views.get_econ_news, name='econ_news'),
    # path('news-articles/econ', views.get_econ_news, name='econ_news'),
    # path('news-articles/econ', views.get_econ_news, name='econ_news'),
    # path('news-articles/econ', views.get_econ_news, name='econ_news'),
    
]