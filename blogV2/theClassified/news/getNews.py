from django_cron import CronJobBase, Schedule
import requests
import json
from django.conf import settings


class GetNewsArticles:

    def __init__(self):
        self.search_terms=['Economy', 'Stock Market', 'Technology', 'Inflation', 'Politics', \
                        'Energy', 'War', 'Oil', 'Middle East', 'South America', 'US', 'Japan', 'China', 'Russia', 'Germany','Africa', \
                        'Basic Materials', 'Industrials', 'Utilities Sector', 'Pharmaceuticals', 'Consumer trends', 'Financials', \
                        'Real Estate', 'Communications Industry']
  

    def get_news(self, search_term):
        subscription_key = settings.AZURE_API_KEY
        search_url = "https://api.cognitive.microsoft.com/bing/v7.0/news/search"
        headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
        params  = {"q": search_term, "count":'50', "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(search_url, headers=headers, params=params)
        search_results = json.loads(response.content)
        items = search_results['value']

        return items


    def get_econ_articles(self):
        search_terms = self.search_terms
        economy = self.get_news(search_terms[0])
        return economy

    def get_market_articles(self):
        search_terms = self.search_terms
        stock_market = self.get_news(search_terms[1])
        return stock_market


    def get_tech_articles(self):
        search_terms = self.search_terms
        tech = self.get_news(search_terms[2])
        return tech


    def get_inflation_articles(self):
        search_terms = self.search_terms
        inflation = self.get_news(search_terms[3])
        return inflation

    def get_politics_articles(self):
        search_terms = self.search_terms
        politics = self.get_news(search_terms[4])
        return politics

    def get_energy_articles(self):
        search_terms = self.search_terms
        energy = self.get_news(search_terms[5])
        return energy


    def get_us_news_articles(self):
        search_terms = self.search_terms
        us_news = self.get_news(search_terms[10])
        return us_news


    def get_china_news_articles(self):
        search_terms = self.search_terms
        china_news = self.get_news(search_terms[12])
        return china_news

    def get_russia_news_articles(self):
        search_terms = self.search_terms
        russia_news = self.get_news(search_terms[13])
        return russia_news

    def get_mid_east_articles(self):
        search_terms = self.search_terms
        mid_east = self.get_news(search_terms[8])
        return mid_east

    def get_german_news_articles(self):
        search_terms = self.search_terms
        german_news = self.get_news(search_terms[14])
        return german_news

    def get_japan_news_articles(self):
        search_terms = self.search_terms
        japan_news = self.get_news(search_terms[11])
        return japan_news


    def get_africa_news_articles(self):
        search_terms = self.search_terms
        africa_news = self.get_news(search_terms[15])
        return africa_news

    def get_oil_articles(self):
        search_terms = self.search_terms
        oil = self.get_news(search_terms[7])
        return oil

    def get_war_articles(self):
        search_terms = self.search_terms
        war = self.get_news(search_terms[6])
        return war


    def get_south_am_articles(self):
        search_terms = self.search_terms
        south_am = self.get_news(search_terms[9])
        return south_am

    def get_materials_articles(self):
        search_terms = self.search_terms
        mat = self.get_news(search_terms[16])
        return mat

    def get_industrials_articles(self):
        search_terms = self.search_terms
        ind = self.get_news(search_terms[17])
        return ind

    def get_util_articles(self):
        search_terms = self.search_terms
        util = self.get_news(search_terms[18])
        return util

    def get_pharma_articles(self):
        search_terms = self.search_terms
        pharma = self.get_news(search_terms[19])
        return pharma

    def get_cons_articles(self):
        search_terms = self.search_terms
        cons = self.get_news(search_terms[20])
        return cons

    def get_fin_articles(self):
        search_terms = self.search_terms
        fin = self.get_news(search_terms[21])
        return fin

    def get_re_articles(self):
        search_terms = self.search_terms
        re = self.get_news(search_terms[22])
        return re

    def get_comm_articles(self):
        search_terms = self.search_terms
        comm = self.get_news(search_terms[23])
        return comm
    