import pandas as pd
from pandas import DataFrame

years = [item for item in range(1990, 2021)]
locations = ['colorado']
monthly_mean_weather = pd.read_csv('data/monthly_mean_weather.csv')
crop_data = pd.read_csv('data/actual_crop_data.csv')

relational_data_list = []
index = 0
start_year = 0
end_year = 0
for location in locations:
    for year in years:
        if index == 0:
            start_year = year
            end_year = year + 10
            index = 10

        yearly_data = monthly_mean_weather[(monthly_mean_weather['year'] == year) & (monthly_mean_weather['location'] == location)]

        yearly_high_temp = yearly_data.iloc[3:10,4]
        yearly_low_temp = yearly_data.iloc[3:10,5]
        yearly_avg_temp = yearly_data.iloc[3:10,6]
        yearly_precipitation = yearly_data.iloc[3:10,7]
        yearly_dew_point = yearly_data.iloc[3:10,8]
        yearly_high_dew_point = yearly_data.iloc[3:10,9]
        yearly_low_dew_point = yearly_data.iloc[3:10,10]
        yearly_avg_dew_point = yearly_data.iloc[3:10,11]
        yearly_max_wind_speed = yearly_data.iloc[3:10,12]
        yearly_month_visibility = yearly_data.iloc[3:10,13]
        yearly_sea_pressure = yearly_data.iloc[3:10,14]

        mean_high_temp = round(yearly_high_temp.mean(), 2)
        mean_low_temp = round(yearly_low_temp.mean(), 2)
        mean_avg_temp = round(yearly_avg_temp.mean(), 2)
        mean_precipitation = round(yearly_precipitation.mean(), 2)
        mean_dew_point = round(yearly_dew_point.mean(), 2)
        mean_high_dew_point = round(yearly_high_dew_point.mean(), 2)
        mean_low_dew_point = round(yearly_low_dew_point.mean(), 2)
        mean_avg_dew_point = round(yearly_avg_dew_point.mean(), 2)
        mean_max_wind_speed = round(yearly_max_wind_speed.mean(), 2)
        mean_visibility = round(yearly_month_visibility.mean(), 2)
        mean_sea_pressure = round(yearly_sea_pressure.mean(), 2)

        filtered_crop_data = crop_data[(crop_data['year'] == (year)) & (crop_data['county_name'] == location.upper())]
        filtered_crop_data_by_year = crop_data[(crop_data['year'] > (start_year)) & (crop_data['year'] < (end_year)) & (crop_data['county_name'] == location.upper())]
        if len(filtered_crop_data.index) > 0:
            acre_planted = filtered_crop_data.iloc[0]['acre_planted']
            acre_harvested = filtered_crop_data.iloc[0]['acre_harvested']
            acres_loss = filtered_crop_data.iloc[0]['acres_loss']
            yield_lb_per_acres = filtered_crop_data.iloc[0]['yield_lb_per_acres']
            production_cwt = filtered_crop_data.iloc[0]['production_cwt']

            sample_yield = (filtered_crop_data_by_year.iloc[:]['yield_lb_per_acres'])
            performance_yield = (yield_lb_per_acres / sample_yield.max()) * 100
            
            class_yield = 'GOOD'
            if performance_yield > 90:
                class_yield = 'GOOD'
            else:
                class_yield = 'BAD'


            percentage_loss = round((100 - (acre_harvested / acre_planted ) * 100), 2)
            
            related_object = { 
            'year' : year,
            'location': location,
            'mean_high_temp' : mean_high_temp,
            'mean_low_temp' : mean_low_temp,
            'mean_avg_temp' : mean_avg_temp,
            'mean_precipitation' : mean_precipitation,
            'mean_dew_point' : mean_dew_point,
            'mean_high_dew_point' : mean_high_dew_point,
            'mean_low_dew_point' : mean_low_dew_point,
            'mean_avg_dew_point' : mean_avg_dew_point,
            'mean_max_wind_speed' : mean_max_wind_speed,
            'mean_visibility' : mean_visibility,
            'mean_sea_pressure' : mean_sea_pressure,
            'acre_planted' : acre_planted,
            'acre_harvested' : acre_harvested,
            'acres_loss' : acres_loss,
            'percentage_loss' : percentage_loss,
            'yield_lb_per_acres': yield_lb_per_acres,
            'production_cwt': production_cwt,
            'performance_yield': performance_yield,
            'class_yield': class_yield
            }
            index = index - 1
            relational_data_list.append(related_object)

relational_data = DataFrame(relational_data_list)
relational_data.to_csv('data/relational_data.csv')






