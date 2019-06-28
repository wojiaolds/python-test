import pandas as pd
import numpy as np


df = pd.DataFrame()
print(df)
print('-----'*10)
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)
print('-----'*10)
data = [['Alex',None],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
print('-----'*10)
print(df.info())
print('-----'*10)
print(df.shape)
print('-----'*10)
print(df.shape[0])
print('-----'*10)
df1=df.dropna()
print(df1)


print('-----'*10)
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)
print(df.dtypes)

print('-----'*10)
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)

print('-----'*10)
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

print('-----'*10)
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
print(df.dtypes)

print('-----'*10)
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print(df)

print('-----'*10)
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
# With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)

print('-----'*10)
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

print('-----'*10)
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df['one'])
print(df.iloc[0])
print(df.loc['a'])

#增加列
print('-----'*10)
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
# Adding a new column to an existing DataFrame object with column label by passing new series
print("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
print("Adding a new column using the existing columns in DataFrame:")
df['four'] = df['one']+df['three']
print(df)


#删除列
print('-----'*10)
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([10,20,30], index=['a','b','c'])}
df = pd.DataFrame(d)
print("Our dataframe is:")
print(df)
# using del function
print("Deleting the first column using DEL function:")
del df['one']
print(df)
# using pop function
print("Deleting another column using POP function:")
df.pop('two')
print(df)


print('-----'*10)
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
print(df.loc['b'])


print('-----'*10)
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
print(df.iloc[2])

print('-----'*10)
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df[2:4])  # 行切片

#附加行
print('-----'*10)
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a','b'])
df3 = pd.DataFrame([['r',4]],columns=['a','b'])
df = df.append(df2)
df = df.append(df3)
print(df)

#删除行
print('-----'*10)
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a','b'])
df = df.append(df2)
# Drop rows with label 0
print(df)
df = df.drop(0)
print(df)

print('-----'*10)
df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
print(df)
# for getting values with a boolean array
print(df.loc['a'])
print (df.loc['a']>0)

print('-----'*10)
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print(df)
print (df[['A','B']])
print (df[2:3])
print(df.A)



































