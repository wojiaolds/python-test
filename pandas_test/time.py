import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def fun_time(start_h,end_h):
    df = pd.DataFrame()
    for day in range(1, 32):
        df1 = pd.read_csv('order\order1805%02d.csv' % day, encoding='gbk')
        # print(df1.dtypes)
        # df1["pay_amt"].apply(convert_currency)
        df1["pay_amt"] = df1["pay_amt"].apply(pd.to_numeric, errors='coerce').fillna(0.0)
        # print(df1.dtypes)
        # df1["create_time"] = df1["create_time"].apply(pd.to_, errors='coerce').fillna(0.0)
        # print(df1.dtypes)
        # s1 = df1.groupby(['user_account', 'create_year', 'create_month', 'create_day'])['user_account'].count()
        # s2 = df1.groupby(['user_account', 'create_year', 'create_month', 'create_day'])['pay_amt'].sum()
        df1['H'] = df1['create_time'].str.slice(11, 13)
        # print(df1.dtypes)
        # print('----'*10)
        # print(df1.loc[df1["H"] == '',:])
        # print('----' * 10)
        df1 = df1.loc[df1["H"] != '', :]
        df1["H"] = df1.H.map(lambda x: int(x))

        # print(df1.dtypes)
        # print(df1.head(10))

        bool_index = df1['H'].apply(lambda x: x in range(start_h, end_h))

        # print(bool_index)
        s1 = df1.loc[bool_index].groupby('user_account')['user_account'].count()
        s2 = df1.loc[bool_index].groupby('user_account')['pay_amt'].sum()

        df3 = pd.merge(s1, s2, left_index=True, right_index=True)
        df3.rename(columns={'user_account': '%02d:00-%02d:00交易笔数' % (start_h, end_h),
                            'pay_amt': '%02d:00-%02d:00交易金额' % (start_h, end_h)}, inplace=True)
        if day == 1:
            df = df3
        else:
            df = df.add(df3, fill_value=0)

    return df

if __name__ == '__main__':
    # start_h = 0
    # end_h = 6

    # datetime = '2018-05-01 01:10:33'
    # h = datetime[11:13]
    # print(int(h))
    #
    # print(list(range(start_h, end_h)))
    # print(int(h) in range(start_h, end_h))
    df1 = fun_time(0, 6)
    df2 = fun_time(6, 12)

    df1 = pd.merge(df1, df2, left_index=True, right_index=True,how='outer')
    df2 = fun_time(12, 18)

    df1 = pd.merge(df1, df2, left_index=True, right_index=True,how='outer')
    df2 = fun_time(18, 24)

    df1 = pd.merge(df1, df2, left_index=True, right_index=True,how='outer')
    df1 = df1.fillna(0.0)
    print(df1.head(20))
    # df1.astype({'00:00-06:00交易笔数': 'int','06:00-12:00交易笔数': 'int','12:00-18:00交易笔数': 'int','18:00-24:00交易笔数': 'int'})
    df1['00:00-06:00交易笔数'] = df1['00:00-06:00交易笔数'].astype(int)
    df1['06:00-12:00交易笔数'] = df1['06:00-12:00交易笔数'].astype(int)
    df1['12:00-18:00交易笔数'] = df1['12:00-18:00交易笔数'].astype(int)
    df1['18:00-24:00交易笔数'] = df1['18:00-24:00交易笔数'].astype(int)
    print(df1)
    print(df1.shape)
    df1.to_csv('total\order_time.csv', encoding='gbk', index=True)






