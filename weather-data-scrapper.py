from selenium import webdriver
from bs4 import BeautifulSoup
import time
from pandas import DataFrame
import pandas as pd
from threading import Thread

list_except_dates = []
list_weather_data = []

def Weather_Data_Extraction(item):
    try: 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options, executable_path='C:/chromedriver/chromedriver.exe')
        driver.get("https://www.wunderground.com/history/daily/KLIT/date/" + item)
        time.sleep(5)
        squadPage = driver.page_source
        soup = BeautifulSoup(squadPage, 'html.parser')
        table_data = soup.find('table', class_='ng-star-inserted')
        table_rows = table_data.find_all('tr')
        index = 0
        for tr in table_rows:
            td = tr.find_all('td')
            if index == 1:
                high_temp_actual = td[0].text
                high_temp_historical_avg = td[1].text
                high_temp_record = td[2].text
            elif index == 2:
                low_temp_actual = td[0].text
                low_temp_historical_avg = td[1].text
                low_temp_record = td[2].text
            elif index == 3:
                avg_temp_actual = td[0].text
                avg_temp_historical_avg = td[1].text
                avg_temp_record = td[2].text
            elif index == 5:
                precipitation_actual = td[0].text
                precipitation_historical_avg = td[1].text
                precipitation_record = td[2].text
            elif index == 7:
                dew_point_actual = td[0].text
                dew_point_historical_avg = td[1].text
                dew_point_record = td[2].text
            elif index == 8:
                high_dew_point_actual = td[0].text
                high_dew_point_historical_avg = td[1].text
                high_dew_point_record = td[2].text
            elif index == 9:
                low_dew_point_actual = td[0].text
                low_dew_point_historical_avg = td[1].text
                low_dew_point_record = td[2].text 
            elif index == 10:
                avg_dew_point_actual = td[0].text
                avg_dew_point_historical_avg = td[1].text
                avg_dew_point_record = td[2].text    
            elif index == 12:
                max_wind_speed_actual = td[0].text
                max_wind_speed_historical_avg = td[1].text
                max_wind_speed_record = td[2].text  
            elif index == 13:
                visibility_actual = td[0].text
                visibility_historical_avg = td[1].text
                visibility_record = td[2].text     
            elif index == 15:
                sea_pressure_actual = td[0].text
                sea_pressure_historical_avg = td[1].text
                sea_pressure_record = td[2].text  
            
            index = index + 1
            
        weather_object = {  
            "date" : item,
            "high_temp_actual" : high_temp_actual, 
            "high_temp_historical_avg" : high_temp_historical_avg, 
            "high_temp_record" : high_temp_record, 
            "low_temp_actual" : low_temp_actual, 
            "low_temp_historical_avg" : low_temp_historical_avg,
            "low_temp_record" : low_temp_record,
            "avg_temp_actual" : avg_temp_actual,
            "avg_temp_historical_avg" : avg_temp_historical_avg,
            "avg_temp_record" : avg_temp_record,
            "precipitation_actual" : precipitation_actual,
            "precipitation_historical_avg" : precipitation_historical_avg,
            "precipitation_record" : precipitation_record,
            "dew_point_actual" : dew_point_actual,
            "dew_point_historical_avg": dew_point_historical_avg,
            "dew_point_record" : dew_point_record,
            "high_dew_point_actual" : high_dew_point_actual,
            "high_dew_point_historical_avg" : high_dew_point_historical_avg,
            "high_dew_point_record" : high_dew_point_record,
            "low_dew_point_actual" : low_dew_point_actual,
            "low_dew_point_historical_avg" : low_dew_point_historical_avg,
            "low_dew_point_record" : low_dew_point_record,
            "avg_dew_point_actual" : avg_dew_point_actual,
            "avg_dew_point_historical_avg": avg_dew_point_historical_avg,
            "avg_dew_point_record" : avg_dew_point_record,
            "max_wind_speed_actual" : max_wind_speed_actual,
            "max_wind_speed_historical_avg" : max_wind_speed_historical_avg,
            "max_wind_speed_record" : max_wind_speed_record,
            "visibility_actual" : visibility_actual,
            "visibility_historical_avg" : visibility_historical_avg,
            "visibility_record" : visibility_record,
            "sea_pressure_actual" : sea_pressure_actual,
            "sea_pressure_historical_avg" : sea_pressure_historical_avg,
            "sea_pressure_record" : sea_pressure_record
        }

        list_weather_data.append(weather_object)
    except Exception as e:
        print('Exception raised')
        print(e)
        list_except_dates.append(item)

    

date_list = pd.date_range('1990-01-01', '2020-12-31', freq="D")
# date_list_except = list((pd.read_csv('arkansas_date_except.csv')).iloc[:,1])


check_index = 0
list_of_threads = []

for date_item in date_list:
    item = str(date_item.year) + '-' + str(date_item.month) + '-' + str(date_item.day)
    check_index = check_index + 1
    list_of_threads.append(Thread(target=Weather_Data_Extraction, args=(item,)))
    
    if check_index == 10:
        for thread_item in list_of_threads:
            thread_item.start()
        for thread_item in list_of_threads:
            thread_item.join()

        list_of_threads.clear()
        check_index = 0

weather_data = DataFrame(list_weather_data)
weather_data.to_csv('weather_data_arkansas.csv')
except_dates_data = DataFrame(list_except_dates)
except_dates_data.to_csv('except_dates_arkansas.csv')

print('Weather Data Completed!')