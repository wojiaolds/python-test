import pandas as pd
from sqlalchemy import create_engine
from multiprocessing import Pool
import os, time, random

# engine = create_engine("oracle://posp:Dyf_pOsp@192.168.10.109:1521/dyfdb1",encoding='utf-8', echo=True)
engine = create_engine('mysql+mysqlconnector://test:yzkj@2019!#$^@192.168.10.131:3306/posp')
def query_cnt():
    sql = '''
        select count(*) from tbl_algo_dtl_his_fx where is_cash = 2;
        '''
    df = pd.read_sql_query(sql, engine)
    cnt = df.iloc[0, 0]
    return cnt

def query_page(page_num,x):
    print("开始下载第%d页" % (x+1))

    # sql = '''
    #     #         select * from (select ROWNUM AS rowno, DATE_SETTLMT,TRANS_DATE_TIME,PAN,TRANS_AMT,SETTL_AMT,
    #     #         t.AGENT_NO,MCHT_CD,t.MCHT_NAME,IPS_NO,MCHT_AT_C,MCHT_FEE_C,ACQ_INS_FEE_C,ACQ_INS_ALLOT_C,CUPS_FEE_C
    #     #         ,FEE_C_OUT,INS_MCC_CODE from tbl_algo_dtl_his a
    #     #         left join AGENT.TBL_MCHT_INF t on a.mcht_cd = t.mcht_no where t.reserve5 ='1' and rownum <= %d) r
    #     #         where r.rowno >=%d
    #     #         '''%(end,start)

    sql = '''
        select DATE_SETTLMT,TRANS_DATE_TIME,PAN,TRANS_AMT,SETTL_AMT,
        t.AGENT_NO,MCHT_CD,t.MCHT_NAME,IPS_NO,MCHT_AT_C,MCHT_FEE_C,ACQ_INS_FEE_C,ACQ_INS_ALLOT_C,CUPS_FEE_C
        ,FEE_C_OUT,INS_MCC_CODE from (select DATE_SETTLMT,TRANS_DATE_TIME,PAN,TRANS_AMT,SETTL_AMT,
        MCHT_CD,IPS_NO,MCHT_AT_C,MCHT_FEE_C,ACQ_INS_FEE_C,ACQ_INS_ALLOT_C,CUPS_FEE_C
        ,FEE_C_OUT,INS_MCC_CODE from tbl_algo_dtl_his_fx  where is_cash = 2 limit %d,%d) a
        left join (select * from tbl_mcht_inf where is_cash = 2) t on a.mcht_cd = t.mcht_no 
    '''%(x*page_num,page_num)
    df1 = pd.read_sql_query(sql, engine)

    df1.to_csv('order\order_is_cash_2_%02d.csv' % x, encoding='gbk', index=False)
    print("第%d页下载完成" % (x + 1))

if __name__=='__main__':
    cnt = query_cnt()
    print(cnt)

    page_num = 20000
    pages = (cnt-1)//page_num+1
    # 文件数记录下来
    with open('F:\\GitHub\\python\\python-test\\oracle\\total\\is_cash_2.txt', 'w') as f:
        f.write(str(pages))
    p = Pool(15)
    for x in range(pages):
        # start = x*page_num+1
        # end = (x+1)*page_num
        p.apply_async(query_page, args=(page_num,x))
    p.close()
    p.join()



