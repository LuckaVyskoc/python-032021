"""Tempo růstu
Pokračuj v práci s daty o kryptoměnách.
Z datového souboru si vyber jednu kryptoměnu a urči průměrné denní tempo růstu měny za sledované období.
Můžeš využít funkci geometric_mean z modulu statistics. Vyber si sloupec se změnou ceny, kterou máš
vypočítanou z předchozího cvičení (případně si jej dopočti), přičti k němu 1 (nemusíš dělit stem jako v lekci,
hodnoty jsou jako desetinná čísla, nikoli jako procenta) a převeď jej na seznam pomocí metody .tolist().
Následně vypočti geometrický průměr z těchto hodnot.
Např. pro měnu XMR (Monero) vychází průměrný mezidenní růst ceny na 0.001794558895."""


import pandas as pd
import statistics

#import
# import requests
# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
# open("crypto_prices.csv", "wb").write(r.content)

meny = pd.read_csv("crypto_prices.csv")
meny = meny.sort_values(["Date"])
meny["predchozi den"]= meny.groupby("Symbol")["Close"].shift(1)
meny["zmena"] = (meny["Close"]-meny["predchozi den"])/meny["predchozi den"]
meny["rust"] = meny["zmena"]+1
#nejsem si jistá, co v "rust" počítám
#print(meny)

Rust = meny[meny['Symbol'] == "XMR"].iloc[:,-1].dropna().tolist()
#print(Rust)
print(statistics.geometric_mean(Rust)-1)