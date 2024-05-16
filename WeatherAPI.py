import requests
import pandas
import sqlalchemy

class instanceVars:
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


def mean_temp():
    url2019 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2019-05-22&end_date=2019-05-22&daily=temperature_2m_mean&temperature_unit=fahrenheit'
    url2020 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2020-05-22&end_date=2020-05-22&daily=temperature_2m_mean&temperature_unit=fahrenheit'
    url2021 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2021-05-22&end_date=2021-05-22&daily=temperature_2m_mean&temperature_unit=fahrenheit'
    url2022 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2022-05-22&end_date=2022-05-22&daily=temperature_2m_mean&temperature_unit=fahrenheit'
    url2023 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2023-05-22&end_date=2023-05-22&daily=temperature_2m_mean&temperature_unit=fahrenheit'

    temp2019 = requests.get(url2019)
    temp2020 = requests.get(url2020)
    temp2021 = requests.get(url2021)
    temp2022 = requests.get(url2022)
    temp2023 = requests.get(url2023)

    temp_data2019 = temp2019.json()
    temp_data2020 = temp2020.json()
    temp_data2021 = temp2021.json()
    temp_data2022 = temp2022.json()
    temp_data2023 = temp2023.json()

    average_temps = (temp_data2019, temp_data2020, temp_data2021, temp_data2022, temp_data2023)
    return average_temps


def max_wind():
    url2019 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2019-05-22&end_date=2019-05-22&daily=wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph'
    url2020 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2020-05-22&end_date=2020-05-22&daily=wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph'
    url2021 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2021-05-22&end_date=2021-05-22&daily=wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph'
    url2022 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2022-05-22&end_date=2022-05-22&daily=wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph'
    url2023 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2023-05-22&end_date=2023-05-22&daily=wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph'

    wind2019 = requests.get(url2019)
    wind2020 = requests.get(url2020)
    wind2021 = requests.get(url2021)
    wind2022 = requests.get(url2022)
    wind2023 = requests.get(url2023)

    wind_data2019 = wind2019.json()
    wind_data2020 = wind2020.json()
    wind_data2021 = wind2021.json()
    wind_data2022 = wind2022.json()
    wind_data2023 = wind2023.json()

    maximum_wind = (wind_data2019, wind_data2020, wind_data2021, wind_data2022, wind_data2023)
    return maximum_wind

def precip_sum():
    url2019 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2019-05-22&end_date=2019-05-22&daily=precipitation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'
    url2020 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2020-05-22&end_date=2020-05-22&daily=precipitation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'
    url2021 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2021-05-22&end_date=2021-05-22&daily=precipitation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'
    url2022 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2022-05-22&end_date=2022-05-22&daily=precipitation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'
    url2023 = 'https://archive-api.open-meteo.com/v1/archive?latitude=46.8083&longitude=-100.7837&start_date=2023-05-22&end_date=2023-05-22&daily=precipitation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'

    precipitation2019 = requests.get(url2019)
    precipitation2020 = requests.get(url2020)
    precipitation2021 = requests.get(url2021)
    precipitation2022 = requests.get(url2022)
    precipitation2023 = requests.get(url2023)

    precipitation_data2019 = precipitation2019.json()
    precipitation_data2020 = precipitation2020.json()
    precipitation_data2021 = precipitation2021.json()
    precipitation_data2022 = precipitation2022.json()
    precipitation_data2023 = precipitation2023.json()

    precipitation_sum = (precipitation_data2019, precipitation_data2020, precipitation_data2021, precipitation_data2022, precipitation_data2023)
    return precipitation_sum






