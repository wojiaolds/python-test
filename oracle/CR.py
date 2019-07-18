import pandas as pd
from sqlalchemy import create_engine
from multiprocessing import Pool
import os, time, random


engine = create_engine("oracle://posp:Dyf_pOsp@192.168.10.109:1521/dyfdb1",encoding='utf-8', echo=True)

def fun(df,start,end,x):
    df1 = pd.DataFrame()
    for i in range(start,end):
        pan = df.loc[i, '银行卡号']
        sql = '''select mcht_cd,pan from tbl_algo_dtl_his t where pan ='%s'
        ''' % (pan)
        print(sql)
        df_tmp = pd.read_sql_query(sql, engine)
        if i == 0:
            df1 = df_tmp;
        else:
            df1 = df1.append(df_tmp)
    df1.to_excel('CR\CR_%02d.xlsx' % x, encoding='gbk', index=False)

if __name__ == '__main__':
    df = pd.read_csv('CR.csv')
    print(df.shape[0])
    cnt = df.shape[0]
    page_num = 500
    pages = (cnt - 1) // page_num + 1
    # 文件数记录下来
    with open('F:\\GitHub\\python\\python-test\\oracle\\CR\\cnt.txt', 'w') as f:
        f.write(str(pages))

    p = Pool(20)
    for x in range(pages):

        start = x*page_num
        end = (x+1)*page_num

        p.apply_async(fun, args=(df,start,end,x))
    p.close()
    p.join()
