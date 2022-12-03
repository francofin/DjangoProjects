from django.urls import path, include
from . import views


urlpatterns = [
    path('newsarticles/economy', views.get_econ_news, name='econ_news'),
    path('newsarticles/markets', views.get_market_news, name='market_news'),
    path('newsarticles/politics', views.get_politics_news, name='pol_news'),
    path('newsarticles/war', views.get_war_news, name='war_news'),
    path('newsarticles/inflation', views.get_inflation_news, name='inflation_news'),
    path('newsarticles/etaunido', views.get_us_news, name='us_news'),
    path('newsarticles/china', views.get_china_news, name='china_news'),
    path('newsarticles/russia', views.get_russia_news, name='russia_news'),
    path('newsarticles/mediooeste', views.get_mid_east_news, name='mideast_news'),
    path('newsarticles/aleman', views.get_germany_news, name='german_news'),
    path('newsarticles/japon', views.get_japan_news, name='japan_news'),
    path('newsarticles/suram', views.get_southam_news, name='southam_news'),
    path('newsarticles/africa', views.get_africa_news, name='africa_news'),
    path('newsarticles/tech', views.get_tech_news, name='tech_news'),
    path('newsarticles/energy', views.get_econ_news, name='econ_news'),
    path('newsarticles/oil', views.get_oil_news, name='oil_news'),
    path('newsarticles/finance', views.get_finance_news, name='fin_news'),
    path('newsarticles/cons', views.get_cons_news, name='cons_news'),
    path('newsarticles/materials', views.get_mat_news, name='mat_news'),
    path('newsarticles/health', views.get_pharma_news, name='health_news'),
    path('newsarticles/indus', views.get_indus_news, name='indus_news'),
    path('newsarticles/util', views.get_util_news, name='util_news'),
    path('newsarticles/realestate', views.get_re_news, name='re_news'),
    path('newsarticles/comm', views.get_comm_news, name='comm_news'),
    path('newsarticles/fmp', views.get_fmp_news, name='fmp_news'),
    # path('news-articles/econ', views.get_econ_news, name='econ_news'),
    # path('news-articles/econ', views.get_econ_news, name='econ_news'),
]