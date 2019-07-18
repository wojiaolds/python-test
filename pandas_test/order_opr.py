import pandas as pd
import numpy as np
from multiprocessing import Pool
import os, time, random

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def convert_currency(var):
    """
    convert the string number to a float
    _ 去除$
    - 去除逗号，
    - 转化为浮点数类型
    """
    new_value = var.replace(",", "").replace("$", "")
    return float(new_value)


def fun(l):
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


def fun2(dic):
    day0_5 = 0
    amt0_5 = 0
    day5_10 = 0
    amt5_10 = 0
    day10_20 = 0
    amt10_20 = 0
    for key,value in dic.items():
        # print('------'*10)
        # print(key)
        # print(value)

        iKey = int(key)
        if 0 < iKey <= 5:
            day0_5 = day0_5 + value[0]
            amt0_5 = amt0_5 + value[1]
        elif 5 < iKey <= 10:
            day5_10 = day5_10 + value[0]
            amt5_10 = amt5_10 + value[1]
        elif 10 < iKey <= 20:
            day10_20 = day10_20 + value[0]
            amt10_20 = amt10_20 + value[1]
    return (day0_5,amt0_5,day5_10,amt5_10,day10_20,amt10_20)

def fun3(a,x,df,df_user):
    # print(a[0:10])
    # j = 0
    for i in a:
        df0 = df.loc[i].sort_index()
        # print(df0.index.get_level_values(2).values)
        l1 = np.array(df0.index.get_level_values(2).values)
        # print(l1)
        l1 = list(map(int, l1))
        l2 = (df0.loc[:, '日总金额'].values).tolist()
        # print(l2)
        l2 = list(map(float, l2))
        l = [l1, l2]
        # print(l)
        yz = fun2(fun(l))
        f = pd.DataFrame([[yz[0], yz[1], yz[2],yz[3],yz[4],yz[5]]], index=[i], columns=df_user.columns)
        # if j == 0:
        #     f.to_csv('order_%02d.csv'%x, mode='a', encoding='gbk', index=True)
        #     j = 1
        # else:
        f.to_csv('total\order_%02d.csv'%x, mode='a', encoding='gbk', index=True, header=0)

if __name__ == '__main__':
    # df = pd.DataFrame()
    # for day in range(1,32):
    #     df1 = pd.read_csv('order\order1805%02d.csv' % day,encoding='gbk')
    #     # print(df1.dtypes)
    #     # df1["pay_amt"].apply(convert_currency)
    #     df1["pay_amt"] = df1["pay_amt"].apply(pd.to_numeric, errors='coerce').fillna(0.0)
    #     # print(df1.dtypes)
    #     # df1.astype({'pay_amt': 'float64'})
    #     # print(df1.dtypes)
    #     s1 = df1.groupby(['user_account', 'create_year', 'create_month', 'create_day'])['user_account'].count()
    #     s2 = df1.groupby(['user_account', 'create_year', 'create_month', 'create_day'])['pay_amt'].sum()
    #
    #     df1 = pd.DataFrame(s1)
    #     df2 = pd.DataFrame(s2)
    #
    #     df3 = pd.merge(df1, df2, left_index=True, right_index=True)
    #     df3.rename(columns={'user_account': '日总笔数', 'pay_amt': '日总金额'}, inplace=True)
    #     # print(df3.head(10))
    #     # print(df3.dtypes)
    #     # df3[['日总笔数']] = df1[['日总笔数']].astype(int)
    #     # df3.astype({'日总金额': 'float64'})
    #
    #     # print(df1)
    #     if day == 1:
    #         df = df3
    #     else:
    #         df = df.add(df3, fill_value=0)
    #     print('第%d天'%day)
    #     print(df['日总笔数'].count())
    #     print(df['日总笔数'].sum())
    #     print(df['日总金额'].sum(), "元")
    #
    # df.to_csv('order180501.csv', encoding='gbk', index=True)

    df = pd.read_csv('order180501.csv', encoding='gbk')
    df.set_index(['user_account', 'create_year', 'create_month', 'create_day'],inplace=True)
    print(df.head(10))

    df_user = pd.DataFrame(columns=['连续0-5天交易次数','连续0-5天交易总金额','连续5-10天交易次数',
                                    '连续5-10天交易总金额','连续10-20天交易次数','连续10-20天交易总金额'])
    a = list(map(int, df.index.get_level_values(0).values))
    a = np.unique(a)

    # print(len(a))
    # print(a[0])

    num = 5000
    pages = (len(a)-1)//num+1
    #文件数记录下来
    with open('F:\\GitHub\\python\\python-test\\pandas_test\\total\\pages.txt', 'w') as f:
        f.write(str(pages))

    print('pages:',pages)
    p = Pool(15)
    for x in range(pages):
        start = x * num
        end = (x+1)*num
        p.apply_async(fun3, args=(a[start:end],x,df,df_user))

    p.close()
    p.join()
    print("end")








    # df_user.index.name = '用户'
    # old_user = ''
    # l = []
    # l1 = []
    # l2 = []
    # arr = []
    # start = 0
    # i = 0
    # for row_index,row in df.iterrows():
    #     s = row_index[3]
    #     amt = row[1]
    #     user = row_index[0]
    #
    #     if start == 0 or user == old_user: #同一个用户
    #         l1.append(int(s))
    #         l2.append(float(amt))
    #         start = 1
    #         pass
    #     else:
    #
    #         l.append(l1)
    #         l.append(l2)
    #         yz = fun2(fun(l))
    #         f = pd.DataFrame([[yz[0], yz[1], 0]], index=[old_user], columns=df_user.columns)
    #         if i == 0:
    #             f.to_csv('order1805.csv', mode='a', encoding='gbk', index=True)
    #             i = 1
    #         else:
    #             f.to_csv('order1805.csv', mode='a', encoding='gbk', index=True, header=0)
    #         df_user = df_user.append(f)
    #         l = []
    #         l1 = []
    #         l2 = []
    #         l1.append(int(s))
    #         l2.append(float(amt))
    #     old_user = user
    #
    # print(df_user)