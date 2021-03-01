#Imports
import pandas as pd
from pandas import DataFrame

import numpy as np


#Define variable for file
df = pd.read_csv('Tezos_1.csv')

#Process Data

df.to_numpy()
a = df[1:4]
#print(a)

b = df.T
print(b)
