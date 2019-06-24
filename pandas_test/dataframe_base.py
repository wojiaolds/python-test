import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
#Create a DataFrame
df = pd.DataFrame(d)
print(df)
print ("Row axis labels and column axis labels are:")
print(df.axes)
print(df.dtypes)
print(df.shape)
print(df.ndim)
print(df.size)
print(df.values)
print(df.head(2))
print(df.tail(2))


print('------'*10)
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#Create a DataFrame
df = pd.DataFrame(d)
print(df)
print('------'*10)
print(df.sum())
print('------'*10)
print(df.sum(1))
print('------'*10)
print(df.mean())
print('------'*10)
print(df.mean(1))
print('------'*10)
print(df.std())
print('------'*10)
print(df.describe())


print('------'*10)
d = {'Age':pd.Series([-2,5,6]),
   'Rating':pd.Series([1.2,1.3,1.4])}
#Create a DataFrame
df = pd.DataFrame(d)
print(df)
print('------'*10)
print(df.abs())
print(df.prod())
print(df.prod(1))
print(df.cumsum())
print(df.cumprod())



