import requests
import pandas
import statsmodels.formula.api as smf

"""IMPORT"""
# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
# with open("Concrete_Data_Yeh.csv", "wb") as f:
#   f.write(r.content)

df = pandas.read_csv("Concrete_Data_Yeh.csv")
# ['cement', 'slag', 'flyash', 'water', 'superplasticizer','coarseaggregate', 'fineaggregate', 'age', 'csMPa']
mod = smf.ols(formula="csMPa ~ cement + slag + flyash + water + superplasticizer + coarseaggregate + fineaggregate + age", data=df)
res = mod.fit()
print(res.summary())
# největší kladný vliv na pevnost má superplasticizer (s koef = 0,2922) a pak cement (koef = 0,1198)
# negativní vliv na pevnost má water (koef = -0.1499) - čím víc vody, tím nižší pevnost
# coarseaggregate + fineaggregate  jsou těsně nad hranicí hladiny významnosti 5%, oba komponenty jsou v modelu na sobě závisleé,
# pokud se jedna složka (coarseaggregate + fineaggregate) vyřadí P value hodně vzroste -> pevnost cementu není závislá ani na jedné z těch samostatných složek
# Pvalue všech složek (všechny zároveň) je nižší než O,O5 -> pevnost je závislá na všech uvedených složkách včetně age
# R-squared = 0.616 -> model vysvětluje cca 62% procent rozptylu, což není neijak zvášť kvalitní model