import requests
import json
import numpy as np
import pandas as pd
from .SP500PeerList import SP500Peers
from .TSXPeerList import TSXPeers
from .NasdaqPeerList import NasdaqPeers
from .EuroPeerList import EuroPeers
import boto3
import pickle
from django.conf import settings
from .DailyFunctions import ExtractAWSData

class StockScreener:
    def __init__(self,market_cap_max=None, market_cap_min=0,dividend_min=0,
                beta_max=None, beta_min=None,sector=None, sub_industry=None,
                country=None, price_max=None, price_min=None,volume_max=None, volume_min=None, limit=10000):
        
        self.api= settings.FMP_API
        self.market_cap_max = market_cap_max
        self.market_cap_min = market_cap_min
        self.volume_max = volume_max
        self.volume_min = volume_min
        self.dividend_min = dividend_min
        self.beta_max = beta_max
        self.beta_min = beta_min
        self.sector = sector
        self.sub_industry = sub_industry
        self.country = country
        self.limit = limit
        self.price_max = price_max
        self.price_min = price_min

        self.collection = [self.market_cap_max, self.volume_max, self.volume_min,
                           self.dividend_min, self.beta_max,self.beta_min, self.sector,self.sub_industry, 
                           self.country, self.limit, self.price_max , self.price_min]

        self.market_cap_max_url = f"&marketCapLowerThan={self.market_cap_max}"
        # self.market_cap_min_url = f"marketCapMoreThan={self.market_cap_min}"

        self.volume_max_url = f"&volumeLowerThan={self.volume_max}"
        self.volume_min_url = f"&volumeMoreThan={self.volume_min}"

        self.dividend_min_url = f"&dividendMoreThan={self.dividend_min}"

        self.beta_max_url = f"&betaLowerThan={self.beta_max}"
        self.beta_min_url = f"&betaMoreThan={self.beta_min}"

        self.price_max_url = f"&priceLowerThan={self.price_max}"
        self.price_min_url = f"p&riceMoreThan={self.price_min}"

        self.sub_industry_url = f"&Industry={self.sub_industry}"
        self.country_url = f"&Country={self.country}"

        self.sector_url = f"&sector={self.sector}"
        self.screener_url = f"https://financialmodelingprep.com/api/v3/stock-screener?marketCapMoreThan={str(self.market_cap_min)}&isEtf=false"
        self.api_suffix = f"&apikey={self.api}"

    def get_screen_query(self):
        base_url = self.screener_url

        if self.market_cap_max is None:
            pass
        else:
            base_url += self.market_cap_max_url

        if self.volume_max is None:
            pass
        else:
            base_url += self.volume_max_url

        if self.volume_min is None:
            pass
        else:
            base_url += self.volume_min_url


        if self.beta_max is None:
            pass
        else:
            base_url += self.beta_max_url

       
        if self.beta_min is None:
            pass
        else:
            base_url += self.beta_min_url


        if self.dividend_min is None:
            pass
        else:
            base_url += self.dividend_min_url

        
        if self.price_max is None:
            pass
        else:
            base_url += self.price_max_url
        

        if self.price_min is None:
            pass
        else:
            base_url += self.price_min_url
        
        if self.sub_industry is None:
            pass
        else:
            base_url += self.sub_industry_url
        
        if self.country is None:
            pass
        else:
            base_url += self.country_url

        if self.sector is None:
            pass
        else:
            base_url += self.sector_url



        final_query_url = base_url+self.api_suffix
        return final_query_url

    
    def get_screen_results(self):

        query = self.get_screen_query()
        data = json.loads(requests.get(query).content)

        return data
        


class UniverseData:

    def __init__(self, api, universe='', ticker=''):
        self.ticker = ticker
        self.sp_universe = SP500Peers().get_available()
        self.nasdaq_universe = NasdaqPeers().get_available()
        self.tsx_universe = TSXPeers().get_available()
        self.euro_universe = EuroPeers().get_available()
        self.universe = universe
        self.data_package = ExtractAWSData()
        self.api = api
        self.sector_perf_url = f"https://financialmodelingprep.com/api/v3/sector-performance?apikey={self.api}"
        self.most_gainer_url = f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={self.api}"
        self.most_loser_url = f"https://financialmodelingprep.com/api/v3/stock_market/losers?apikey={self.api}"
        self.most_active_url = f"https://financialmodelingprep.com/api/v3/stock_market/actives?apikey={self.api}"
        


    def get_universe(self):
        if self.universe == 'sp500':
            return self.sp_universe
        elif self.universe == 'nasdaq':
            return self.nasdaq_universe
        elif self.universe == 'tsx':
            return self.tsx_universe
        elif self.universe == 'euro':
            return self.euro_universe

    def get_universe_fundamentals(self):
        universe  = self.get_universe()
        available_peers = universe[self.ticker]

    def get_sector_returns(self):
        data = json.loads(requests.get(self.sector_perf_url).content)
        sector_perf_positives = [float(data[x]['changesPercentage'].split("%")[0]) for x in range(len(data))]
        greater_than_zero = len([i for i in sector_perf_positives if i > 0])
        message = ''
        if greater_than_zero == 13:
            message = "All Sectors Outperformed"
        elif greater_than_zero >= 6:
            message = "General Positive Day in Markets"
        elif greater_than_zero <= 1:
            message = "Red Across the Board"
        elif greater_than_zero <=6:
            message = "Red Mostly Across The Board"

        return data, message

    def get_sector_return_timeseries(self, frequency=''):

        data = []

        if frequency == 'thirty':
            data = self.data_package.get_data_package(self.data_package.sector_return_30)
        elif frequency == 'sixty':
            data = self.data_package.get_data_package(self.data_package.sector_return_60)
        elif frequency == 'ninety':
            data = self.data_package.get_data_package(self.data_package.sector_return_90)
        else:
            data = self.data_package.get_data_package(self.data_package.sector_return_15)

        
        return data
        
    
    def get_sector_vol_timeseries(self, frequency=''):

        data = []

        if frequency == 'thirty':
            data = self.data_package.get_data_package(self.data_package.sector_vol_30)
        elif frequency == 'sixty':
            data = self.data_package.get_data_package(self.data_package.sector_vol_60)
        elif frequency == 'ninety':
            data = self.data_package.get_data_package(self.data_package.sector_vol_90)
        else:
            data = self.data_package.get_data_package(self.data_package.sector_vol_15)

        
        return data


    def get_most_gainer_loser_active(self):

        most_gainer = json.loads(requests.get(self.most_gainer_url).content)
        most_loser = json.loads(requests.get(self.most_loser_url).content)
        most_active = json.loads(requests.get(self.most_active_url).content)


        return most_gainer, most_loser, most_active

