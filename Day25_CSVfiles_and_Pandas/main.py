import pandas as pd
import csv  # in python, there is a library for working with csv files as python is very useful in data related fields

with open("weather.csv") as file:
    weather_list = file.readlines()
    print(weather_list)


with open("weather.csv") as file:
    weather_list = csv.reader(file)
    temperature = []
    for row in weather_list:
        if row[1] != "temp":  # When I didn't write this line it was showing invalid literal means temp was string and
            # I was trying to make it int we cant make strings to int
            temperature.append(int(row[1]))

    print(temperature)

