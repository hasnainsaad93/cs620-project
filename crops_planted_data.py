import requests
import json
from pandas import DataFrame
import pandas as pd

data_planted_request = requests.get(
    'http://quickstats.nass.usda.gov/api/api_GET/?key=E58B962C-15E5-3E0D-AE13-2294EBD581C4&source_desc=SURVEY&commodity_desc=RICE&statisticcat_desc=AREA PLANTED&short_desc=RICE - ACRES PLANTED&agg_level_desc=COUNTY&format=JSON')
data_harvested_request = requests.get(
    'http://quickstats.nass.usda.gov/api/api_GET/?key=E58B962C-15E5-3E0D-AE13-2294EBD581C4&source_desc=SURVEY&commodity_desc=RICE&statisticcat_desc=AREA HARVESTED&short_desc=RICE - ACRES HARVESTED&agg_level_desc=COUNTY&format=JSON')
data_yield_request = requests.get(
    'http://quickstats.nass.usda.gov/api/api_GET/?key=E58B962C-15E5-3E0D-AE13-2294EBD581C4&source_desc=SURVEY&commodity_desc=RICE&statisticcat_desc=YIELD&short_desc=RICE - YIELD, MEASURED IN LB / ACRE&agg_level_desc=COUNTY&format=JSON')
data_production_request = requests.get(
    'http://quickstats.nass.usda.gov/api/api_GET/?key=E58B962C-15E5-3E0D-AE13-2294EBD581C4&source_desc=SURVEY&commodity_desc=RICE&statisticcat_desc=PRODUCTION&short_desc=RICE - PRODUCTION, MEASURED IN CWT&agg_level_desc=COUNTY&format=JSON')

planted_request = json.loads(data_planted_request.text)
harvested_request = json.loads(data_harvested_request.text)
yield_request = json.loads(data_yield_request.text)
production_request = json.loads(data_production_request.text)

planted_collection = planted_request['data']
harvested_collection = harvested_request['data']
yield_collection = yield_request['data']
production_collection = production_request['data']

planted_df = DataFrame(planted_collection)
harvest_df = DataFrame(harvested_collection)
yield_df = DataFrame(yield_collection)
production_df = DataFrame(production_collection)

# def converttofloat(x):
#     if not('D' in x):
#         return float(str(x).replace(',', ''))
#     else:
#         return 0 

# planted_dataset = planted_df[['year', 'state_name', 'country_name', 'county_name', 'Value']]
# planted_dataset = planted_dataset.rename(columns={'year': 'year', 'state_name': 'state', 'country_name': 'country', 'county_name': 'county', 'Value': 'acres_planted'})
# planted_dataset['acres_planted'] = planted_dataset['acres_planted'].apply(converttofloat)
# planted_dataset.to_csv('data/actual_crop_planted.csv')

# harvest_dataset = harvest_df[['year', 'state_name', 'country_name', 'county_name', 'Value']]
# harvest_dataset = harvest_dataset.rename(columns={'year': 'year', 'state_name': 'state', 'country_name': 'country', 'county_name': 'county', 'Value': 'acres_harvested'})
# harvest_dataset['acres_harvested'] = harvest_dataset['acres_harvested'].apply(converttofloat)
# harvest_dataset.to_csv('data/actual_crop_harvested.csv')

# yield_dataset = yield_df[['year', 'state_name', 'country_name', 'county_name', 'Value']]
# yield_dataset = yield_dataset.rename(columns={'year': 'year', 'state_name': 'state', 'country_name': 'country', 'county_name': 'county', 'Value': 'yield_per_acre'})
# yield_dataset['yield_per_acre'] = yield_dataset['yield_per_acre'].apply(converttofloat)
# yield_dataset.to_csv('data/actual_crop_yeild_per_acre.csv')

# production_dataset = production_df[['year', 'state_name', 'country_name', 'county_name', 'Value']]
# production_dataset = production_dataset.rename(columns={'year': 'year', 'state_name': 'state', 'country_name': 'country', 'county_name': 'county', 'Value': 'production'})
# production_dataset['production'] = production_dataset['production'].apply(converttofloat)
# production_dataset.to_csv('data/actual_crop_production.csv')

# merge_dataset = pd.concat([planted_dataset, harvest_dataset, yield_dataset, production_dataset], axis=1)
# print(merge_dataset.head())

list_actual_data = []

for item in planted_collection:

    harvest_data = harvest_df[(harvest_df['year'] == item['year']) & (harvest_df['country_name'] == item['country_name']) & (harvest_df['state_name'] == item['state_name']) & (harvest_df['county_name'] == item['county_name'])]
    yield_data = yield_df[(yield_df['year'] == item['year']) & (yield_df['country_name'] == item['country_name']) & (yield_df['state_name'] == item['state_name']) & (yield_df['county_name'] == item['county_name'])]
    production_data = production_df[(production_df['year'] == item['year']) & (production_df['country_name'] == item['country_name']) & (production_df['state_name'] == item['state_name']) & (production_df['county_name'] == item['county_name'])]
    # if not('D' in str(harvest_data.iloc[0]['Value'])):
    if len(harvest_data.index > 0) and not('D' in str(harvest_data.iloc[0]['Value'])):
        acres_harvested = float(str(harvest_data.iloc[0]['Value']).replace(',', ''))
    else:
        acres_harvested = 0

    acres_loss = (float(str(item['Value']).replace(',', '')) -  acres_harvested)
    acres_planted = float(str(item['Value']).replace(',', ''))
    
    if len(production_data.index) > 0:
        production_cwt = float(str(production_data.iloc[0]['Value']).replace(',', ''))
    else:
        production_cwt = 0
        
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
        'total_yield': acres_planted * yield_lb_per_acres,
        'production_cwt': production_cwt
        }
    list_actual_data.append(actual_object)

actual_data_df = DataFrame(list_actual_data)
actual_data_df.to_csv('data/actual_crop_data.csv')

test = 1
