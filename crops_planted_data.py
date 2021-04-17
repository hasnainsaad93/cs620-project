import requests
import json
from pandas import DataFrame

data_planted_request = requests.get('http://quickstats.nass.usda.gov/api/api_GET/?key=E58B962C-15E5-3E0D-AE13-2294EBD581C4&commodity_desc=RICE&statisticcat_desc=AREA PLANTED&short_desc=RICE - ACRES PLANTED&agg_level_desc=COUNTY&state_name=TEXAS&format=JSON')
data_harvested_request = requests.get('http://quickstats.nass.usda.gov/api/api_GET/?key=E58B962C-15E5-3E0D-AE13-2294EBD581C4&commodity_desc=RICE&statisticcat_desc=AREA HARVESTED&short_desc=RICE - ACRES HARVESTED&agg_level_desc=COUNTY&state_name=TEXAS&format=JSON')

planted_request = json.loads(data_planted_request.text)
harvested_request = json.loads(data_harvested_request.text)

planted_collection = planted_request['data']
harvested_collection = harvested_request['data']
harvest_df = DataFrame(harvested_collection)

list_actual_data = []

for item in planted_collection:
    
    harvest_data = harvest_df[(harvest_df['year'] == item['year']) & (harvest_df['country_name'] == item['country_name']) & (harvest_df['state_name'] == item['state_name']) & (harvest_df['county_name'] == item['county_name'])]
    if not('D' in str(harvest_data.iloc[0]['Value'])):
        acres_loss = (float(str(item['Value']).replace(',', '')) -  float(str(harvest_data.iloc[0]['Value']).replace(',', '')))
        acres_planted = float(str(item['Value']).replace(',', ''))
        acres_harvested = float(str(harvest_data.iloc[0]['Value']).replace(',', ''))
        actual_object = { 'year': item['year'], 'country': item['country_name'], 'state': item['state_name'], 'county_name': item['county_name'], 'acre_planted': acres_planted, 'acre_planted_cv': item['CV (%)'], 'acre_harvested': acres_harvested, 'acres_loss': acres_loss }
        list_actual_data.append(actual_object)

actual_data_df = DataFrame(list_actual_data)
actual_data_df.to_csv('actual_crop_data.csv')

test = 1