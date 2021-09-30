import pandas as pd
import numpy

'''IMPORT'''
# import requests
# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
# open("london_merged.csv", 'wb').write(r.content)
# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
# open("titanic.csv", 'wb').write(r.content)

'''TITANIC'''
# V souboru titanic.csv najdeš informace o cestujících na zaoceánském parníku Titanic.
# Vytvoř kontingenční tabulku, která porovná závislost mezi pohlavím cestujícího (soupec Sex),
# třídou (sloupec Pclass), ve které cestoval, a tím, jesti přežil potopení Titanicu
# (sloupec Survived). Pro data můžeš použít agregaci len, numpy.sum, která ti spočte absolutní
# počet přeživších pro danou kombinaci, nebo numpy.mean, která udá relativní počet přeživších pro danou kombinaci.
tit =pd.read_csv('titanic.csv')
titKT = pd.pivot_table(tit, index="Sex", columns="Pclass", values="Survived", aggfunc=numpy.sum)
print(titKT.head().to_string())

'''Půjčování kol'''
# V souboru london_merged.csv najdeš informace o počtu vypůjčení jízdních kol v Londýně.
# Vytvoř sloupec, do kterého z časové značky (sloupec timestamp) ulož rok.
# Vytvoř kontingenční tabulku, která porovná kód počasí (sloupec weather_code se sloupcem udávající rok.
# Definice jednotlivých kódů jsou:
# 1 = Clear ; mostly clear but have some values with haze/fog/patches of fog/ fog in vicinity
# 2 = scattered clouds / few clouds
# 3 = Broken clouds
# 4 = Cloudy
# 7 = Rain/ light Rain shower/ Light rain
# 10 = rain with thunderstorm
# 26 = snowfall
# 94 = Freezing Fog

kola =pd.read_csv('london_merged.csv')
kola["timestamp"] = pd.to_datetime(kola["timestamp"])
kola['rok']=kola['timestamp'].dt.year
kolaKT = pd.pivot_table(kola, index="weather_code", columns='rok', values="cnt", aggfunc=numpy.sum)
print(kola.head())
print(kolaKT.to_string())