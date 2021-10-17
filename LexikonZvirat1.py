import pandas as pd

#IMPORT
"""import requests
r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)"""

lexikon = pd.read_csv("lexikon-zvirat.csv", sep=";")
lexikon = lexikon.dropna(subset=["title"])
lexikon = lexikon.dropna(how="all", axis="columns")
lexikon = lexikon.set_index("id")


def check_url (radek):
    if not isinstance(radek.image_src, str) \
            or not radek.image_src.startswith("https://zoopraha.cz/images/")\
            or ".jpg" not in radek.image_src.lower():
                return radek.title


for radek in lexikon.itertuples():
    print(check_url(radek))


