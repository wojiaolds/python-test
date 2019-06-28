import pandas as pd
import numpy as np

a = []
b = []
data = {}
for i in range(0, 10):
    a.append(i)
    b.append(i)
print(a)
print(b)
data['a_name'] = a
data['b_name'] = b
print(data)
df = pd.DataFrame(data)
print(df.dtypes)
df['a_name'] = df['a_name'].astype('float64')
print(df.dtypes)
df.to_csv(path_or_buf='text4.csv', sep=',', na_rep='NA', float_format='%.2f'
         ,index = False)
# headers = False(不保存列名)
# index = False(不保存索引)
