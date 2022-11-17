from __future__ import absolute_import, unicode_literals
import random
from celery import shared_task
from .getNews import GetNewsArticles

news_articles_init = GetNewsArticles()



@shared_task(name='get_economic_articles')
def economic_articles():
    articles = news_articles_init.get_econ_articles()
    return articles

@shared_task(name='get_market_articles')
def market_articles():
    articles = news_articles_init.get_market_articles()
    return articles

@shared_task(name='get_tech_articles')
def tech_articles():
    articles = news_articles_init.get_tech_articles()
    return articles


@shared_task(name='get_inflation_articles')
def inflation_articles():
    articles = news_articles_init.get_inflation_articles()
    return articles

@shared_task(name='get_politics_articles')
def political_articles():
    articles = news_articles_init.get_politics_articles()
    return articles

@shared_task(name='get_energy_articles')
def energy_articles():
    articles = news_articles_init.get_energy_articles()
    return articles

@shared_task(name='get_us_news_articles')
def us_articles():
    articles = news_articles_init.get_us_news_articles()
    return articles


@shared_task(name='get_china_news_articles')
def china_articles():
    articles = news_articles_init.get_china_news_articles()
    return articles


@shared_task(name='get_russia_news_articles')
def russia_articles():
    articles = news_articles_init.get_russia_news_articles()
    return articles


@shared_task(name='get_mid_east_articles')
def mid_east_articles():
    articles = news_articles_init.get_mid_east_articles()
    return articles


@shared_task(name='get_german_news_articles')
def german_articles():
    articles = news_articles_init.get_german_news_articles()
    return articles


@shared_task(name='get_japan_news_articles')
def japan_articles():
    articles = news_articles_init.get_japan_news_articles()
    return articles

@shared_task(name='get_africa_news_articles')
def africa_articles():
    articles = news_articles_init.get_africa_news_articles()
    return articles

@shared_task(name='get_south_am_articles')
def southam_articles():
    articles = news_articles_init.get_south_am_articles()
    return articles

@shared_task(name='get_oil_articles')
def oil_articles():
    articles = news_articles_init.get_oil_articles()
    return articles

@shared_task(name='get_war_articles')
def war_articles():
    articles = news_articles_init.get_war_articles()
    return articles

@shared_task(name='get_mat_articles')
def mat_articles():
    articles = news_articles_init.get_materials_articles()
    return articles

@shared_task(name='get_ind_articles')
def ind_articles():
    articles = news_articles_init.get_industrials_articles()
    return articles


@shared_task(name='get_util_articles')
def util_articles():
    articles = news_articles_init.get_util_articles()
    return articles

@shared_task(name='get_pharma_articles')
def pharma_articles():
    articles = news_articles_init.get_pharma_articles()
    return articles

@shared_task(name='get_cons_articles')
def cons_articles():
    articles = news_articles_init.get_cons_articles()
    return articles


@shared_task(name='get_fin_articles')
def fin_articles():
    articles = news_articles_init.get_fin_articles()
    return articles


@shared_task(name="sum_two_numbers")
def add(x, y):
    return x + y


@shared_task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total


@shared_task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)