import pandas as pd
from pandas import DataFrame
import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

years = [item for item in range(1990, 2021)]

monthly_mean_weather = pd.read_csv('data/monthly_mean_weather.csv')
crop_data = pd.read_csv('data/actual_crop_data.csv')

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

    filtered_crop_data = crop_data[(crop_data['year'] == year) & (crop_data['county_name'] == 'COLORADO')]

    if len(filtered_crop_data.index) > 0:
        acre_planted = filtered_crop_data.iloc[0]['acre_planted']
        acre_harvested = filtered_crop_data.iloc[0]['acre_harvested']
        acres_loss = filtered_crop_data.iloc[0]['acres_loss']
        yield_lb_per_acres = filtered_crop_data.iloc[0]['yield_lb_per_acres']

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
        'yield_lb_per_acres': yield_lb_per_acres
        }
        index = index + 1
        relational_data_list.append(related_object)

relational_data = DataFrame(relational_data_list)
relational_data = relational_data.sort_values(by=['std_high_temp'])
# relational_data['std_high_temp'] = relational_data.index
fig, axs = plt.subplots(ncols=3, nrows=3)

sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='std_high_temp', ax=axs[0][0])
sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='std_dew_point', ax=axs[0][1])
sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='std_precipitation', ax=axs[0][2])
sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='std_max_wind_speed', ax=axs[1][0])
sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='std_sea_pressure', ax=axs[1][1])
sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='std_visibility', ax=axs[1][2])
sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='std_low_temp', ax=axs[2][0])
sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='std_avg_temp', ax=axs[2][1])
sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='std_high_dew_point', ax=axs[2][2])

# sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='mean_high_temp', ax=axs[0][0])
# sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='mean_dew_point', ax=axs[0][1])
# sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='mean_precipitation', ax=axs[0][2])
# sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='mean_max_wind_speed', ax=axs[1][0])
# sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='mean_sea_pressure', ax=axs[1][1])
# sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='mean_visibility', ax=axs[1][2])
# sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='mean_low_temp', ax=axs[2][0])
# sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='mean_avg_temp', ax=axs[2][1])
# sns.scatterplot(data=relational_data, x='yield_lb_per_acres', y='mean_high_dew_point', ax=axs[2][2])

plt.show()




