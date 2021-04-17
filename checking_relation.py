import pandas as pd
from pandas import DataFrame
import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

weather_data = pd.read_csv('weather_data.csv')
weather_data['date'] = pd.to_datetime(weather_data['date'])

test_data = weather_data[weather_data['high_temp_actual'] == '1:52 AM']

weather_data = weather_data.drop(test_data.index)

weather_data['high_temp_actual'] = pd.to_numeric(weather_data['high_temp_actual'])
weather_data['low_temp_actual'] = pd.to_numeric(weather_data['low_temp_actual'])
weather_data['avg_temp_actual'] = pd.to_numeric(weather_data['avg_temp_actual'])
weather_data['precipitation_actual'] = pd.to_numeric(weather_data['precipitation_actual'])
weather_data['dew_point_actual'] = pd.to_numeric(weather_data['dew_point_actual'])
weather_data['high_dew_point_actual'] = pd.to_numeric(weather_data['high_dew_point_actual'])
weather_data['low_dew_point_actual'] = pd.to_numeric(weather_data['low_dew_point_actual'])
weather_data['avg_dew_point_actual'] = pd.to_numeric(weather_data['avg_dew_point_actual'])
weather_data['max_wind_speed_actual'] = pd.to_numeric(weather_data['max_wind_speed_actual'])
weather_data['visibility_actual'] = pd.to_numeric(weather_data['visibility_actual'])
weather_data['sea_pressure_actual'] = pd.to_numeric(weather_data['sea_pressure_actual'])


years = [item for item in range(2010, 2021)]
list_month_temp = []

for year in years:
    yearly_grouped_data = weather_data[weather_data['date'].dt.year == year] 
    
    for m in range(1, 12):
        month_grouped_data = yearly_grouped_data[yearly_grouped_data['date'].dt.month == m]

        month_high_temp = month_grouped_data['high_temp_actual']
        month_low_temp = month_grouped_data['low_temp_actual']
        month_avg_temp = month_grouped_data['avg_temp_actual']
        month_precipitation = month_grouped_data['precipitation_actual']
        month_dew_point = month_grouped_data['dew_point_actual']
        month_high_dew_point = month_grouped_data['high_dew_point_actual']
        month_low_dew_point = month_grouped_data['low_dew_point_actual']
        month_avg_dew_point = month_grouped_data['avg_dew_point_actual']
        month_max_wind_speed = month_grouped_data['max_wind_speed_actual']
        month_visibility = month_grouped_data['visibility_actual']
        month_sea_pressure = month_grouped_data['sea_pressure_actual']

        mean_high_temp = month_high_temp.mean()
        mean_low_temp = month_low_temp.mean()
        mean_avg_temp = month_avg_temp.mean()
        mean_precipitation = month_precipitation.mean()
        mean_dew_point = month_dew_point.mean()
        mean_high_dew_point = month_high_dew_point.mean()
        mean_low_dew_point = month_low_dew_point.mean()
        mean_avg_dew_point = month_avg_dew_point.mean()
        mean_max_wind_speed = month_max_wind_speed.mean()
        mean_visibility = month_visibility.mean()
        mean_sea_pressure = month_sea_pressure.mean()

        month_temp_object = { 
            'month' : str(m),
            'year' : str(year), 
            'mean_high_temp' : round(mean_high_temp, 2),
            'mean_low_temp' : round(mean_low_temp, 2),
            'mean_avg_temp' : round(mean_avg_temp, 2),
            'mean_precipitation' : round(mean_precipitation, 2),
            'mean_dew_point' : round(mean_dew_point, 2),
            'mean_high_dew_point' : round(mean_high_dew_point, 2),
            'mean_low_dew_point' : round(mean_low_dew_point, 2),
            'mean_avg_dew_point' : round(mean_avg_dew_point, 2),
            'mean_max_wind_speed' : round(mean_max_wind_speed, 2),
            'mean_month_visibility' : round(mean_visibility, 2),
            'mean_sea_pressure' : round(mean_sea_pressure, 2)
        }

        list_month_temp.append(month_temp_object)

monthly_mean_weather = DataFrame(list_month_temp)
monthly_mean_weather.to_csv('monthly_mean_weather.csv')
crop_data = pd.read_csv('actual_crop_data.csv')

