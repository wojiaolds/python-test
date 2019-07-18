import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pages = 0
with open('F:\\GitHub\\python\\python-test\\pandas_test\\total\\pages.txt', 'r') as f:
    pages = int(f.read())
    print(pages)

df_list =[]
for i in range(pages):
    df = pd.read_csv('total\order_%02d.csv' % i,encoding='gbk',header=None)
    df_list.append(df)
w = pd.concat(df_list)
w.columns=['用户','连续0-5天交易次数','连续0-5天交易总金额','连续5-10天交易次数',
            '连续5-10天交易总金额','连续10-20天交易次数','连续10-20天交易总金额']
w.to_csv('total\order.csv', encoding='gbk', index=False)
print(w.loc[w['连续0-5天交易次数']>4,['用户','连续0-5天交易次数','连续0-5天交易总金额']])