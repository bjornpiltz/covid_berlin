import pandas as pd

# Read Berlin Covid-19 cases  and convert from wide to long format.
df = pd.read_csv("http://ftp.berlinonline.de/lageso/corona/csv/meldedatum_bezirk.csv", sep=';')
df = df.melt(id_vars="Datum")
df = df.rename(columns={"Datum": "date", "variable": "location", "value" : "new_cases"})
df.set_index('date', inplace=True)
df.to_csv("LAGeSo.csv")
