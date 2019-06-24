import pandas as pd
import numpy as np

s = pd.Series()
print(s)  # 空系列

print('----'*10)
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)

print('----'*10)
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)

print('----'*10)
df = pd.DataFrame(s.values,index=s.index,columns=['ab'])
print(df)

print('----'*10)
data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)

print('----'*10)
data = {'a': 0., 'b': 1., 'c': 2.}
# 如果传递了索引，索引中与标签对应的数据中的值将被拉出
s = pd.Series(data, index=['b', 'c', 'd'])
print(s)


'''
从标量创建一个系列
如果数据是标量值，则必须提供索引。将重复该值以匹配索引的长度。
'''
print('----'*10)
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

print('----'*10)
s = pd.Series([1,2,3,4,5],index=['a', 'b', 'c', 'd', 'e'])
print(s)
# retrieve the first element
print(s[0])

print('----'*10)
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve multiple elements
print(s[['a', 'c', 'd']])
print(s.loc['a'])

s = pd.Series(['tom ', ' William Rick', 'john', 'Aelber@t'])
print (s.str.findall('e'))
print(s.str.islower())
print (s.str.swapcase())























