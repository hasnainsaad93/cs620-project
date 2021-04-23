import pandas as pd
from pandas import DataFrame

wd_1990_1999 = pd.read_csv('weather_data_1990_1999.csv')
wd_2000_2000 = pd.read_csv('weather_data_2000_2000.csv')
wd_2001_2009 = pd.read_csv('weather_data_2001_2009.csv')
wd_2010_2020 = pd.read_csv('weather_data.csv')

wd_concat = pd.concat([wd_1990_1999, wd_2000_2000, wd_2001_2009, wd_2010_2020])
wd_concat['date'] = pd.to_datetime(wd_concat['date'])
wd_concat = wd_concat.sort_values('date')
wd_concat.to_csv('weather_data_colorado.csv')
