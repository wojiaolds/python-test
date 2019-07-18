import pandas as pd
import numpy as np



d =pd.DataFrame([[1,2,3,np.nan]])
print(d.columns)
print(d)
d = d.fillna(5.0)
print(d)
print(d.dtypes)
d[3] = d[3].astype(int)
print(d.dtypes)
print(d)
print('----'*10)





# sb = pd.Series([3,6])
# print(sb)  # 空系列
#
# print('----'*10)
# data = np.array([2, 3, 4, 5])
# s = pd.Series(data)
# print(s)
# print( sb.add(s,  fill_value=0))
#
# print('----'*10)
# data = np.array(['a','b','c','d'])
# s = pd.Series(data,index=[100,101,102,103])
# print(s)
#
# print('----'*10)
# df = pd.DataFrame(s.values,index=s.index,columns=['ab'])

l = [[1, 2, 3, 5, 9,10,12,13,16,18,19,20,21,22,23],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
def fun(l):
    arr = []
    d = {}
    old = 0
    cnt = 0
    amt_sum = 0
    it = iter(l[1])
    for i in l[0]:
        if old != 0 and i != old + 1:

            if str(cnt) in d.keys():
                d[str(cnt)] = [d[str(cnt)][0] + 1,d[str(cnt)][1]+amt_sum]
            else:
                d[str(cnt)] = [1,amt_sum]

            cnt = 1
            amt_sum = next(it)
        else:
            amt_sum = next(it)+amt_sum
            cnt = cnt + 1
        old = i

    if str(cnt) in d.keys():
        d[str(cnt)] = [d[str(cnt)][0] + 1,d[str(cnt)][1]+amt_sum]
    else:
        d[str(cnt)] = [1,amt_sum]

    return d
print(fun(l))
dic = fun(l)
def fun2(dic):
    day0_5 = 0
    amt0_5 = 0
    for key,value in dic.items():
        # print('------'*10)
        # print(key)
        # print(value)

        iKey = int(key)
        if 0 < iKey <= 5:
            day0_5 = day0_5 + value[0]
            amt0_5 = amt0_5 + value[1]
    return (day0_5,amt0_5)

print(fun2(fun(l)))

ll = [2,4,9,5,3]

ll.sort()

print(ll)


df=pd.DataFrame({'idx1':[0,0,1,1,2], 'idx2':(5,5,5,5,5),'idx3':(2,1,3,4,4), 'value':np.random.randn(5)})
df.set_index(keys=['idx1','idx2','idx3'], inplace=True)
print(df)
df["idx1_mod"] = df.index.get_level_values(0).values + 100
print(df)
print(type(df.index.get_level_values(0).values))
print(df.index.get_level_values(0).values)
a = np.unique(df.index.get_level_values(0).values)
print(df.index.get_level_values(0).values)
print(a)
print(type(a))
# for i in df.index.get_level_values(0).values:
#     print(i)
print(df.index)
print(df.index.dtype)
print(df.loc[0])
df0 = df.loc[0]
print(type(df0))
df1 = df0.sort_index()
# df.sort_index(inplace=True)
print(df1)
print(df.loc[0].index.get_level_values(1).values)
print(df.loc[0].loc[:,'value'].values)
print(type(df.loc[0].loc[:,'value'].values))
print(np.array(df.loc[0].loc[:,'value'].values))
print((df.loc[0].loc[:,'value'].values).tolist())

