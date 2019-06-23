import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)


dates = pd.date_range('2017-01-02', periods=7)
print(type(dates))
print(dates)

print("--"*16)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df)
print("--------------" * 10)
print(df.head())
print("--------------" * 10)
print(df.tail(3))

print("index is :" )
print(df.index)
print("columns is :" )
print(df.columns)
print("values is :" )
print(type(df.values))
print(df.values)
print("--------------" * 10)
print(df.T)


df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20170102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

print(df2)
print(df2.dtypes)


dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.sort_values(by='B'))
print('-----'*10)
print(type(df['A']))
print(df['A'])  # print(df.A)
print('-----'*10)
print(df[0:3])
print("========= 指定选择日期 ========")
print(df['20170102':'20170103'])

'''
按标签选择
'''
print('-----'*10)
print(dates[0])
print(df.loc[dates[0]])
print('-----'*10)
print(df.iloc[0])
print('-----'*10)
print(df.loc[:,['A','B']])
print('-----'*10)
print(type(df.loc['20170102':'20170104',['A','B']]))
print(df.loc['20170102':'20170104',['A','B']])
print('-----'*10)
print(type(df.loc['20170102',['A','B']]))
print(df.loc['20170102',['A','B']])
print('-----'*10)
print(df.loc[dates[0],'A'])
print('-----'*10)
print(df.at[dates[0],'A'])

'''
通过位置选择
'''
print('-----'*10)
print(df.iloc[3])
print('-----'*10)
print(df.iloc[3:5,0:2])
print('-----'*10)
print(df.iloc[[1,2,4],[0,2]])
print('-----'*10)
print(df.iloc[1,1])

'''
布尔索引
'''
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
print('-----'*10)
print(df[df.A > 0])
print('-----'*10)
print(df[df > 0])
print('-----'*10)
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']  # 增加一列
print(df2)
print("============= start to filter =============== ")
print(df2[df2['E'].isin(['two', 'four'])])
print('-----'*10)
print(df2.dtypes)
print('-----'*10)
print(df2.iloc[0].index)

































