import pandas as pd
from pandas import DataFrame
import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

weather_data = pd.read_csv('data/weather_data_colorado.csv')
weather_data['date'] = pd.to_datetime(weather_data['date'])

test_data_pm = weather_data[weather_data['high_temp_actual'].str.contains('PM')]
test_data_am = weather_data[weather_data['high_temp_actual'].str.contains('AM')]

weather_data = weather_data.drop(test_data_pm.index)
weather_data = weather_data.drop(test_data_am.index)

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


years = [item for item in range(1990, 2021)]
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
monthly_mean_weather.to_csv('data/monthly_mean_weather.csv')