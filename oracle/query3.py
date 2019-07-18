import pandas as pd
from sqlalchemy import create_engine
from multiprocessing import Pool
import os, time, random

# engine = create_engine("oracle://posp:Dyf_pOsp@192.168.10.109:1521/dyfdb1",encoding='utf-8', echo=True)
#
# def query_cnt():
#     sql = '''
#         select count(*) from tbl_algo_dtl_his a
#         left join AGENT.TBL_MCHT_INF t on a.mcht_cd = t.mcht_no
#         where t.reserve5 ='0' and t.AGENT_NO in('1035','1071','1106','1034','1082','1109','1108','1060','1083')
#         '''
#     df = pd.read_sql_query(sql, engine)
#     cnt = df.iloc[0, 0]
#     return cnt
#
# def query_page(start,end,x):
#     print("开始下载第%d页" % (x+1))
#     sql = '''
#            select * from (select  ROWNUM AS rowno, DATE_SETTLMT,TXN_KEY,KEY_CANCEL,TRANS_DATE,TRANS_DATE_TIME,TXN_SSN,TERM_SSN,AUTH_SSN,PAN,TRANS_AMT,SETTL_AMT,
#             t.AGENT_NO,MCHT_CD,t.MCHT_NAME,IPS_NO,TERM_ID,TXN_NUM,CHNL_CD,CARD_TP,CARD_MED,ACQ_INS_ID_CD,STLM_INS_ID_CD,OBJ_INS_ID_CD,BRH_INS_ID_CD,
#             C_D_FLG,MCHT_AT_D,MCHT_AT_C,MCHT_FEE_D,MCHT_FEE_C,MCHT_ALLOT_D,MCHT_ALLOT_C,ACQ_INS_AT_D,ACQ_INS_AT_C,ACQ_INS_FEE_D,
#             ACQ_INS_FEE_C,ACQ_INS_ALLOT_D,ACQ_INS_ALLOT_C,CUPS_AT_D,CUPS_AT_C,CUPS_FEE_D,CUPS_FEE_C,CUPS_ALLOT_D,CUPS_ALLOT_C,
#             FEE_D_OUT,FEE_C_OUT,MCHT_FEE_MD,MCHT_FEE_PCT_MIN,MCHT_FEE_PCT_MAX,MCHT_ALOT_PCT_MAX,MCHT_ALOT_PCT_MIN,ACQ_INS_FEE_PCT_MIN,
#             ACQ_INS_FEE_PCT_MAX,ACQ_INS_ALOT_PCT_MIN,ACQ_INS_ALOT_PCT_MAX,T_0_FLAG,TXN_ACQ_TYPE,ORG_TXN_NUM,REC_OPR_ID,INS_MCC_CODE,
#             DEST_ID,CHANNEL_TYPE from tbl_algo_dtl_his a
#             left join AGENT.TBL_MCHT_INF t on a.mcht_cd = t.mcht_no
#             where t.reserve5 ='0' and t.AGENT_NO in('1035','1071','1106','1034','1082','1109','1108','1060','1083') and rownum <= %d) r
#             where r.rowno >=%d
#             '''%(end,start)
#     df1 = pd.read_sql_query(sql, engine)
#     # df1['create_time'] = df1['create_time'] + '\t'
#     # df1['user_account'] = df1['user_account'] + '\t'
#     # df1['cust_id'] = df1['cust_id'] + '\t'
#     # df1['agent_id'] = df1['agent_id'] + '\t'
#     df1.to_csv('order\order_0_1_%02d.csv' % x, encoding='gbk', index=False)
#     print("第%d页下载完成" % (x + 1))
#
# if __name__=='__main__':
#     cnt = query_cnt()
#     print(cnt)
#
#     page_num = 20000
#     pages = (cnt-1)//page_num+1
#     # 文件数记录下来
#     with open('F:\\GitHub\\python\\python-test\\oracle\\total\\pages1.txt', 'w') as f:
#         f.write(str(pages))
#     p = Pool(15)
#     for x in range(pages):
#         start = x*page_num+1
#         end = (x+1)*page_num
#         p.apply_async(query_page, args=(start,end,x))
#     p.close()
#     p.join()


engine = create_engine('mysql+mysqlconnector://test:yzkj@2019!#$^@192.168.10.131:3306/posp')
def query_cnt():
    sql = '''
        select count(*) from tbl_algo_dtl_his_fx where is_cash = 3;
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
        ,FEE_C_OUT,INS_MCC_CODE from tbl_algo_dtl_his_fx  where is_cash = 3 limit %d,%d) a
        left join (select * from tbl_mcht_inf where is_cash = 3) t on a.mcht_cd = t.mcht_no 
    '''%(x*page_num,page_num)
    df1 = pd.read_sql_query(sql, engine)

    df1.to_csv('order\order_is_cash_3_%02d.csv' % x, encoding='gbk', index=False)
    print("第%d页下载完成" % (x + 1))

if __name__=='__main__':
    cnt = query_cnt()
    print(cnt)

    page_num = 20000
    pages = (cnt-1)//page_num+1
    # 文件数记录下来
    with open('F:\\GitHub\\python\\python-test\\oracle\\total\\is_cash_3.txt', 'w') as f:
        f.write(str(pages))
    p = Pool(15)
    for x in range(pages):
        # start = x*page_num+1
        # end = (x+1)*page_num
        p.apply_async(query_page, args=(page_num,x))
    p.close()
    p.join()

