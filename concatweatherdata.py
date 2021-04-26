import pandas as pd
from pandas import DataFrame

# wd_1990_1999 = pd.read_csv('weather_data_1990_1999.csv')
# wd_2000_2000 = pd.read_csv('weather_data_2000_2000.csv')
# wd_2001_2009 = pd.read_csv('weather_data_2001_2009.csv')
# wd_2010_2020 = pd.read_csv('weather_data.csv')

# wd_concat = pd.concat([wd_1990_1999, wd_2000_2000, wd_2001_2009, wd_2010_2020])
# wd_concat['date'] = pd.to_datetime(wd_concat['date'])
# wd_concat = wd_concat.sort_values('date')
# wd_concat.to_csv('weather_data_colorado.csv')

wd_colorado = pd.read_csv('data/weather_data_colorado.csv')
wd_arkansas = pd.read_csv('data/weather_data_arkansas.csv')
wd_colorado['location'] = 'colorado'
wd_arkansas['location'] = 'arkansas'
wd_combine = pd.concat([wd_colorado, wd_arkansas])
wd_combine = wd_combine.reset_index()
wd_combine = wd_combine.drop([wd_combine.columns[0],wd_combine.columns[1],wd_combine.columns[2]], axis=1)
wd_combine['date'] = pd.to_datetime(wd_combine['date'])

test_data_pm = wd_combine[wd_combine['high_temp_actual'].str.contains('PM')]
test_data_am = wd_combine[wd_combine['high_temp_actual'].str.contains('AM')]

wd_combine = wd_combine.drop(test_data_pm.index)
wd_combine = wd_combine.drop(test_data_am.index)

wd_combine['high_temp_actual'] = pd.to_numeric(wd_combine['high_temp_actual'])
wd_combine['low_temp_actual'] = pd.to_numeric(wd_combine['low_temp_actual'])
wd_combine['avg_temp_actual'] = pd.to_numeric(wd_combine['avg_temp_actual'])
wd_combine['precipitation_actual'] = pd.to_numeric(wd_combine['precipitation_actual'])
wd_combine['dew_point_actual'] = pd.to_numeric(wd_combine['dew_point_actual'])
wd_combine['high_dew_point_actual'] = pd.to_numeric(wd_combine['high_dew_point_actual'])
wd_combine['low_dew_point_actual'] = pd.to_numeric(wd_combine['low_dew_point_actual'])
wd_combine['avg_dew_point_actual'] = pd.to_numeric(wd_combine['avg_dew_point_actual'])
wd_combine['max_wind_speed_actual'] = pd.to_numeric(wd_combine['max_wind_speed_actual'])
wd_combine['visibility_actual'] = pd.to_numeric(wd_combine['visibility_actual'])
wd_combine['sea_pressure_actual'] = pd.to_numeric(wd_combine['sea_pressure_actual'])

wd_combine.to_csv('data/weather_data_by_location.csv')
