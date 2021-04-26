import pandas as pd
from pandas import DataFrame
import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

weather_data = pd.read_csv('data/weather_data_by_location.csv')
weather_data['date'] = pd.to_datetime(weather_data['date'])
years = [item for item in range(1990, 2021)]
list_month_temp = []
list_locations = ['colorado', 'arkansas']
for location in list_locations:
    location_weather_data = weather_data[weather_data['location'] == location]
    for year in years:
        yearly_grouped_data = location_weather_data[location_weather_data['date'].dt.year == year] 
        
        for m in range(1, 13):
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
            
            max_high_temp = month_high_temp.max()
            max_low_temp = month_low_temp.max()
            max_avg_temp = month_avg_temp.max()
            max_precipitation = month_precipitation.max()
            max_dew_point = month_dew_point.max()
            max_high_dew_point = month_high_dew_point.max()
            max_low_dew_point = month_low_dew_point.max()
            max_avg_dew_point = month_avg_dew_point.max()
            max_max_wind_speed = month_max_wind_speed.max()
            max_visibility = month_visibility.max()
            max_sea_pressure = month_sea_pressure.max()

            min_high_temp = month_high_temp.min()
            min_low_temp = month_low_temp.min()
            min_avg_temp = month_avg_temp.min()
            min_precipitation = month_precipitation.min()
            min_dew_point = month_dew_point.min()
            min_high_dew_point = month_high_dew_point.min()
            min_low_dew_point = month_low_dew_point.min()
            min_avg_dew_point = month_avg_dew_point.min()
            min_max_wind_speed = month_max_wind_speed.min()
            min_visibility = month_visibility.min()
            min_sea_pressure = month_sea_pressure.min()

            median_high_temp = month_high_temp.median()
            median_low_temp = month_low_temp.median()
            median_avg_temp = month_avg_temp.median()
            median_precipitation = month_precipitation.median()
            median_dew_point = month_dew_point.median()
            median_high_dew_point = month_high_dew_point.median()
            median_low_dew_point = month_low_dew_point.median()
            median_avg_dew_point = month_avg_dew_point.median()
            median_max_wind_speed = month_max_wind_speed.median()
            median_visibility = month_visibility.median()
            median_sea_pressure = month_sea_pressure.median()

            mode_high_temp = month_high_temp.mode()
            mode_low_temp = month_low_temp.mode()
            mode_avg_temp = month_avg_temp.mode()
            mode_precipitation = month_precipitation.mode()
            mode_dew_point = month_dew_point.mode()
            mode_high_dew_point = month_high_dew_point.mode()
            mode_low_dew_point = month_low_dew_point.mode()
            mode_avg_dew_point = month_avg_dew_point.mode()
            mode_max_wind_speed = month_max_wind_speed.mode()
            mode_visibility = month_visibility.mode()
            mode_sea_pressure = month_sea_pressure.mode()

            std_high_temp = month_high_temp.std()
            std_low_temp = month_low_temp.std()
            std_avg_temp = month_avg_temp.std()
            std_precipitation = month_precipitation.std()
            std_dew_point = month_dew_point.std()
            std_high_dew_point = month_high_dew_point.std()
            std_low_dew_point = month_low_dew_point.std()
            std_avg_dew_point = month_avg_dew_point.std()
            std_max_wind_speed = month_max_wind_speed.std()
            std_visibility = month_visibility.std()
            std_sea_pressure = month_sea_pressure.std()

            month_temp_object = { 
                'month' : str(m),
                'year' : str(year), 
                'location' : location,
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
                'mean_sea_pressure' : round(mean_sea_pressure, 2),
                'median_high_temp' : round(median_high_temp, 2),
                'median_low_temp' : round(median_low_temp, 2),
                'median_avg_temp' : round(median_avg_temp, 2),
                'median_precipitation' : round(median_precipitation, 2),
                'median_dew_point' : round(median_dew_point, 2),
                'median_high_dew_point' : round(median_high_dew_point, 2),
                'median_low_dew_point' : round(median_low_dew_point, 2),
                'median_avg_dew_point' : round(median_avg_dew_point, 2),
                'median_max_wind_speed' : round(median_max_wind_speed, 2),
                'median_month_visibility' : round(median_visibility, 2),
                'median_sea_pressure' : round(median_sea_pressure, 2),
                'mode_high_temp' : round(mode_high_temp[0], 2),
                'mode_low_temp' : round(mode_low_temp[0], 2),
                'mode_avg_temp' : round(mode_avg_temp[0], 2),
                'mode_precipitation' : round(mode_precipitation[0], 2),
                'mode_dew_point' : round(mode_dew_point[0], 2),
                'mode_high_dew_point' : round(mode_high_dew_point[0], 2),
                'mode_low_dew_point' : round(mode_low_dew_point[0], 2),
                'mode_avg_dew_point' : round(mode_avg_dew_point[0], 2),
                'mode_max_wind_speed' : round(mode_max_wind_speed[0], 2),
                'mode_month_visibility' : round(mode_visibility[0], 2),
                'mode_sea_pressure' : round(mode_sea_pressure[0], 2),
                'std_high_temp' : round(std_high_temp, 2),
                'std_low_temp' : round(std_low_temp, 2),
                'std_avg_temp' : round(std_avg_temp, 2),
                'std_precipitation' : round(std_precipitation, 2),
                'std_dew_point' : round(std_dew_point, 2),
                'std_high_dew_point' : round(std_high_dew_point, 2),
                'std_low_dew_point' : round(std_low_dew_point, 2),
                'std_avg_dew_point' : round(std_avg_dew_point, 2),
                'std_max_wind_speed' : round(std_max_wind_speed, 2),
                'std_month_visibility' : round(std_visibility, 2),
                'std_sea_pressure' : round(std_sea_pressure, 2),
                'min_high_temp' : round(min_high_temp, 2),
                'min_low_temp' : round(min_low_temp, 2),
                'min_avg_temp' : round(min_avg_temp, 2),
                'min_precipitation' : round(min_precipitation, 2),
                'min_dew_point' : round(min_dew_point, 2),
                'min_high_dew_point' : round(min_high_dew_point, 2),
                'min_low_dew_point' : round(min_low_dew_point, 2),
                'min_avg_dew_point' : round(min_avg_dew_point, 2),
                'min_max_wind_speed' : round(min_max_wind_speed, 2),
                'min_month_visibility' : round(min_visibility, 2),
                'min_sea_pressure' : round(min_sea_pressure, 2),
                'max_high_temp' : round(max_high_temp, 2),
                'max_low_temp' : round(max_low_temp, 2),
                'max_avg_temp' : round(max_avg_temp, 2),
                'max_precipitation' : round(max_precipitation, 2),
                'max_dew_point' : round(max_dew_point, 2),
                'max_high_dew_point' : round(max_high_dew_point, 2),
                'max_low_dew_point' : round(max_low_dew_point, 2),
                'max_avg_dew_point' : round(max_avg_dew_point, 2),
                'max_max_wind_speed' : round(max_max_wind_speed, 2),
                'max_month_visibility' : round(max_visibility, 2),
                'max_sea_pressure' : round(max_sea_pressure, 2)
            }

            list_month_temp.append(month_temp_object)

monthly_mean_weather = DataFrame(list_month_temp)
monthly_mean_weather.to_csv('data/monthly_mean_weather.csv')