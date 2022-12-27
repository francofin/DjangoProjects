import requests
import json
import numpy as np
import pandas as pd

class GetData:
    
    def __init__(self, ticker, api, is_index= False):
        self.ticker = ticker
        self.api = api
        self.is_an_index = is_index
        if self.is_an_index:
            self.base_url = f"https://financialmodelingprep.com/api/v3/historical-price-full/%5E{self.ticker}?apikey={self.api}"
        else:
            self.base_url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{self.ticker}?serietype=line&apikey={self.api}"

        self.raw_dataframe = pd.DataFrame(json.loads(requests.get(self.base_url).content)['historical'])
        # self.raw_dataframe = json.loads(requests.get(self.base_url).content)['historical']
        

    def clean_df(self):
        dataframe = self.raw_dataframe
        dataframe.set_index(pd.to_datetime(dataframe['date'], infer_datetime_format=True), inplace=True)
        clean_df = dataframe[::-1].drop('date', axis=1)
        return clean_df
        
        
    def get_daily_index_stats(self):
        daily_data = self.clean_df()
        clean_data = daily_data[['adjClose']]
        return clean_data
        
    def get_daily_stats(self):
        daily_data = self.clean_df()
        monthly_data = daily_data.reset_index().groupby([daily_data.index.year, daily_data.index.month], as_index=False).last().set_index('date')
        daily_data['Returns'] = daily_data.pct_change()
        daily_data['1+R'] = daily_data['Returns'] +1
        daily_data['30d_returns'] = (daily_data['1+R'].rolling(window=30).apply(np.prod, raw=True) -1)*100
        daily_data['60d_returns'] = (daily_data['close'].pct_change(60))*100
        daily_data['90d_returns'] = (daily_data['close'].pct_change(90))*100
        daily_data['120d_returns'] = (daily_data['close'].pct_change(120))*100
        monthly_data['Returns'] = monthly_data.pct_change()
        monthly_data['1+R'] = monthly_data['Returns'] + 1
        monthly_data['quarterly_returns'] = (monthly_data['1+R'].rolling(window=3).apply(np.prod, raw=True) -1)*100
        monthly_data['yearly_returns'] = (monthly_data['1+R'].rolling(window=12).apply(np.prod, raw=True) -1)*100
        # daily_data['30d_vol'] = (daily_data['Returns'].rolling(window=30).std()*np.sqrt(252))*100
        # daily_data['60d_vol'] = (daily_data['Returns'].rolling(window=60).std()*np.sqrt(252))*100
        # daily_data['120d_vol'] = (daily_data['Returns'].rolling(window=120).std()*np.sqrt(252))*100
        return daily_data, monthly_data
    
    
    def get_weekly_stats(self):
        data = self.clean_df()
        weekly_data = data.reset_index().groupby([data.index.year, data.index.month, \
                                                     data.index.week], as_index=False).last().set_index('date')
        weekly_data['Returns'] = weekly_data.pct_change()
        weekly_data['13w_returns'] = (weekly_data['close'].pct_change(13))*100
        weekly_data['26w_returns'] = (weekly_data['close'].pct_change(26))*100
        weekly_data['13w_vol'] = (weekly_data['Returns'].rolling(window=13).std()*np.sqrt(48))*100
        weekly_data['26w_vol'] = (weekly_data['Returns'].rolling(window=26).std()*np.sqrt(48))*100
        
        return weekly_data
        
    
    def get_monthly_stats(self):
        data = self.clean_df()
        monthly_data = data.reset_index().groupby([data.index.year, data.index.month], as_index=False).last().set_index('date')
        monthly_data['Returns'] = monthly_data.pct_change()
        monthly_data['quarterly_returns'] = monthly_data['1+R'].rolling(window=3).apply(np.prod, raw=True) -1
        monthly_data['yearly_returns'] = monthly_data['1+R'].rolling(window=12).apply(np.prod, raw=True) -1
        monthly_data['3year_returns'] = (monthly_data['1+R'].rolling(window=36).apply(np.prod, raw=True)**(1/3)) -1
        monthly_data['5year_returns'] = (monthly_data['1+R'].rolling(window=60).apply(np.prod, raw=True)**(1/5)) -1
        monthly_data['10year_returns'] = (monthly_data['1+R'].rolling(window=120).apply(np.prod, raw=True)**(1/10)) -1
        monthly_data['1yr_vol'] = monthly_data['Returns'].rolling(window=12).std()*np.sqrt(12)
        monthly_data['2yr_vol'] = monthly_data['Returns'].rolling(window=24).std()*np.sqrt(12)
        monthly_data['3yr_vol'] = monthly_data['Returns'].rolling(window=36).std()*np.sqrt(12)
        monthly_data['10yr_vol'] = monthly_data['Returns'].rolling(window=120).std()*np.sqrt(12)
        
        
        return monthly_data


class StockSentiment:
    def __init__ (self, api):
        self.api = api
        self.upgrade_downgrade_url = f"https://financialmodelingprep.com/api/v4/upgrades-downgrades-rss-feed?page=0&apikey={self.api}"

    def get_stock_upgrades_downgrades(self):
        data = json.loads(requests.get(self.upgrade_downgrade_url).content)
        return data