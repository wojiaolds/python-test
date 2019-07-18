import pandas as pd
import numpy as np
from multiprocessing import Pool
import os, time, random

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('precision', 2)
np.set_printoptions(suppress=True)
'''
20160601为截止日期算起
'''
df = pd.read_csv('total\order_is_cash_3.csv', encoding='gbk',low_memory=False)
df['DATE_SETTLMT'] = df['DATE_SETTLMT'].astype(object)
# df['TRANS_DATE_TIME'] = df['TRANS_DATE_TIME'].astype(object)
df['MONTH'] = df['DATE_SETTLMT'].map(lambda x: str(x)[0:6]).astype("int64")

df['TRANS_DATE_TIME'] = df['TRANS_DATE_TIME'].map(lambda x:"%06d"%x)
df['HOUR'] = df['TRANS_DATE_TIME'].map(lambda x: str(x)[:-4]).astype("int64")
# print(df.dtypes)
# print(df.head())
df = df.loc[df["PAN"] != 0, :]
df["PAN"] = df["PAN"].astype(object)
# print(df.head())
# print(df['MONTH'])
bool_index = ((df['MONTH'] > 201505) & (df['MONTH'] < 201606))
# print(bool_index)
df = df.loc[bool_index,:]
# print(df)
# print(df.shape)
#
# print(df.dtypes)
# s1 = df.groupby(['mcht_cd'])['mcht_cd'].count()
# s2 = df.groupby(['mcht_cd'])['trans_amt'].sum()

# df1 = pd.DataFrame(s1)
# df2 = pd.DataFrame(s2)

# df3 = pd.merge(s1, s2, left_index=True, right_index=True)
df3 = df.groupby(['MCHT_CD']).agg({'MCHT_CD':'count','TRANS_AMT':'sum'})
df3.rename(columns={'MCHT_CD': '总笔数', 'TRANS_AMT': '总金额'}, inplace=True)
df3['客单价'] = round(df3['总金额'].div(df3['总笔数']),0)
print(df3.head())
# print(df3.index)
print('------'*10)
s4 = df.groupby(['MCHT_CD','PAN'])['MCHT_CD'].count()
# print(type(s4))
df4 = pd.DataFrame(s4)
print('------'*10)
#统计用户数
df5 = df4.groupby(level=['MCHT_CD'],axis=0).count()
df5.rename(columns={'MCHT_CD': '用户数'}, inplace=True)
print('------'*10)
# print(df4.head(20))
# print(df4.index)
# a = np.unique(df4.index.get_level_values(0).values)
# a= list(a)
# print(a)
# print(len(a))
# print('------'*10)
# df_list =[]
# for i in a:
#     v = df4.loc[i].index.get_level_values(0).values
#     f = pd.DataFrame([[len(v)]], index=[i], columns=['用户数'])
#     df_list.append(f)
# w = pd.concat(df_list)

# df5 = pd.merge(df3, w, left_index=True, right_index=True)

df_result = pd.merge(df3, df5, left_index=True, right_index=True)
df_result['总笔数/用户数'] = round(df_result['总笔数'].div(df_result['用户数']),2)
df_result['总金额/用户数'] = round(df_result['总金额'].div(df_result['用户数']),0)
# df_result['总金额/用户数'] = df_result['总金额/用户数'].astype(np.float64)

