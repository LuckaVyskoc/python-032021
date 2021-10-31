import pandas
import pandas as pd
import numpy as np
import seaborn as sns
import statistics
import matplotlib.pyplot as plt

#import
"""import requests
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)"""

meny = pd.read_csv("crypto_prices.csv")
meny = meny.sort_values(["Date"])
meny["predchozi den"]= meny.groupby("Symbol")["Close"].shift(1)
meny["zmena"] = (meny["Close"]-meny["predchozi den"])/meny["predchozi den"]
print(meny.head().to_string())

df = pd.pivot_table(meny, index="Date", columns="Symbol", values="zmena",aggfunc=np.sum)
#print(df.tail(10).to_string())

korelMat = pandas.DataFrame(df.corr().abs())
print(korelMat)

def get_redundant_pairs(df):
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def get_top_abs_correlations(df, n):
    au_corr = korelMat.unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corrMAX = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    au_corrMIN = au_corr.drop(labels=labels_to_drop).sort_values(ascending=True)
    return au_corrMAX[0:n],  au_corrMIN[0:n]

mat = pd.DataFrame(get_top_abs_correlations(df,1))
maxX=mat.columns[0][0]
maxY=mat.columns[0][1]
minX=mat.columns[1][0]
minY=mat.columns[1][1]

#sns.heatmap(korelMat, annot=True,fmt='.3g', linewidths=.1, cmap="YlGn")
#max WBTC x BTC
#min USCD x XLM

sns.jointplot(maxX,maxY,korelMat, kind="scatter")
sns.jointplot(minX,minY,korelMat, kind="scatter")
plt.show()
