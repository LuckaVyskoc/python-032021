import pandas as pd
import numpy

'''IMPORT'''
# import requests
# with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
#   open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)
# with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
#   open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

'''Swing states'''
# V případě amerických prezidentských voleb obecně platí, že ve většině států dlouhodobě vyhrávají
# kandidáti jedné strany. Například v Kalifornii vyhrává kandidát Demokratické strany or roku 1992,
# v Texasu kandidát Republikánské strany od roku 1980, v Kansasu do konce od roku 1968 atd. Státy,
# kde se vítězné strany střídají, jsou označovány jako "swing states" ("kolísavé státy").
# Tvým úkolem je vybrat státy, které lze označit jako swing states.
# V souboru 1976-2020-president.csv najdeš historické výsledky amerických prezidentských voleb.
# Každý řádek souboru obsahuje počet hlasů pro kandidáta dané strany v daném roce.
# V souboru jsou důležité následující sloupce:
# Year - rok voleb,
# State - stát,
# party_simplified - zjednodušené označení politické strany,
# candidatevotes - počet hlasů pro vybraného kandidáta,
# totalvotes - celkový počet odevzdaných hlasů.
# Urči pořadí jednotlivých kandidátů v jednotlivých státech a v jednotlivých letech (pomocí metody rank()).
# Nezapomeň, že data je před použitím metody nutné seřadit a spolu s metodou rank() je nutné použít metodu groupby().
# Pro další analýzu jsou důležití pouze vítězové. Ponech si v tabulce pouze řádky, které obsahují vítěze voleb
# v jednotlivých letech v jednotlivých státech.
# Pomocí metody shift() přidej nový sloupec, abys v jednotlivých řádcích měl(a) po sobě vítězné strany ve dvou
# po sobě jdoucích letech.
# Porovnej, jestli se ve dvou po sobě jdoucích letech změnila vítězná strana. Můžeš k tomu použít např. funkce
# numpy.where a vložit hodnotu 0 nebo 1 podle toho, jestli došlo ke změně vítězné strany.
# Proveď agregaci podle názvu státu a seřaď státy podle počtu změn vítězných stran.

volby = pd.read_csv("1976-2020-president.csv")
volby['rank']=volby.groupby(["state",'year'])['candidatevotes'].rank(method="min", ascending=False)
vitezove =volby[volby["rank"] == 1]
vitezoveRazeno = vitezove.sort_values(["state", "year"])
vitezoveRazeno['PredchoziVolby'] = vitezoveRazeno.groupby(['state'])["party_simplified"].shift(1)
vitezoveRazeno2 = vitezoveRazeno.dropna(subset=['PredchoziVolby']).reset_index(drop=True)
vitezoveRazeno2["srovnani"] = numpy.where(vitezoveRazeno2["party_simplified"] == vitezoveRazeno2['PredchoziVolby'] , 0, 1)
vyhodnoceni = vitezoveRazeno2.groupby(["state"])["srovnani"].sum()
vyhodniceniRazeno = vyhodnoceni.sort_values()
print(vitezoveRazeno2.head(20).to_string())
print(vyhodniceniRazeno)

#Jemné částice
'''V souboru air_polution_ukol.csv najdeš data o množství jemných částic změřených v ovzduší
v jedné plzeňské meteorologické stanici.
Načti dataset a převeď sloupec date (datum měření) na typ datetime.
Přidej sloupce s rokem a číslem měsíce, které získáš z data měření.
Vytvoř pivot tabulku s průměrným počtem množství jemných částic (sloupec pm25) v jednotlivých měsících
a jednotlivých letech. Jako funkci pro agregaci můžeš použít numpy.mean.'''

castice = pd.read_csv('air_polution_ukol.csv')
castice["date"] = pd.to_datetime(castice["date"])
castice['rok'] = castice['date'].dt.year
castice['mesic'] = castice['date'].dt.month
casticeKT = pd.pivot_table(castice, index='rok',columns="mesic",values="pm25", aggfunc=numpy.mean)
print(casticeKT.to_string())