#统计商户近12月有交易的月数
print('------'*10)
s4 = df.groupby(['MCHT_CD','MONTH'])['MCHT_CD'].count()
# print(type(s4))
df4 = pd.DataFrame(s4)
print(df4.head())
df_tmp = df4.groupby(level=['MCHT_CD'],axis=0).count()
df_tmp.rename(columns={'MCHT_CD': '近12月有交易的月数'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head())
print('------'*10)

#近1月交易天数
bool_index = ((df['MONTH'] >= 201605) & (df['MONTH'] < 201606))
# print(bool_index)
df1 = df.loc[bool_index,:]
print(df1.head())
s4 = df1.groupby(['MCHT_CD','DATE_SETTLMT'])['MCHT_CD'].count()
# print(type(s4))
df4 = pd.DataFrame(s4)
print(df4.head())

df_tmp = df4.groupby(level=['MCHT_CD'],axis=0).count()
df_tmp.rename(columns={'MCHT_CD': '近1月交易天数'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))

#近3月交易天数
bool_index = ((df['MONTH'] >= 201603) & (df['MONTH'] < 201606))
# print(bool_index)
df1 = df.loc[bool_index,:]
print(df1.head())
s4 = df1.groupby(['MCHT_CD','DATE_SETTLMT'])['MCHT_CD'].count()
# print(type(s4))
df4 = pd.DataFrame(s4)
print(df4.head())

df_tmp = df4.groupby(level=['MCHT_CD'],axis=0).count()
df_tmp.rename(columns={'MCHT_CD': '近3月交易天数'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))

#近6月交易天数
bool_index = ((df['MONTH'] >= 201512) & (df['MONTH'] < 201606))
# print(bool_index)
df1 = df.loc[bool_index,:]
print(df1.head())
s4 = df1.groupby(['MCHT_CD','DATE_SETTLMT'])['MCHT_CD'].count()
# print(type(s4))
df4 = pd.DataFrame(s4)
print(df4.head())

df_tmp = df4.groupby(level=['MCHT_CD'],axis=0).count()
df_tmp.rename(columns={'MCHT_CD': '近6月交易天数'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))


#近12月交易天数
s4 = df.groupby(['MCHT_CD','DATE_SETTLMT'])['MCHT_CD'].count()
# print(type(s4))
df4 = pd.DataFrame(s4)
print(df4.head())

df_tmp = df4.groupby(level=['MCHT_CD'],axis=0).count()
df_tmp.rename(columns={'MCHT_CD': '近12月交易天数'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))

print('------'*10)
#近1月交易总金额
bool_index = ((df['MONTH'] >= 201605) & (df['MONTH'] < 201606))
df1 = df.loc[bool_index,:]
# print(df1.head())
df_tmp = df1.groupby(['MCHT_CD']).agg({'MCHT_CD':'count','TRANS_AMT':'sum'})
df_tmp.rename(columns={'MCHT_CD':'近1月交易笔数','TRANS_AMT': '近1月交易总金额'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))

print('------'*10)
#近3月交易总金额
bool_index = ((df['MONTH'] >= 201603) & (df['MONTH'] < 201606))
df1 = df.loc[bool_index,:]
# print(df1.head())
df_tmp = df1.groupby(['MCHT_CD']).agg({'MCHT_CD':'count','TRANS_AMT':'sum'})
df_tmp.rename(columns={'MCHT_CD':'近3月交易笔数','TRANS_AMT': '近3月交易总金额'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))

print('------'*10)
#近6月交易总金额
bool_index = ((df['MONTH'] >= 201512) & (df['MONTH'] < 201606))
df1 = df.loc[bool_index,:]
# print(df1.head())
df_tmp = df1.groupby(['MCHT_CD']).agg({'MCHT_CD':'count','TRANS_AMT':'sum'})
df_tmp.rename(columns={'MCHT_CD':'近6月交易笔数','TRANS_AMT': '近6月交易总金额'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))

print('------'*10)
#近12月交易总金额
df_tmp = df.groupby(['MCHT_CD']).agg({'MCHT_CD':'count','TRANS_AMT':'sum'})
df_tmp.rename(columns={'MCHT_CD':'近12月交易笔数','TRANS_AMT': '近12月交易总金额'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))


print('------'*10)
#近1月22:00~04:00的交易总金额
print(df.dtypes)
bool_index = ((df['MONTH'] >= 201605) & (df['MONTH'] < 201606) & ((df['HOUR'] >=22) | (df['HOUR'] <4)))
df1 = df.loc[bool_index,:]
# print(df1)
df_tmp = df1.groupby(['MCHT_CD']).agg({'MCHT_CD':'count','TRANS_AMT':'sum'})
df_tmp.rename(columns={'MCHT_CD':'近1月22:00~04:00的交易总笔数','TRANS_AMT': '近1月22:00~04:00的交易总金额'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))

print('------'*10)
#近3月22:00~04:00的交易总金额
print(df.dtypes)
bool_index = ((df['MONTH'] >= 201603) & (df['MONTH'] < 201606) & ((df['HOUR'] >=22) | (df['HOUR'] <4)))
df1 = df.loc[bool_index,:]
# print(df1)
df_tmp = df1.groupby(['MCHT_CD']).agg({'MCHT_CD':'count','TRANS_AMT':'sum'})
df_tmp.rename(columns={'MCHT_CD':'近3月22:00~04:00的交易总笔数','TRANS_AMT': '近3月22:00~04:00的交易总金额'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))

print('------'*10)
#近6月22:00~04:00的交易总金额
print(df.dtypes)
bool_index = ((df['MONTH'] >= 201512) & (df['MONTH'] < 201606) & ((df['HOUR'] >=22) | (df['HOUR'] <4)))
df1 = df.loc[bool_index,:]
# print(df1)
df_tmp = df1.groupby(['MCHT_CD']).agg({'MCHT_CD':'count','TRANS_AMT':'sum'})
df_tmp.rename(columns={'MCHT_CD':'近6月22:00~04:00的交易总笔数','TRANS_AMT': '近6月22:00~04:00的交易总金额'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))

print('------'*10)
#近12月22:00~04:00的交易总金额
print(df.dtypes)
bool_index = ((df['HOUR'] >=22) | (df['HOUR'] <4))
df1 = df.loc[bool_index,:]
# print(df1)
df_tmp = df1.groupby(['MCHT_CD']).agg({'MCHT_CD':'count','TRANS_AMT':'sum'})
df_tmp.rename(columns={'MCHT_CD':'近12月22:00~04:00的交易总笔数','TRANS_AMT': '近12月22:00~04:00的交易总金额'}, inplace=True)
print(df_tmp.head())

df_result = pd.merge(df_result, df_tmp, left_index=True, right_index=True)
print(df_result.head(20))












df_result['商户号'] = df_result.index
df_result['商户号'] = df_result['商户号'].astype(object)
# df5['商户号'] = df5['商户号'] + '\t'
df_result = df_result.set_index('商户号')
df_result.sort_values(by = '总笔数',inplace = True,ascending=False)
# print(df_result)

# print(df_result.dtypes)
# print(df_result.shape[0])
# print(df_result.mean())
print('-----'*10)
print(df_result.index)
df6 = pd.DataFrame([df_result.mean().values.tolist()],index = [df_result.shape[0]],columns=df_result.columns)
# df6 = df6.reindex(df6.index.rename(['商户号']))
# df6.index.names = ['商户号']
df_result = df_result.append(df6)
print(df_result)
df_result['总金额'] = round(df_result['总金额']/100,2)
df_result['客单价'] = round(df_result['客单价']/100,2)
df_result['总金额/用户数'] = round(df_result['总金额/用户数']/100,2)

df_result['近1月交易总金额'] = round(df_result['近1月交易总金额']/100,2)
df_result['近3月交易总金额'] = round(df_result['近3月交易总金额']/100,2)
df_result['近6月交易总金额'] = round(df_result['近6月交易总金额']/100,2)
df_result['近12月交易总金额'] = round(df_result['近12月交易总金额']/100,2)

df_result['近1月22:00~04:00的交易总金额'] = round(df_result['近1月22:00~04:00的交易总金额']/100,2)
df_result['近3月22:00~04:00的交易总金额'] = round(df_result['近3月22:00~04:00的交易总金额']/100,2)
df_result['近6月22:00~04:00的交易总金额'] = round(df_result['近6月22:00~04:00的交易总金额']/100,2)
df_result['近12月22:00~04:00的交易总金额'] = round(df_result['近12月22:00~04:00的交易总金额']/100,2)


df_result = df_result.reset_index()
# print(df_result.index)
df_result.rename(columns={'index': '商户号'}, inplace=True)
# print(df_result.head())

df_result['商户号'] = df_result['商户号'].astype(object)
df_result['商户号'] = [' %i' % i for i in df_result['商户号']]

df_result.to_excel('total\order_is_cash_3_hz.xlsx', encoding='gbk', index=False)

#
#
