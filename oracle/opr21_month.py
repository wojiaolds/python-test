import pandas as pd
import numpy as np
from multiprocessing import Pool
import os, time, random



pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('precision', 2)
np.set_printoptions(suppress=True)

df = pd.read_csv('total\order_is_cash_2.csv', encoding='gbk',low_memory=False)
df['DATE_SETTLMT'] = df['DATE_SETTLMT'].astype(object)
print(df.dtypes)
df = df.loc[df["PAN"] != 0, :]
df["PAN"] = df["PAN"].astype(object)
df['MONTH'] = df['DATE_SETTLMT'].map(lambda x: str(x)[0:6])
print(df.dtypes)
print(df.head())
# print(df.shape)
#

# s1 = df.groupby(['mcht_cd','month'])['mcht_cd'].count()
# s2 = df.groupby(['mcht_cd','month'])['trans_amt'].sum()

# df1 = pd.DataFrame(s1)
# df2 = pd.DataFrame(s2)

# df3 = pd.merge(s1, s2, left_index=True, right_index=True)
df3 = df.groupby(['MCHT_CD','MONTH']).agg({'MCHT_CD':'count','TRANS_AMT':'sum'})
df3.rename(columns={'MCHT_CD': '总笔数', 'TRANS_AMT': '总金额'}, inplace=True)
df3['客单价'] = round(df3['总金额'].div(df3['总笔数']),2)
print(df3.head(30))
# print(df3.index)
print('------'*10)
s4 = df.groupby(['MCHT_CD','MONTH','PAN'])['MCHT_CD'].count()
# # print(type(s4))
df4 = pd.DataFrame(s4)
print(df4.head(20))
print('------'*10)
df5 = df4.groupby(level=['MCHT_CD','MONTH'],axis=0).count()
df5.rename(columns={'MCHT_CD': '用户数'}, inplace=True)
print('------'*10)
# # print(df4.index)
# a = np.unique(df4.index.get_level_values(0).values)
# a= list(a)
# # print(a)
# # print(len(a))
# print('------'*10)
# df_list =[]
# for i in a:
#     v = df4.loc[i].index.get_level_values(0).values
#     b= np.unique(v)
#     b = list(b)
#     for j in b:
#         va = df4.loc[i].loc[j].index.get_level_values(0).values
#         # print(va)
#         # print(i,j)
#         multiIndex = pd.MultiIndex.from_arrays([[i],[j]],names=['mcht_cd', 'month'])
#         f = pd.DataFrame([[len(va)]], index=multiIndex, columns=['用户数'])
#         df_list.append(f)
# w = pd.concat(df_list)
# print('------'*10)
# print(df3.index)
# print(w.index)
# print('------'*10)
# print(w.head())
# #
# df5 = pd.merge(df3, w, left_index=True, right_index=True)
# print(df5.index)
# print(df5.head(20))
# #
# #
df5 = pd.merge(df3, df5, left_index=True, right_index=True)
df5['总笔数/用户数'] = round(df5['总笔数'].div(df5['用户数']),2)
df5['总金额/用户数'] = round(df5['总金额'].div(df5['用户数']),2)

# df5['总金额/用户数'] = df5['总金额/用户数'].astype(np.int64)
#
print(df5.head(20))
# print(df5.dtypes)
df5.to_csv('total\order_is_cash_2_hz_mon.csv', encoding='gbk', index=True)