"""IMPORT"""
# import requests
# with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
#   open("psenice.csv", 'w', encoding="utf-8").write(r.text)

import seaborn as sns
import matplotlib.pyplot as plt
import pandas
from scipy.stats import mannwhitneyu

df = pandas.read_csv("psenice.csv")
print(df)
# HO: Délka zrn obou pšenic jsou stejné
# H1: Délka zrn obou pšenic jsou různé
print(mannwhitneyu(df["Rosa"], df["Canadian"]))
#pvalue=3.522437521029982e-24 < 0.05 -> H0 zamítáme -> délka zrn není stejná
# sns.jointplot("Rosa", "Canadian", df, kind="scatter")
# plt.show()