relational_data_list = []
index = 0
for year in years:
    yearly_data = monthly_mean_weather[monthly_mean_weather['year'] == str(year)]

    yearly_high_temp = yearly_data.iloc[:,2]
    yearly_low_temp = yearly_data.iloc[:,3]
    yearly_avg_temp = yearly_data.iloc[:,4]
    yearly_precipitation = yearly_data.iloc[:,5]
    yearly_dew_point = yearly_data.iloc[:,6]
    yearly_high_dew_point = yearly_data.iloc[:,7]
    yearly_low_dew_point = yearly_data.iloc[:,8]
    yearly_avg_dew_point = yearly_data.iloc[:,9]
    yearly_max_wind_speed = yearly_data.iloc[:,10]
    yearly_month_visibility = yearly_data.iloc[:,11]
    yearly_sea_pressure = yearly_data.iloc[:,12]

    std_high_temp = round(yearly_high_temp.std(), 2)
    std_low_temp = round(yearly_low_temp.std(), 2)
    std_avg_temp = round(yearly_avg_temp.std(), 2)
    std_precipitation = round(yearly_precipitation.std(), 2)
    std_dew_point = round(yearly_dew_point.std(), 2)
    std_high_dew_point = round(yearly_high_dew_point.std(), 2)
    std_low_dew_point = round(yearly_low_dew_point.std(), 2)
    std_avg_dew_point = round(yearly_avg_dew_point.std(), 2)
    std_max_wind_speed = round(yearly_max_wind_speed.std(), 2)
    std_visibility = round(yearly_month_visibility.std(), 2)
    std_sea_pressure = round(yearly_sea_pressure.std(), 2)

    filtered_crop_data = crop_data[(crop_data['year'] == year) & (crop_data['county_name'] == 'COLORADO')]

    if len(filtered_crop_data.index) > 0:
        acre_planted = filtered_crop_data.iloc[0]['acre_planted']
        acre_harvested = filtered_crop_data.iloc[0]['acre_harvested']
        acres_loss = filtered_crop_data.iloc[0]['acres_loss']

        percentage_loss = round((100 - (acre_harvested / acre_planted ) * 100), 2)
        
        related_object = { 
        'ind': index,
        'std_high_temp' : std_high_temp,
        'std_low_temp' : std_low_temp,
        'std_avg_temp' : std_avg_temp,
        'std_precipitation' : std_precipitation,
        'std_dew_point' : std_dew_point,
        'std_high_dew_point' : std_high_dew_point,
        'std_low_dew_point' : std_low_dew_point,
        'std_avg_dew_point' : std_avg_dew_point,
        'std_max_wind_speed' : std_max_wind_speed,
        'std_visibility' : std_visibility,
        'std_sea_pressure' : std_sea_pressure,
        'acre_planted' : acre_planted,
        'acre_harvested' : acre_harvested,
        'acres_loss' : acres_loss,
        'percentage_loss' : percentage_loss
        }
        index = index + 1
        relational_data_list.append(related_object)

relational_data = DataFrame(relational_data_list)
relational_data = relational_data.sort_values(by=['std_high_temp'])
# relational_data['std_high_temp'] = relational_data.index
fig, axs = plt.subplots(ncols=3, nrows=3)

sns.scatterplot(data=relational_data, x='percentage_loss', y='std_high_temp', ax=axs[0][0])
sns.scatterplot(data=relational_data, x='percentage_loss', y='std_dew_point', ax=axs[0][1])
sns.scatterplot(data=relational_data, x='percentage_loss', y='std_precipitation', ax=axs[0][2])
sns.scatterplot(data=relational_data, x='percentage_loss', y='std_max_wind_speed', ax=axs[1][0])
sns.scatterplot(data=relational_data, x='percentage_loss', y='std_sea_pressure', ax=axs[1][1])
sns.scatterplot(data=relational_data, x='percentage_loss', y='std_visibility', ax=axs[1][2])
sns.scatterplot(data=relational_data, x='percentage_loss', y='std_low_temp', ax=axs[2][0])
sns.scatterplot(data=relational_data, x='percentage_loss', y='std_avg_temp', ax=axs[2][1])
sns.scatterplot(data=relational_data, x='percentage_loss', y='std_high_dew_point', ax=axs[2][2])

plt.show()




