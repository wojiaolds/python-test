import pandas as pd
import numpy as np
from multiprocessing import Pool
import os, time, random

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df1 = pd.read_csv('total\category.csv',encoding='gbk')
# df1['user_account'] = df1['user_account'].astype('int64')
# df1 = df1.loc[df1["user_account"] != '', :]
# df1["user_account"] = df1['user_account'].map(lambda x: int(x))
df1["user_account"] = df1["user_account"].apply(pd.to_numeric, errors='coerce').fillna(0)
df1.set_index(['user_account'], inplace=True)
df1 = df1.sort_index()
print(df1.head())
print(df1.index)

df2 = pd.read_csv('total\order.csv',encoding='gbk')
df2.rename(columns={'用户': 'user_account', }, inplace=True)
df2.set_index(['user_account'], inplace=True)
df2 = df2.sort_index()
print(df2.head())
print(df2.index)

df3 = pd.read_csv('total\order_time.csv',encoding='gbk')
df3.set_index(['user_account'], inplace=True)
df3 = df3.sort_index()
print(df3.head())
print(df3.index)

print(df1.shape)
print(df2.shape)
print(df3.shape)

df = pd.merge(df1, df2, left_index=True, right_index=True,how='outer')
df = pd.merge(df, df3, left_index=True, right_index=True,how='outer')
print(df)
df.to_csv('total\end.csv', encoding='gbk', index=True)


