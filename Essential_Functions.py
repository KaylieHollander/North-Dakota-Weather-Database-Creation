from WeatherAPI import Weather

#Necessary Local Variables
meanTemp2019 = Weather.mean_temp2019()
meanTemp2020 = Weather.mean_temp2020()
meanTemp2021 = Weather.mean_temp2021()
meanTemp2022 = Weather.mean_temp2022()
meanTemp2023 = Weather.mean_temp2023()

wind2019 = Weather.max_wind2019()
wind2020 = Weather.max_wind2020()
wind2021 = Weather.max_wind2021()
wind2022 = Weather.max_wind2022()
wind2023 = Weather.max_wind2023()

precip2019 = Weather.precip_sum2019()
precip2020 = Weather.precip_sum2020()
precip2021 = Weather.precip_sum2021()
precip2022 = Weather.precip_sum2022()
precip2023 = Weather.precip_sum2023()

class Essentials:
    def month():
        datePlaceHolder = meanTemp2019['daily']['time']
        date = ""
        for x in datePlaceHolder:
            date = date + x

        month2 = date[5:7]
        return month2

    def day():
        datePlaceHolder = meanTemp2019['daily']['time']
        date = ""
        for x in datePlaceHolder:
            date = date + x

        day2 = date[8:]
        return day2

    def year():
        datePlaceHolder = meanTemp2019['daily']['time']
        date = ""
        for x in datePlaceHolder:
            date = date + x

        year2 = date[:4]
        return year2

    def TempMax():
        max_temp = 0
        if meanTemp2019['daily']['temperature_2m_mean'] > meanTemp2020['daily']['temperature_2m_mean'] and meanTemp2019['daily']['temperature_2m_mean'] > meanTemp2021['daily']['temperature_2m_mean'] \
                and meanTemp2019['daily']['temperature_2m_mean'] > meanTemp2022['daily']['temperature_2m_mean'] and meanTemp2019['daily']['temperature_2m_mean'] > meanTemp2023['daily']['temperature_2m_mean']:
            max_temp = meanTemp2019['daily']['temperature_2m_mean']
        elif meanTemp2020['daily']['temperature_2m_mean'] > meanTemp2019['daily']['temperature_2m_mean'] and meanTemp2020['daily']['temperature_2m_mean'] > meanTemp2021['daily']['temperature_2m_mean'] \
                and meanTemp2020['daily']['temperature_2m_mean'] > meanTemp2022['daily']['temperature_2m_mean'] and meanTemp2020['daily']['temperature_2m_mean'] > meanTemp2023['daily']['temperature_2m_mean']:
            max_temp = meanTemp2020['daily']['temperature_2m_mean']
        elif meanTemp2021['daily']['temperature_2m_mean'] > meanTemp2019['daily']['temperature_2m_mean'] and meanTemp2021['daily']['temperature_2m_mean'] > meanTemp2020['daily']['temperature_2m_mean'] \
                and meanTemp2021['daily']['temperature_2m_mean'] > meanTemp2022['daily']['temperature_2m_mean'] and meanTemp2021['daily']['temperature_2m_mean'] > meanTemp2023['daily']['temperature_2m_mean']:
            max_temp = meanTemp2021['daily']['temperature_2m_mean']
        elif meanTemp2022['daily']['temperature_2m_mean'] > meanTemp2019['daily']['temperature_2m_mean'] and meanTemp2022['daily']['temperature_2m_mean'] > meanTemp2020['daily']['temperature_2m_mean'] \
                and meanTemp2022['daily']['temperature_2m_mean'] > meanTemp2021['daily']['temperature_2m_mean'] and meanTemp2022['daily']['temperature_2m_mean'] > meanTemp2023['daily']['temperature_2m_mean']:
            max_temp = meanTemp2022['daily']['temperature_2m_mean']
        else:
            max_temp = meanTemp2023['daily']['temperature_2m_mean']

        temp_Place_Holder = ""

        for x in max_temp:
            temp_Place_Holder = temp_Place_Holder + str(x)

        return float(temp_Place_Holder)

    def TempMin():
        min_temp = 0

        if meanTemp2019['daily']['temperature_2m_mean'] < meanTemp2020['daily']['temperature_2m_mean'] and meanTemp2019['daily']['temperature_2m_mean'] < meanTemp2021['daily']['temperature_2m_mean'] \
                and meanTemp2019['daily']['temperature_2m_mean'] < meanTemp2022['daily']['temperature_2m_mean'] and meanTemp2019['daily']['temperature_2m_mean'] < meanTemp2023['daily']['temperature_2m_mean']:
            min_temp = meanTemp2019['daily']['temperature_2m_mean']
        elif meanTemp2020['daily']['temperature_2m_mean'] < meanTemp2019['daily']['temperature_2m_mean'] and meanTemp2020['daily']['temperature_2m_mean'] < meanTemp2021['daily']['temperature_2m_mean'] \
                and meanTemp2020['daily']['temperature_2m_mean'] < meanTemp2022['daily']['temperature_2m_mean'] and meanTemp2020['daily']['temperature_2m_mean'] < meanTemp2023['daily']['temperature_2m_mean']:
            min_temp = meanTemp2020['daily']['temperature_2m_mean']
        elif meanTemp2021['daily']['temperature_2m_mean'] < meanTemp2019['daily']['temperature_2m_mean'] and meanTemp2021['daily']['temperature_2m_mean'] < meanTemp2020['daily']['temperature_2m_mean'] \
                and meanTemp2021['daily']['temperature_2m_mean'] < meanTemp2022['daily']['temperature_2m_mean'] and meanTemp2021['daily']['temperature_2m_mean'] < meanTemp2023['daily']['temperature_2m_mean']:
            min_temp = meanTemp2021['daily']['temperature_2m_mean']
        elif meanTemp2022['daily']['temperature_2m_mean'] < meanTemp2019['daily']['temperature_2m_mean'] and meanTemp2022['daily']['temperature_2m_mean'] < meanTemp2020['daily']['temperature_2m_mean'] \
                and meanTemp2022['daily']['temperature_2m_mean'] < meanTemp2021['daily']['temperature_2m_mean'] and meanTemp2022['daily']['temperature_2m_mean'] < meanTemp2023['daily']['temperature_2m_mean']:
            min_temp = meanTemp2022['daily']['temperature_2m_mean']
        else:
            min_temp = meanTemp2023['daily']['temperature_2m_mean']

        temp_Place_Holder = ""

        for x in min_temp:
            temp_Place_Holder = temp_Place_Holder + str(x)

        return float(temp_Place_Holder)

    def TempAvg():
        averagePlaceHolder1 = (
                    meanTemp2019['daily']['temperature_2m_mean'] + meanTemp2020['daily']['temperature_2m_mean'] +
                    meanTemp2021['daily']['temperature_2m_mean'] + meanTemp2022['daily']['temperature_2m_mean'] +
                    meanTemp2023['daily']['temperature_2m_mean'])

        averagePlaceHolder2 = ""
        num = 0
        for x in averagePlaceHolder1:
            num = num + x

        averagePlaceHolder2 = num

        average = float(averagePlaceHolder2) / 5
        return round(average,2)

    def WindAvg():
        averagePlaceHolder1 = (
                wind2019['daily']['wind_speed_10m_max'] + wind2020['daily']['wind_speed_10m_max'] +
                wind2021['daily']['wind_speed_10m_max'] + wind2022['daily']['wind_speed_10m_max'] +
                wind2023['daily']['wind_speed_10m_max'])

        averagePlaceHolder2 = ""
        num = 0
        for x in averagePlaceHolder1:
            num = num + x

        averagePlaceHolder2 = num

        average = float(averagePlaceHolder2) / 5
        return round(average, 2)

    def WindMax():
        wind_max = 0

        if wind2019['daily']['wind_speed_10m_max'] > wind2020['daily']['wind_speed_10m_max'] and \
                wind2019['daily']['wind_speed_10m_max'] > wind2021['daily']['wind_speed_10m_max'] \
                and wind2019['daily']['wind_speed_10m_max'] > wind2022['daily']['wind_speed_10m_max'] and \
                wind2019['daily']['wind_speed_10m_max'] > wind2023['daily']['wind_speed_10m_max']:
            wind_max = wind2019['daily']['wind_speed_10m_max']
        elif wind2020['daily']['wind_speed_10m_max'] > wind2019['daily']['wind_speed_10m_max'] and \
                wind2020['daily']['wind_speed_10m_max'] > wind2021['daily']['wind_speed_10m_max'] \
                and wind2020['daily']['wind_speed_10m_max'] > wind2022['daily']['wind_speed_10m_max'] and \
                wind2020['daily']['wind_speed_10m_max'] > wind2023['daily']['wind_speed_10m_max']:
            wind_max = wind2020['daily']['wind_speed_10m_max']
        elif wind2021['daily']['wind_speed_10m_max'] > wind2019['daily']['wind_speed_10m_max'] and \
                wind2021['daily']['wind_speed_10m_max'] > wind2020['daily']['wind_speed_10m_max'] \
                and wind2021['daily']['wind_speed_10m_max'] > wind2022['daily']['wind_speed_10m_max'] and \
                wind2021['daily']['wind_speed_10m_max'] > wind2023['daily']['wind_speed_10m_max']:
            wind_max = wind2021['daily']['wind_speed_10m_max']
        elif wind2022['daily']['wind_speed_10m_max'] > wind2019['daily']['wind_speed_10m_max'] and \
                wind2022['daily']['wind_speed_10m_max'] > wind2020['daily']['wind_speed_10m_max'] \
                and wind2022['daily']['wind_speed_10m_max'] > wind2021['daily']['wind_speed_10m_max'] and \
                wind2022['daily']['wind_speed_10m_max'] > wind2023['daily']['wind_speed_10m_max']:
            wind_max = wind2022['daily']['wind_speed_10m_max']
        else:
            wind_max = wind2023['daily']['wind_speed_10m_max']

        wind_Place_Holder = ""

        for x in wind_max:
            wind_Place_Holder = wind_Place_Holder + str(x)

        return float(wind_Place_Holder)

    def WindMin():
        wind_min = 0

        if wind2019['daily']['wind_speed_10m_max'] < wind2020['daily']['wind_speed_10m_max'] and wind2019['daily']['wind_speed_10m_max'] < wind2021['daily']['wind_speed_10m_max'] \
                and wind2019['daily']['wind_speed_10m_max'] < wind2022['daily']['wind_speed_10m_max'] and wind2019['daily']['wind_speed_10m_max'] < wind2023['daily']['wind_speed_10m_max']:
            wind_min = wind2019['daily']['wind_speed_10m_max']
        elif wind2020['daily']['wind_speed_10m_max'] < wind2019['daily']['wind_speed_10m_max'] and wind2020['daily']['wind_speed_10m_max'] < wind2021['daily']['wind_speed_10m_max'] \
                and wind2020['daily']['wind_speed_10m_max'] < wind2022['daily']['wind_speed_10m_max'] and wind2020['daily']['wind_speed_10m_max'] < wind2023['daily']['wind_speed_10m_max']:
            wind_min = wind2020['daily']['wind_speed_10m_max']
        elif wind2021['daily']['wind_speed_10m_max'] < wind2019['daily']['wind_speed_10m_max'] and wind2021['daily']['wind_speed_10m_max'] < wind2020['daily']['wind_speed_10m_max'] \
                and wind2021['daily']['wind_speed_10m_max'] < wind2022['daily']['wind_speed_10m_max'] and wind2021['daily']['wind_speed_10m_max'] < wind2023['daily']['wind_speed_10m_max']:
            wind_min = wind2021['daily']['wind_speed_10m_max']
        elif wind2022['daily']['wind_speed_10m_max'] < wind2019['daily']['wind_speed_10m_max'] and wind2022['daily']['wind_speed_10m_max'] < wind2020['daily']['wind_speed_10m_max'] \
                and wind2022['daily']['wind_speed_10m_max'] < wind2021['daily']['wind_speed_10m_max'] and wind2022['daily']['wind_speed_10m_max'] < wind2023['daily']['wind_speed_10m_max']:
            wind_min = wind2022['daily']['wind_speed_10m_max']
        else:
            wind_min = wind2023['daily']['wind_speed_10m_max']

        wind_Place_Holder = ""

        for x in wind_min:
            wind_Place_Holder = wind_Place_Holder + str(x)

        return float(wind_Place_Holder)

    def PrecipSum():
        averagePlaceHolder1 = (
                precip2019['daily']['precipitation_sum'] + precip2020['daily']['precipitation_sum'] +
                precip2021['daily']['precipitation_sum'] + precip2022['daily']['precipitation_sum'] +
                precip2023['daily']['precipitation_sum'])

        averagePlaceHolder2 = ""
        num = 0
        for x in averagePlaceHolder1:
            num = num + x

        averagePlaceHolder2 = num

        average = float(averagePlaceHolder2)
        return round(average, 2)

    def PrecipMax():
        precip_max = 0

        if precip2019['daily']['precipitation_sum'] > precip2020['daily']['precipitation_sum'] and \
                precip2019['daily']['precipitation_sum'] > precip2021['daily']['precipitation_sum'] \
                and precip2019['daily']['precipitation_sum'] > precip2022['daily']['precipitation_sum'] and \
                precip2019['daily']['precipitation_sum'] > precip2023['daily']['precipitation_sum']:
            precip_max = precip2019['daily']['precipitation_sum']
        elif precip2020['daily']['precipitation_sum'] > precip2019['daily']['precipitation_sum'] and \
                precip2020['daily']['precipitation_sum'] > precip2021['daily']['precipitation_sum'] \
                and precip2020['daily']['precipitation_sum'] > precip2022['daily']['precipitation_sum'] and \
                precip2020['daily']['precipitation_sum'] > precip2023['daily']['precipitation_sum']:
            precip_max = precip2020['daily']['precipitation_sum']
        elif precip2021['daily']['precipitation_sum'] > precip2019['daily']['precipitation_sum'] and \
                precip2021['daily']['precipitation_sum'] > precip2020['daily']['precipitation_sum'] \
                and precip2021['daily']['precipitation_sum'] > precip2022['daily']['precipitation_sum'] and \
                precip2021['daily']['precipitation_sum'] > precip2023['daily']['precipitation_sum']:
            precip_max = precip2021['daily']['precipitation_sum']
        elif precip2022['daily']['precipitation_sum'] > precip2019['daily']['precipitation_sum'] and \
                precip2022['daily']['precipitation_sum'] > precip2020['daily']['precipitation_sum'] \
                and precip2022['daily']['precipitation_sum'] > precip2021['daily']['precipitation_sum'] and \
                precip2022['daily']['precipitation_sum'] > precip2023['daily']['precipitation_sum']:
            precip_max = precip2022['daily']['precipitation_sum']
        else:
            precip_max = precip2023['daily']['precipitation_sum']

        precip_Place_Holder = ""

        for x in precip_max:
            precip_Place_Holder = precip_Place_Holder + str(x)

        return float(precip_Place_Holder)

    def PrecipMin():
        precip_min = 0

        if precip2019['daily']['precipitation_sum'] < precip2020['daily']['precipitation_sum'] and precip2019['daily']['precipitation_sum'] < precip2021['daily']['precipitation_sum'] \
                and precip2019['daily']['precipitation_sum'] < precip2022['daily']['precipitation_sum'] and \
                precip2019['daily']['precipitation_sum'] < precip2023['daily']['precipitation_sum']:
            precip_min = precip2019['daily']['precipitation_sum']
        elif precip2020['daily']['precipitation_sum'] < precip2019['daily']['precipitation_sum'] and precip2020['daily'][
            'precipitation_sum'] < precip2021['daily']['precipitation_sum'] \
                and precip2020['daily']['precipitation_sum'] < precip2022['daily']['precipitation_sum'] and \
                precip2020['daily']['precipitation_sum'] < precip2023['daily']['precipitation_sum']:
            precip_min = precip2020['daily']['precipitation_sum']
        elif precip2021['daily']['precipitation_sum'] < precip2019['daily']['precipitation_sum'] and precip2021['daily'][
            'precipitation_sum'] < precip2020['daily']['precipitation_sum'] \
                and precip2021['daily']['precipitation_sum'] < precip2022['daily']['precipitation_sum'] and \
                precip2021['daily']['precipitation_sum'] < precip2023['daily']['precipitation_sum']:
            precip_min = precip2021['daily']['precipitation_sum']
        elif precip2022['daily']['precipitation_sum'] < precip2019['daily']['precipitation_sum'] and precip2022['daily'][
            'precipitation_sum'] < precip2020['daily']['precipitation_sum'] \
                and precip2022['daily']['precipitation_sum'] < precip2021['daily']['precipitation_sum'] and \
                precip2022['daily']['precipitation_sum'] < precip2023['daily']['precipitation_sum']:
            precip_min = precip2022['daily']['precipitation_sum']
        else:
            precip_min = precip2023['daily']['precipitation_sum']

        precip_Place_Holder = ""

        for x in precip_min:
            precip_Place_Holder = precip_Place_Holder + str(x)

        return float(precip_Place_Holder)







