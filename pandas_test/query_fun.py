import pandas as pd
from sqlalchemy import create_engine
from multiprocessing import Pool
import os, time, random




dic_month = {'1':31,'2':29,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}


class Query(object):

    def __init__(self,engine):
        self.engine = engine
    def count_day(self,day):
        sql = '''
            select count(*) FROM alidata.ali_order_1805 a
            INNER JOIN alidata.buyer_information_phone b 
            ON a.user_account = b.user_account
            where a.create_day = %d
            '''%(day)
        # print(sql)
        df = pd.read_sql_query(sql, self.engine)
        return df.iloc[0,0]
    def select_day(self,day):
        cnt = self.count_day(day)
        page_num = 5000
        pages = (cnt-1)//page_num+1

        for x in range(pages):
            # 查询语句，选出employee表中的所有数据
            # print("第%d页" % x)
            start = x * page_num
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
              WHEN  20 THEN 1
              ELSE 0
              END as category
              FROM alidata.ali_order_1805 a
              INNER JOIN alidata.buyer_information_phone b
              ON a.user_account = b.user_account 
              where a.create_day = %d 
              limit %d,%d ''' % \
                  (day,start, page_num)
            df1 = pd.read_sql_query(sql, self.engine)
            # df1['create_time'] = df1['create_time'] + '\t'
            # df1['user_account'] = df1['user_account'] + '\t'
            # df1['cust_id'] = df1['cust_id'] + '\t'
            # df1['agent_id'] = df1['agent_id'] + '\t'
            df1.to_csv('order\order1805%02d.csv'%day, mode='a', encoding='gbk', index=False)


def select(d):
    print('开始下载第%d天的数据'%d)
    engine = create_engine('mysql+mysqlconnector://test:yzkj@2019!#$^@192.168.10.131:3306/alidata')
    query = Query(engine)
    start = time.time()
    query.select_day(d)
    end = time.time()
    print('下载第%d天的数据 耗时%0.2f seconds.' % (d, (end - start)))

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    # pd.set_option('display.max_rows', 500)
    # pd.set_option('display.max_columns', 500)
    # pd.set_option('display.width', 1000)
    # 初始化数据库连接，使用pymysql模块
    # MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
    try:

        p = Pool(15)
        month = 5
        days = dic_month[str(month)]
        for day in range(1, days + 1):
            p.apply_async(select, args=(day,))
            # p.apply_async(long_time_task, args=(day,))
        p.close()
        p.join()
    except BaseException as ex:
        print(ex)

    print("end")
