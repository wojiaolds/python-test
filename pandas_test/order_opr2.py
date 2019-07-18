import pandas as pd
import numpy as np
from multiprocessing import Pool
import os, time, random

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

if __name__ == '__main__':
    df = pd.DataFrame()
    for day in range(1,32):
        df1 = pd.read_csv('order\order1805%02d.csv' % day,encoding='gbk')
        df1 = df1[['user_account','category']]
        df1.set_index(['user_account'], inplace=True)
        # print(df1.head())
        if day == 1:
            df = df1
        else:
            df = df.append(df1)

    df = df[~df.index.duplicated()]
    print(df)

    df.to_csv('total\category.csv', encoding='gbk', index=True)