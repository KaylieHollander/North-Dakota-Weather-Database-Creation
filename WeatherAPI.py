import requests
import json
import sqlite3

class Weather:
    def __init__(self, latitude, longitude, month, day, year, fiveYearAvgTemp, fiveYearMinTemp,
                 fiveYearMaxTemp, fiveYearAvgWindSpeed, fiveYearMinWindSpeed, fiveYearMaxWindSpeed,
                 fiveYearRainSum, fiveYearRainMin, fiveYearRainMax):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.fiveYearAvgTemp = fiveYearAvgTemp
        self.fiveYearMinTemp = fiveYearMinTemp
        self.fiveYearMaxTemp = fiveYearMaxTemp
        self.fiveYearAvgWindSpeed = fiveYearAvgWindSpeed
        self.fiveYearMinWindSpeed = fiveYearMinWindSpeed
        self.fiveYearMaxWindSpeed = fiveYearMaxWindSpeed
        self.fiveYearRainSum = fiveYearRainSum
        self.fiveYearRainMin = fiveYearRainMin
        self.fiveYearRainMax = fiveYearRainMax

    def mean_temp2019():
        temp2019 = requests.get('https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2019-05-22&end_date=2019-05-22&daily=temperature_2m_mean&temperature_unit=fahrenheit')
        temp_data2019 = temp2019.json()
        return temp_data2019

    def mean_temp2020():
        temp2020 = requests.get('https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2020-05-22&end_date=2020-05-22&daily=temperature_2m_mean&temperature_unit=fahrenheit')
        temp_data2020 = temp2020.json()
        return temp_data2020

    def mean_temp2021():
        temp2021 = requests.get('https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2021-05-22&end_date=2021-05-22&daily=temperature_2m_mean&temperature_unit=fahrenheit')
        temp_data2021 = temp2021.json()
        return temp_data2021

    def mean_temp2022():
        temp2022 = requests.get('https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2022-05-22&end_date=2022-05-22&daily=temperature_2m_mean&temperature_unit=fahrenheit')
        temp_data2022 = temp2022.json()
        return temp_data2022

    def mean_temp2023():
        temp2023 = requests.get('https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2023-05-22&end_date=2023-05-22&daily=temperature_2m_mean&temperature_unit=fahrenheit')
        temp_data2023 = temp2023.json()
        return temp_data2023

    def max_wind2019():
        url2019 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2019-05-22&end_date=2019-05-22&daily=wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph'
        wind2019 = requests.get(url2019)
        wind_data2019 = wind2019.json()
        return wind_data2019

    def max_wind2020():
        url2020 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2020-05-22&end_date=2020-05-22&daily=wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph'
        wind2020 = requests.get(url2020)
        wind_data2020 = wind2020.json()
        return wind_data2020

    def max_wind2021():
        url2021 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2021-05-22&end_date=2021-05-22&daily=wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph'
        wind2021 = requests.get(url2021)
        wind_data2021 = wind2021.json()
        return wind_data2021

    def max_wind2022():
        url2022 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2022-05-22&end_date=2022-05-22&daily=wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph'
        wind2022 = requests.get(url2022)
        wind_data2022 = wind2022.json()
        return wind_data2022

    def max_wind2023():
        url2023 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2023-05-22&end_date=2023-05-22&daily=wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph'
        wind2023 = requests.get(url2023)
        wind_data2023 = wind2023.json()
        return wind_data2023

    def precip_sum2019():
        url2019 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2019-05-22&end_date=2019-05-22&daily=precipitation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'
        precipitation2019 = requests.get(url2019)
        precipitation_data2019 = precipitation2019.json()
        return precipitation_data2019

    def precip_sum2020():
        url2020 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2020-05-22&end_date=2020-05-22&daily=precipitation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'
        precipitation2020 = requests.get(url2020)
        precipitation_data2020 = precipitation2020.json()
        return precipitation_data2020

    def precip_sum2021():
        url2021 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2021-05-22&end_date=2021-05-22&daily=precipitation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'
        precipitation2021 = requests.get(url2021)
        precipitation_data2021 = precipitation2021.json()
        return precipitation_data2021

    def precip_sum2022():
        url2022 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2022-05-22&end_date=2022-05-22&daily=precipitation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'
        precipitation2022 = requests.get(url2022)
        precipitation_data2022 = precipitation2022.json()
        return precipitation_data2022

    def precip_sum2023():
        url2023 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2023-05-22&end_date=2023-05-22&daily=precipitation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'
        precipitation2023 = requests.get(url2023)
        precipitation_data2023 = precipitation2023.json()
        return precipitation_data2023

