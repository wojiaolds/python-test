import pandas as pd
import numpy as np
from multiprocessing import Pool
import os, time, random

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pages = 0
with open('F:\\GitHub\\python\\python-test\\oracle\\CR\\cnt.txt', 'r') as f:
    pages = int(f.read())
    print(pages)

for i in range(pages):
    print(i)
    df = pd.read_excel('CR\CR_%02d.xlsx' % i, encoding='gbk')
    if i == 0:
        df.to_csv('CR\CR_T.csv', mode='a', encoding='gbk', index=False)
    else:
        df.to_csv('CR\CR_T.csv', mode='a',encoding='gbk', index=False,header=0)


