import pandas as pd
from openpyxl import load_workbook


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)



def _excelAddSheet(dataframe, excelWriter, sheet_name):
    book = load_workbook(excelWriter.path)
    excelWriter.book = book
    dataframe.to_excel(excel_writer=excelWriter, sheet_name=sheet_name, index=True)
    excelWriter.close()

path=r'F:\GitHub\python\python-test\excel\order.xlsx'
excelWriter = pd.ExcelWriter(path,engine='openpyxl')
df=pd.read_excel(path,sheet_name='交易流水')
print(df)
# print(df.info())

# 按商户号统计交易总笔数
print('-----'*10)
df1 = df.groupby('商户号')['商户号'].count()
df1.name = '笔数'
# print(type(df.groupby('商户号')['商户号']))
# _excelAddSheet(df1, excelWriter, '商户汇总笔数')

# 按商户号日期统计交易总笔数
print('-----'*10)
df1 = df.groupby(['商户号','交易日期','交易状态'])['商户号'].count()
df1.name = '笔数'
# print(type(df.groupby(['商户号','交易日期'])))
# print(type(df1))
print(df1)
# print(df1.index)
# print(pd.DataFrame(df1))
# _excelAddSheet(df1, excelWriter, '商户日期汇总笔数')


# 按商户号统计交易总金额
print('---------------'*10)
df2 = df.groupby(['商户号','交易日期','交易状态'])['交易金额'].sum()
# print(type(df2))
# print(df2)
df3 = pd.merge(df1,df2,left_index=True,right_index=True)
df3['交易金额'] = df3['交易金额'].map(lambda x:x*0.01)

print (df3)
# _excelAddSheet(df3, excelWriter, '商户交易汇总')


# print ("display.max_columns = ", pd.get_option("display.max_columns"))
# print ("after set display.max_colwidth = ", pd.get_option("display.max_colwidth"))
# print ("after set display.max_columns = ", pd.get_option("display.max_columns"))


