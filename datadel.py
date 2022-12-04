import pandas as pd
import csv
df=pd.read_csv("final.csv")
del df["Luminosity"]
df.to_csv("main.csv")