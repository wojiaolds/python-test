import pandas as pd
import sys
from sqlalchemy import create_engine
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
engine = create_engine('mysql+mysqlconnector://test:yzkj@2019!#$^@192.168.10.131:3306/alidata')
df = pd.DataFrame();
# print(df)
page_num = 5000
for x in range(1):
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
    df1['create_time'] = df1['create_time'] + '\t'
    df1['user_account'] = df1['user_account'] + '\t'
    df1['cust_id'] = df1['cust_id']+'\t'
    df1['agent_id'] = df1['agent_id'] + '\t'
    print(df1)
    df1.to_csv('order1805.csv', mode='a', encoding='gbk',index=False)