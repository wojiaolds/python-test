import pandas as pd
import numpy as np
from multiprocessing import Pool
import os, time, random

pages = 0
with open('F:\\GitHub\\python\\python-test\\oracle\\total\\is_cash_3.txt', 'r') as f:
    pages = int(f.read())
    print(pages)

# df_list =[]
for i in range(pages):
    print(i)
    df = pd.read_csv('order\order_is_cash_3_%02d.csv' % i, encoding='gbk')
    if i == 0:
        df.to_csv('total\order_is_cash_3.csv', mode='a', encoding='gbk', index=False)
    else:
        df.to_csv('total\order_is_cash_3.csv', mode='a',encoding='gbk', index=False,header=0)
