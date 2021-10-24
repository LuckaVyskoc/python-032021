import pandas
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt
import numpy
import psycopg2


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

inspector = inspect(engine) #prohlížení
#print(inspector.get_table_names())
#print(inspector.get_columns('crime'))

"""[{'name': 'CASE#', 'type': TEXT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'DATE_OF_OCCURRENCE', 'type': TEXT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'BLOCK', 'type': TEXT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'IUCR', 'type': TEXT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'PRIMARY_DESCRIPTION', 'type': TEXT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'SECONDARY_DESCRIPTION', 'type': TEXT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'LOCATION DESCRIPTION', 'type': TEXT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'ARREST', 'type': TEXT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'DOMESTIC', 'type': TEXT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'BEAT', 'type': BIGINT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'WARD', 'type': DOUBLE_PRECISION(precision=53), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'FBI CD', 'type': TEXT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'X COORDINATE', 'type': DOUBLE_PRECISION(precision=53), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'Y COORDINATE', 'type': DOUBLE_PRECISION(precision=53), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'LATITUDE', 'type': DOUBLE_PRECISION(precision=53), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'LONGITUDE', 'type': DOUBLE_PRECISION(precision=53), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None},
 {'name': 'LOCATION', 'type': TEXT(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}]
"""

crime = pandas.read_sql("crime", con=engine)
# print(crime.head().to_string())
# kradeze_aut = pandas.read_sql('''
# SELECT *
# FROM crime
# WHERE PRIMARY_DESCRIPTION = 'MOTOR VEHICLE THEFT'
# '''
# , con=engine)  #NEVIDÍM CHYBU V SQL DOTAZU - HLÁSÍ MI TO, ŽE column "primary_description" does not exist

kradeze_aut = crime[crime['PRIMARY_DESCRIPTION'] == "MOTOR VEHICLE THEFT"]

df = kradeze_aut[kradeze_aut['SECONDARY_DESCRIPTION'] == 'AUTOMOBILE']
#df['Date'] = pandas.to_datetime(df['DATE_OF_OCCURRENCE'])
df['month'] = pandas.DatetimeIndex(df['DATE_OF_OCCURRENCE']).month
kradeze_KT= pandas.pivot_table(df, values="SECONDARY_DESCRIPTION", index="month",  aggfunc=numpy.count_nonzero)
kradeze_KT = kradeze_KT.rename(columns={"SECONDARY_DESCRIPTION": "Pocet kradezi"})
print(kradeze_KT.sort_values("Pocet kradezi"))
