import requests
import json
import numpy as np
import pandas as pd

class GetData:
    
    def __init__(self, ticker, api):
        self.ticker = ticker
        self.api = api
        self.base_url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{self.ticker}?serietype=line&apikey={self.api}"
        self.raw_dataframe = pd.DataFrame(json.loads(requests.get(self.base_url).content)['historical'])
        
    def clean_df(self):
        dataframe = self.raw_dataframe
        dataframe.set_index(pd.to_datetime(dataframe['date'], infer_datetime_format=True), inplace=True)
        clean_df = dataframe[::-1].drop('date', axis=1)
        return clean_df
        
        
    def get_daily_stats(self):
        daily_data = self.clean_df()
        daily_data['Returns'] = daily_data.pct_change()
        daily_data['30d_returns'] = (daily_data['close'].pct_change(30))*100
        daily_data['60d_returns'] = (daily_data['close'].pct_change(60))*100
        daily_data['90d_returns'] = (daily_data['close'].pct_change(90))*100
        daily_data['120d_returns'] = (daily_data['close'].pct_change(120))*100
        daily_data['30d_vol'] = (daily_data['Returns'].rolling(window=30).std()*np.sqrt(252))*100
        daily_data['60d_vol'] = (daily_data['Returns'].rolling(window=60).std()*np.sqrt(252))*100
        daily_data['120d_vol'] = (daily_data['Returns'].rolling(window=120).std()*np.sqrt(252))*100
        return daily_data
    
    
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
        