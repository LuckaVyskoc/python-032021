import requests
import pandas
import statsmodels.formula.api as smf

"""IMPORT"""
# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
# with open("Fish.csv", "wb") as f:
#   f.write(r.content)

df = pandas.read_csv("Fish.csv")
print(df.head().to_string())
#['Species', 'Weight', 'Length1', 'Length2', 'Length3', 'Height','Width']
df["prumer_Species"] = df["Species"].map(df.groupby('Species')['Weight'].mean())
#print(df.head(100).to_string())
mod = smf.ols(formula="Weight ~ Length2 + Height + prumer_Species", data=df)
res = mod.fit()
print(res.summary())
# Weight ~ Length2, R-squared:0.844
# Weight ~ Length2 + Height, R-squared:0.875 -> přidáním parametru Height se zvýšila kvalita modelu
# Weight ~ Length2 + Height + prumer_Species, R-squared:0.900 -> přidáním parametru prumer_Species se zvýšila kvalita modelu