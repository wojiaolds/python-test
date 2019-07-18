import pandas as pd
import numpy as np
from multiprocessing import Pool
import os, time, random

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pages = 0
with open('F:\\GitHub\\python\\python-test\\oracle\\total\\is_cash_2.txt', 'r') as f:
    pages = int(f.read())
    print(pages)

for i in range(pages):
    print(i)
    df = pd.read_csv('order\order_is_cash_2_%02d.csv' % i, encoding='gbk')
    if i == 0:
        df.to_csv('total\order_is_cash_2.csv', mode='a', encoding='gbk', index=False)
    else:
        df.to_csv('total\order_is_cash_2.csv', mode='a',encoding='gbk', index=False,header=0)




# df_list =[]
# for i in range(pages):
#     df = pd.read_csv('order\order_is_cash_2_%02d.csv' % i,encoding='gbk')
#     # print(df.head(1))
#     # print(df.dtypes)
#     df_list.append(df)
#
# w = pd.concat(df_list)
#
# w['pan'] = w['pan'].astype('int64')
# print(w.dtypes)
# print(w)
# w.to_csv('total\order_is_cash_2.csv', encoding='gbk', index=False)