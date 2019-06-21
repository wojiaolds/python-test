import pandas as pd

#方法一：默认读取第一个表单
df=pd.read_excel('lemon.xlsx')#这个会直接默认读取到这个Excel的第一个表单
print(type(df))
data=df.head()#默认读取前5行的数据
print(type(data))
print("获取到所有的值:\n{0}".format(data))#格式化输出
print('---------------------------------------')



#方法二：通过指定表单名的方式来读取
df=pd.read_excel('lemon.xlsx',sheet_name='student')#可以通过sheet_name来指定读取的表单
data=df.head()#默认读取前5行的数据
print("获取到所有的值:\n{0}\n{1}".format(data,data))#格式化输出
print('---------------------------------------')

#方法三：通过表单索引来指定要访问的表单，0表示第一个表单
#也可以采用表单名和索引的双重方式来定位表单
#也可以同时定位多个表单，方式都罗列如下所示
#返回的是数据字典类型
df=pd.read_excel('lemon.xlsx',sheet_name=['python','student'])#可以通过表单名同时指定多个
# df=pd.read_excel('lemon.xlsx',sheet_name=0)#可以通过表单索引来指定读取的表单
# df=pd.read_excel('lemon.xlsx',sheet_name=['python',1])#可以混合的方式来指定
# df=pd.read_excel('lemon.xlsx',sheet_name=[1,2])#可以通过索引 同时指定多个
data=df.values()#获取所有的数据，注意这里不能用head()方法哦~
print(type(df))
# print("获取到所有的值:\n{0}".format(data))#格式化输出
for k,v in df.items():
    print(k,'\n',v)


