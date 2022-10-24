import boto3
import pickle
from django.conf import settings
import os

def load_obj(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
def save_obj(obj, path ):
    with open(path, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

fintank_data_client = boto3.client(
    's3',
    aws_access_key_id = str(settings.AWS_ACCESS_KEY_ID),
    aws_secret_access_key = str(settings.AWS_SECRET_ACCESS_KEY),
    region_name = 'us-east-1'
)

# s3 = boto3.resource("s3",
#     aws_access_key_id = str(settings.AWS_ACCESS_KEY_ID),
#     aws_secret_access_key = str(settings.AWS_SECRET_ACCESS_KEY),
#     region_name = 'us-east-1')

class AWSStockData:

    def __init__(self):
        self.fintank_data_client = fintank_data_client
        # self.s3 = s3
        self.sector_return_keys = ['15_day_return.pkl', '30_day_return.pkl', '60_day_return.pkl', '90_day_return.pkl']
        self.sector_vol_keys = ['15_day_vol.pkl', '30_day_vol.pkl', '60_day_vol.pkl', '90_day_vol.pkl']


    def get_sector_return_time_series(self):
        
        obj_15_return = self.fintank_data_client.get_object(Bucket = 'fintank-stock-data',Key = self.sector_return_keys[0])
        obj_30_return = self.fintank_data_client.get_object(Bucket = 'fintank-stock-data',Key = self.sector_return_keys[1])
        obj_60_return = self.fintank_data_client.get_object(Bucket = 'fintank-stock-data',Key = self.sector_return_keys[2])
        obj_90_return = self.fintank_data_client.get_object(Bucket = 'fintank-stock-data',Key = self.sector_return_keys[3])


        pickle_data_15 = pickle.loads(obj_15_return['Body'].read())
        pickle_data_30 = pickle.loads(obj_30_return['Body'].read())
        pickle_data_60 = pickle.loads(obj_60_return['Body'].read())
        pickle_data_90 = pickle.loads(obj_90_return['Body'].read())

        

        

        return pickle_data_15, pickle_data_30, pickle_data_60, pickle_data_90

    def get_sector_vol_time_series(self):
        
        obj_15_vol = self.fintank_data_client.get_object(Bucket = 'fintank-stock-data',Key = self.sector_vol_keys[0])
        obj_30_vol = self.fintank_data_client.get_object(Bucket = 'fintank-stock-data',Key = self.sector_vol_keys[1])
        obj_60_vol = self.fintank_data_client.get_object(Bucket = 'fintank-stock-data',Key = self.sector_vol_keys[2])
        obj_90_vol = self.fintank_data_client.get_object(Bucket = 'fintank-stock-data',Key = self.sector_vol_keys[3])

        pickle_data_15 = pickle.loads(obj_15_vol['Body'].read())
        pickle_data_30 = pickle.loads(obj_30_vol['Body'].read())
        pickle_data_60 = pickle.loads(obj_60_vol['Body'].read())
        pickle_data_90 = pickle.loads(obj_90_vol['Body'].read())

        return pickle_data_15, pickle_data_30, pickle_data_60, pickle_data_90



aws_data = AWSStockData()

sector_return_15, sector_return_30, sector_return_60, sector_return_90 = aws_data.get_sector_return_time_series()
sector_vol_15, sector_vol_30, sector_vol_60, sector_vol_90 = aws_data.get_sector_vol_time_series()


class ExtractAWSData:

    def __init__(self):
        self.sector_return_15 = sector_return_15
        self.sector_return_30 = sector_return_30
        self.sector_return_60 = sector_return_60
        self.sector_return_90 = sector_return_90
        self.sector_vol_15 = sector_vol_15
        self.sector_vol_30 = sector_vol_30
        self.sector_vol_60 = sector_vol_60
        self.sector_vol_90 = sector_vol_90

    def get_data_package(self, data_pack):
        data_dataes = [str(x)[0:10] for x in list(data_pack.index)]
        utilities = [str(x)[0:10] for x in list(data_pack['Utilities'])]
        Basic_Materials = [str(x)[0:10] for x in list(data_pack['Basic_Materials'])]
        Communications = [str(x)[0:10] for x in list(data_pack['Communications'])]
        Consumer_Cyclical = [str(x)[0:10] for x in list(data_pack['Consumer_Cyclical'])]
        Consumer_Defensive = [str(x)[0:10] for x in list(data_pack['Consumer_Defensive'])]
        Energy = [str(x)[0:10] for x in list(data_pack['Energy'])]
        Financials = [str(x)[0:10] for x in list(data_pack['Financials'])]
        Financial_Services = [str(x)[0:10] for x in list(data_pack['Financial_Services'])]
        Health_Care = [str(x)[0:10] for x in list(data_pack['Health_Care'])]
        Industrials = [str(x)[0:10] for x in list(data_pack['Industrials'])]
        Real_Estate = [str(x)[0:10] for x in list(data_pack['Real_Estate'])]
        Technology = [str(x)[0:10] for x in list(data_pack['Technology'])]


        all_data = {
            "dates":data_dataes,
            "utilities":utilities,
            "basicM":Basic_Materials,
            "communications":Communications,
            "cons_cyc":Consumer_Cyclical,
            "cons_def":Consumer_Defensive,
            "energy":Energy,
            "financials":Financials,
            "fin_services":Financial_Services,
            "health_care":Health_Care,
            "industrials":Industrials,
            "real_estate":Real_Estate,
            "tech":Technology
        }

        return all_data




