import pandas as pd
from pandas import DataFrame
import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

weather_data = pd.read_csv('data/weather_data_by_location.csv')
weather_data['date'] = pd.to_datetime(weather_data['date'])
weather_data = weather_data[weather_data['location'] == 'arkansas']

monthly_mean_weather = pd.read_csv('data/monthly_mean_weather.csv')
monthly_mean_weather = monthly_mean_weather[monthly_mean_weather['location'] == 'arkansas']

highest_temp_by_year = weather_data.groupby([weather_data['date'].dt.month.rename('month'), weather_data['date'].dt.year.rename('year')])['high_temp_actual'].agg(['max'])
highest_temp_by_year = highest_temp_by_year.reset_index()
highest_temp_by_year = highest_temp_by_year[highest_temp_by_year['year'] > 2009]
sns.barplot(data=highest_temp_by_year, x='year', y='max', hue='month')
plt.show()

# avg_temp_by_year = weather_data.groupby(weather_data['date'].dt.year)['avg_temp_actual'].agg(['max'])
# avg_temp_by_year = avg_temp_by_year.reset_index()
# avg_temp_by_year.plot.bar(x='date', y='max')
# plt.show()


# max_perc_by_year = weather_data.groupby(weather_data['date'].dt.year)['precipitation_actual'].agg(['max'])
# max_perc_by_year = max_perc_by_year.reset_index()
# max_perc_by_year.plot.bar(x='date', y='max')
# plt.show()

# max_dew_by_year = weather_data.groupby(weather_data['date'].dt.year)['dew_point_actual'].agg(['max'])
# max_dew_by_year = max_dew_by_year.reset_index()
# max_dew_by_year.plot.bar(x='date', y='max')
# plt.show()
# monthly_mean_weather = monthly_mean_weather[monthly_mean_weather['year'] > 2009]
# sns.barplot(data=monthly_mean_weather, x='year', y='mean_dew_point', hue='month')
# plt.show()

# sns.lineplot(data=monthly_mean_weather, x='year', y='mean_avg_temp', hue="month")
# plt.show()

# sns.lineplot(data=monthly_mean_weather, x='month', y='mean_avg_temp', hue="year")
# plt.show()

# sns.lineplot(data=monthly_mean_weather, x='year', y='mean_high_temp')
# plt.show()

monthly_mean_weather = monthly_mean_weather[monthly_mean_weather['year'] > 2015]
ax = sns.lineplot(data=monthly_mean_weather, x='month', y='mean_high_temp', hue="year")
ax.set(xticks=monthly_mean_weather.month)
plt.show()