import requests
import json
import numpy as np
import pandas as pd
from .SP500PeerList import SP500Peers
from .TSXPeerList import TSXPeers
from .NasdaqPeerList import NasdaqPeers
from .EuroPeerList import EuroPeers
from stockuploader.models import FundamentalAttributes
import boto3
import pickle
from django.conf import settings
from .DailyFunctions import ExtractAWSData



class PeerSpecificData:
    def __init__(self,ticker, universe):
        self.sp_universe = SP500Peers().get_available()
        self.nasdaq_universe = NasdaqPeers().get_available()
        self.tsx_universe = TSXPeers().get_available()
        self.euro_universe = EuroPeers().get_available()
        self.universe = universe
        self.ticker = ticker
        self.columns_required_for_analysis = ['netIncomePerShareTTM',  'revenuePerShareTTM', 'operatingCashFlowPerShareTTM', 'peRatioTTM', 'pocfratioTTM', 'pbRatioTTM',  \
                                'pfcfRatioTTM', 'priceToSalesRatioTTM', 'freeCashFlowPerShareTTM', 'bookValuePerShareTTM',  'freeCashFlowYieldTTM','earningsYieldTTM', \
                                'roicTTM', 'roeTTM', 'marketCapTTM', 'debtToAssetsTTM', 'debtToMarketCapTTM', 'debtToEquityTTM',\
                                'dividendYieldPercentageTTM', 'interestCoverageTTM','payoutRatioTTM', 'netDebtToEBITDATTM',\
                                'researchAndDevelopementToRevenueTTM', 'shareholdersEquityPerShareTTM', 'salesGeneralAndAdministrativeToRevenueTTM']
        self.fundamental_attirbute_name_mappings ={
                                                    'netIncomePerShareTTM':'Net Income Per Share',
                                                    'revenuePerShareTTM':'Revenue Per Share',
                                                    'operatingCashFlowPerShareTTM':'Operating Cash Flow Per Share',
                                                    'peRatioTTM':'Price to Earnings Ratio',
                                                    'pocfratioTTM':'Price to Operating Cash Flow',
                                                    'pbRatioTTM':'Price to Book',
                                                    'pfcfRatioTTM':'Price to Cash Flow',
                                                    'priceToSalesRatioTTM':'Price to Sales',
                                                    'freeCashFlowPerShareTTM':'Free Cash Flow Per Share',
                                                    'bookValuePerShareTTM':'Book Value Per Share',
                                                    'freeCashFlowYieldTTM':'Free Cash Flow Yield',
                                                    'earningsYieldTTM':'Earnings Yield',
                                                    'roicTTM':'Return On Invested Capital',
                                                    'roeTTM':'Return On Equity',
                                                    'marketCapTTM':'Market Cap',
                                                    'debtToAssetsTTM':'Debt To Assets',
                                                    'debtToMarketCapTTM':'Debt To Market Cap',
                                                    'debtToEquityTTM':'Debt To Equity',
                                                    'dividendYieldPercentageTTM':'Dividend Yield (%)',
                                                    'interestCoverageTTM':'Interest Coverage',
                                                    'payoutRatioTTM':'Dividend Payout Ratio',
                                                    'netDebtToEBITDATTM':'Net Debt To EBITDA',
                                                    'researchAndDevelopementToRevenueTTM':'Research and Development to Revenue',
                                                    'shareholdersEquityPerShareTTM':'Shareholders Equity Per Share',
                                                    'salesGeneralAndAdministrativeToRevenueTTM':'Sales and Genral Admin to Revenue'
                                                }

    def get_universe(self):
        if self.universe == 'sp500':
            return self.sp_universe
        elif self.universe == 'nasdaq':
            return self.nasdaq_universe
        elif self.universe == 'tsx':
            return self.tsx_universe
        elif self.universe == 'euro':
            return self.euro_universe


    def get_peer_chart_data(self):
        universe = self.get_universe()
        peers = universe[self.ticker]
        if len(peers) == 0:
            return "Unfortunately No Matches Found, we continue to grow our database to ensure your analysis retrieves the best results."
        else:
            if self.ticker in peers:
                pass
            else:
                peers.append(self.ticker)
            print(peers)
            all_peer_data_retrieved = FundamentalAttributes.objects.filter(symbol__in=peers)
            print(all_peer_data_retrieved)
            return
            # 
            
            # return all_peer_data_retrieved