import pandas as pd
import numpy as np

def adder(ele1,ele2):
    print(type(ele1))
    return ele1+ele2

def max_min(df):
    return df.max()-df.min()

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df)
print('-----'*10)
df = df.pipe(adder,3)
print(df)
print('-----'*10)
df2 = df.apply(np.mean)
print(df2)
print('-----'*10)
df2 = df.apply(np.mean,axis=1)
print(df2)
print('-----'*10)
df2 = df.apply(lambda x:  x.max() - x.min())
print(df2)
print('-----'*10)
df2 = df.apply(max_min)
print(df2)
print('-----'*10)
print(type(df['col1'].map(lambda x:x*100)))
print(df['col1'].map(lambda x:x*100))
print(df['col1'].apply(lambda x:x*100))
print('-----'*10)
df2 = df.applymap(lambda x:x*100)
print(df2)







