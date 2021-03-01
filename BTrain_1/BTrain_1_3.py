#Imports
import pandas as pd
from pandas import DataFrame


#Define variable for file
df = pd.read_csv('Tezos_1.csv')

#Process Data
#print(df.index)
#print(df.columns)

#print(df["Open"])

c = df[0:3]
print(c)

d = df.iloc[5]
print(d)

