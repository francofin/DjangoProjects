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

        return data

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

