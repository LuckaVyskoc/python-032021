"""IMPORT"""
# import requests
# with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
#   open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

import pandas as pd
from scipy.stats import mannwhitneyu

castice = pd.read_csv('air_polution_ukol.csv')
castice["date"] = pd.to_datetime(castice["date"])
castice['rok'] = castice['date'].dt.year
castice['mesic'] = castice['date'].dt.month
#print(castice)
#vyber = castice[(castice.rok>2018)&(castice.rok<2021)&(castice.mesic==1)]
vyber19 = castice[(castice.rok==2019)&(castice.mesic==1)]["pm25"].dropna()
vyber20 = castice[(castice.rok==2020)&(castice.mesic==1)]["pm25"].dropna()
#H0: průměrné množství jemných částic je v obou letech v lednu stejné
#H1: průměrné množství jemných částic není v obou letech v lednu stejné
print(mannwhitneyu(vyber19, vyber20))
#pvalue=0.011721695410358317 < 0.05 -> H0 zamítáme -> množství částic není stejné