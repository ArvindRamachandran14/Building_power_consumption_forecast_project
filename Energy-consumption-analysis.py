import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_holidays = pd.read_csv('power-laws-forecasting-energy-consumption-holidays.csv', delimiter=';')
df_holidays['count'] =1

df_energy_consumption = pd.read_csv('power-laws-forecasting-energy-consumption-training-data.csv', delimiter=';')
df_energy_consumption['count']=1

df_weather_data = pd.read_csv('power-laws-forecasting-energy-consumption-weather.csv', delimiter=';')
df_weather_data['count']=1

df_meta_data = pd.read_csv('power-laws-forecasting-energy-consumption-metadata.csv',delimiter=";")
df_meta_data['count']=1

df_test_data = pd.read_csv('power-laws-forecasting-energy-consumption-test-data.csv',delimiter=";")
df_submission = pd.read_csv('power-laws-forecasting-energy-consumption-submission-forecast-period.csv',delimiter=";")


df_energy_consumption_site_grouped = df_energy_consumption.groupby(['SiteId'])
df_meta_data_site_grouped = df_meta_data.groupby(['SiteId'])
df_weather_data_site_grouped = df_weather_data.groupby(['SiteId'])


index_energy_consumption_max = df_energy_consumption_site_grouped.mean()['Value'].idxmax()

index_surface_max = df_meta_data_site_grouped.mean()['Surface'].idxmax()

index_temperature_max = df_weather_data_site_grouped.mean()['Temperature'].idxmin()

sorted_energy = list(df_energy_consumption_site_grouped.mean().sort_index()['Value'])

sorted_surface = list(df_meta_data_site_grouped.mean().sort_index()['Surface'])

#plt.plot(sorted_surface, sorted_energy, 'ko')

plt.plot(df_energy_consumption.loc[df_energy_consumption["SiteId"]==93]['Timestamp'][:1000], df_energy_consumption.loc[df_energy_consumption["SiteId"]==93]['Value'][:1000], 'k-')

plt.show()

#df_energy_consumption["datetime"] = pd.to_datetime(df_energy_consumption['Timestamp'], format='%Y-%M-%dT%H:%M:%S+00:00')

