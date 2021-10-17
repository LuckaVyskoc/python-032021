import pandas as pd

lexikon = pd.read_csv("lexikon-zvirat.csv", sep=";")
lexikon = lexikon.dropna(subset=["title"])
lexikon = lexikon.dropna(how="all", axis="columns")
lexikon = lexikon.set_index("id")

def popisek (radek):
    return f"{radek.title} preferuje následující typ stravy: {radek.food}. Konkrétně ocení, když mu do misky přistanou " \
           f"převážně {radek.food_note}. \nJak toto zvíře poznáme: {radek.description}"

lexikon["popisek"] = lexikon.apply(popisek, axis=1)


print(lexikon.sort_values(by="title")[["popisek"]].head().to_string())

