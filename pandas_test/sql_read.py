import pandas as pd
import sys
from sqlalchemy import create_engine

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
    for key,value in dic.items():
        # print('------'*10)
        # print(key)
        # print(value)

        iKey = int(key)
        if 0 < iKey <= 5:
            day0_5 = day0_5 + value[0]
            amt0_5 = amt0_5 + value[1]
    return (day0_5,amt0_5)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# df = pd.DataFrame()
# print(df)
# df1 = pd.DataFrame({'a':[4,2,5],'b':[3,5,8]},index=['c','d','e'])
# print(df1)
# df2 = df.add(df1,  fill_value=0)
# print(df2)


# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
engine = create_engine('mysql+mysqlconnector://test:yzkj@2019!#$^@192.168.10.131:3306/alidata')
df = pd.DataFrame();
# print(df)
page_num = 10000
for x in range(2):
    # 查询语句，选出employee表中的所有数据
    print("第%d页"%x)
    start = x*page_num
    sql = '''SELECT
      a.create_time,
      a.pay_amt,
      a.user_account,
      a.create_year,
      a.create_month,
      a.create_day,
      b.province_location as province,
      b.city_location as city ,
      b.cust_id,
      b.cust_name,
      b.agent_id,
      b.agent_name,
      CASE  b.category
      WHEN b.category = 20 THEN 1
      ELSE 0
      END as category
      FROM alidata.ali_order_1805 a
      INNER JOIN alidata.buyer_information_phone b
      ON a.user_account = b.user_account limit %d,%d ''' % \
      (start,page_num)
    # print(sql)
    # read_sql_query的两个参数: sql语句， 数据库连接
    df1 = pd.read_sql_query(sql, engine)
    # 输出employee表的查询结果
    s1 = df1.groupby(['user_account', 'create_year', 'create_month', 'create_day'])['user_account'].count()
    s2 = df1.groupby(['user_account', 'create_year', 'create_month', 'create_day'])['pay_amt'].sum()

    df1 = pd.DataFrame(s1)
    df2 = pd.DataFrame(s2)

    df3 = pd.merge(df1, df2, left_index=True, right_index=True)
    df3.rename(columns={'user_account': '日总笔数', 'pay_amt': '日总金额'}, inplace=True)
    # print(df1)
    if x == 0:
        df =df3
    else:
        df = df.add(df3,  fill_value=0)
    print(df['日总笔数'].count())
    print(df['日总金额'].sum()/100,"元")


    # print(df.shape)
    # print(df.index)
print(df)
print(sys.getsizeof(df)/(1024*1024),"Mb")

# print(df.index)
# print(type(df.index))
# print(df.index)
#
# print(df.index.get_level_values(0))
# print(df.index.get_level_values(1))
# print(df.index.get_level_values(2))
# print(df.index.get_level_values(3))
# print(df.index[0])

df_user = pd.DataFrame(columns=['连续0-5天交易次数','连续0-5天交易总金额','连续5-10天交易次数'])
df_user.index.name = '用户'
# print(df.shape[0])
# for i in range(20):
#     for data in df.iloc[i]:
#         print(data)
# day0_5 = 0
# amt0_5 = 0
# days = 0 # 连续次数
# old_day = 0
old_user = ''
# amt = 0
l = []
l1 = []
l2 = []
arr = []
start = 0
for row_index,row in df.iterrows():
    s = row_index[3]
    amt = row[1]
    user = row_index[0]

    if start == 0 or user == old_user: #同一个用户
        l1.append(int(s))
        l2.append(float(amt))
        start = 1
        pass
    else:
        l.append(l1)
        l.append(l2)
        yz = fun2(fun(l))
        f = pd.DataFrame([[yz[0], yz[1], 0]], index=[old_user], columns=df_user.columns)
        df_user = df_user.append(f)
        l = []
        l1 = []
        l2 = []
        l1.append(int(s))
        l2.append(float(amt))
    old_user = user

    # s = row_index[3]
    # user = row_index[0]
    #
    # if  user == old_user: #同一个用户
    #     if int(old_day) == 0 or int(s) == int(old_day)+1:
    #         days = days + 1
    #         amt = amt + row[1]
    #     else:
    #         if days > 0 and days <= 5:
    #             day0_5 = day0_5 + 1
    #             amt0_5 = amt0_5 + amt
    #
    #         amt = row[1]
    #         days = 1  # 连续次数
    #
    # else:
    #     if days > 0 and days <= 5:
    #         day0_5 = day0_5 + 1
    #         amt0_5 = amt0_5 + amt
    #     if (old_user != ''):
    #         f = pd.DataFrame([[day0_5, amt0_5, 0]], index=[old_user], columns=df_user.columns)
    #         df_user = df_user.append(f)
    #         pass
    #
    #     day0_5 = 0
    #     amt0_5 = 0
    #     days = 1
    #     amt = row[1]
    #     old_user = user
    #
    # old_day = s

    # print (row_index,'\n',row)
print(df_user)

# for index in df.index:
#     print(index.level)
#     print(index.name)

# 新建pandas中的DataFrame, 只有id,num两列
# df = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['zhangsan', 'lisi', 'wangwu', 'zhuliu']})
# # 将新建的DataFrame储存为MySQL中的数据表，储存index列
# print(df)
# df.to_sql('mydf', engine, index=True,if_exists='append')
# print('Read from and write to Mysql table successfully!')
