import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pylab import mpl
#mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

df1=pd.read_excel('order_is_cash_2_hz_new.xlsx')

df2=pd.read_excel('order_is_cash_3_hz_new.xlsx')

df_train = df1.append(df2)
print('打印样本数据')

#使用python自动分箱woe转化
# bins1=[-1,0,3,8,12]
# cut1=pd.cut(df_train["近12月有交易的月数"],4,labels=False)
# print(type(cut1))
# print(cut1.index)
# # print(cut1.name)
# print(len(cut1))
# print(cut1[0])
# print('----'*10)
# print(cut1[1])
# print(type(cut1[1]))
# # print(cut1[2])
# l =  cut1[1].tolist()
# print(l)
# print(pd.value_counts(cut1))
# cut=pd.qcut(df_train["近12月有交易的月数"],4,labels=False)
# print(pd.value_counts(cut))

bins1=[0,0.1,0.3,0.7,1.0]
cut10=pd.qcut(df_train["近12月有交易的月数"],bins1,labels=False,retbins=True,duplicates='drop')
cut1=pd.qcut(df_train["近12月有交易的月数"],bins1,labels=False,duplicates='drop')
bins1=cut10[1].tolist()

print(bins1)
print(pd.value_counts(cut1))
