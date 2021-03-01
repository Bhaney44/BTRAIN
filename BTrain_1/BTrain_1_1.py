#Imports
import pandas as pd
from pandas import DataFrame

#Define variable for file
df = pd.read_csv('Tezos_1.csv')

#Process Data
#print(df.index)
#print(df.columns)

#print(df["Open"])

c = df["Open"]-df["Close"]
print(c)
