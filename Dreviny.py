import pandas
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt
import numpy


"""Uživatelské jméno: vyskoc@czechitaspsql
Heslo: Z3bo6zciAOFV1EaW"""

#DATABAZE

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "vyskoc"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "Z3bo6zciAOFV1EaW"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)

inspector = inspect(engine)

#dreviny = pandas.read_sql("dreviny", con=engine)

#print(dreviny.head(20).to_string())
smrk = pandas.read_sql('''
SELECT *
FROM dreviny
WHERE dd_txt = 'Smrk, jedle, douglaska'
order by rok 
'''
, con=engine)

smrk.plot.bar(x="rok", y="hodnota",color=["orange"], title="Vývoj objemu těžby - Smrk, jedle, douglaska")
#print(smrk.to_string())
nahodila_tezba = pandas.read_sql('''
SELECT *
FROM dreviny
WHERE druhtez_txt = 'Nahodilá těžba dřeva'
'''
, con=engine)

nahodila_tezba_KT = pandas.pivot_table(nahodila_tezba, values="hodnota", index="rok", columns="prictez_txt", aggfunc=numpy.sum)
#print(nahodila_tezba_KT.to_string())

nahodila_tezba_KT.plot(kind="bar", y=["Exhalační příčina", "Hmyzová příčina", "Příčina jiná než živelní, exhalační a hmyzová", "Živelní příčina"],
                    color=["red", "green", "black", "blue"], title="Vývoj objemu nahodilé těžby")
plt.legend(["Exhalační příčina", "Hmyzová příčina", "Příčina jiná než živelní, exhalační a hmyzová", "Živelní příčina"])
plt.show()