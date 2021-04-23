import requests
import json
from pandas import DataFrame
import pandas as pd

data_planted_request = requests.get('http://quickstats.nass.usda.gov/api/api_GET/?key=E58B962C-15E5-3E0D-AE13-2294EBD581C4&commodity_desc=RICE&statisticcat_desc=AREA PLANTED&short_desc=RICE - ACRES PLANTED&agg_level_desc=COUNTY&format=JSON')
data_harvested_request = requests.get('http://quickstats.nass.usda.gov/api/api_GET/?key=E58B962C-15E5-3E0D-AE13-2294EBD581C4&commodity_desc=RICE&statisticcat_desc=AREA HARVESTED&short_desc=RICE - ACRES HARVESTED&agg_level_desc=COUNTY&format=JSON')
data_yield_request = requests.get('http://quickstats.nass.usda.gov/api/api_GET/?key=E58B962C-15E5-3E0D-AE13-2294EBD581C4&commodity_desc=RICE&statisticcat_desc=YIELD&short_desc=RICE - YIELD, MEASURED IN LB / ACRE&agg_level_desc=COUNTY&format=JSON')

planted_request = json.loads(data_planted_request.text)
harvested_request = json.loads(data_harvested_request.text)
yield_request = json.loads(data_yield_request.text)

planted_collection = planted_request['data']
harvested_collection = harvested_request['data']
yield_collection = yield_request['data']

harvest_df = DataFrame(harvested_collection)
yield_df = DataFrame(yield_collection)

list_actual_data = []

for item in planted_collection:
    
    harvest_data = harvest_df[(harvest_df['year'] == item['year']) & (harvest_df['country_name'] == item['country_name']) & (harvest_df['state_name'] == item['state_name']) & (harvest_df['county_name'] == item['county_name'])]
    yield_data = yield_df[(yield_df['year'] == item['year']) & (yield_df['country_name'] == item['country_name']) & (yield_df['state_name'] == item['state_name']) & (yield_df['county_name'] == item['county_name'])]
    # if not('D' in str(harvest_data.iloc[0]['Value'])):
    if len(harvest_data.index > 0) and not('D' in str(harvest_data.iloc[0]['Value'])):
        acres_harvested = float(str(harvest_data.iloc[0]['Value']).replace(',', ''))
    else:
        acres_harvested = 0

    acres_loss = (float(str(item['Value']).replace(',', '')) -  acres_harvested)
    acres_planted = float(str(item['Value']).replace(',', ''))
    # acres_harvested = float(str(harvest_data.iloc[0]['Value']).replace(',', ''))

    if len(yield_data.index) > 0:
        yield_lb_per_acres = float(str(yield_data.iloc[0]['Value']).replace(',', ''))
    else:
        yield_lb_per_acres = 0
    
    actual_object = { 
        'year': item['year'], 
        'country': item['country_name'], 
        'state': item['state_name'], 
        'county_name': item['county_name'], 
        'acre_planted': acres_planted, 
        'acre_planted_cv': item['CV (%)'], 
        'acre_harvested': acres_harvested, 
        'acres_loss': acres_loss,
        'yield_lb_per_acres': yield_lb_per_acres,
        'total_yield': acres_planted * yield_lb_per_acres
        }
    list_actual_data.append(actual_object)

actual_data_df = DataFrame(list_actual_data)
actual_data_df.to_csv('data/actual_crop_data.csv')

test = 1