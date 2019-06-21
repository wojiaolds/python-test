import pandas as pd

#1：读取指定行
df=pd.read_excel('lemon.xlsx')#这个会直接默认读取到这个Excel的第一个表单
print(type(df))
print(type(df.iloc[0]))
data=df.iloc[0].values #0表示第一行 这里读取数据并不包含表头，要注意哦！
print(type(data))
print("读取第一行的数据：\n{0}".format(data))

print("----------------------------------------")

df=pd.read_excel('lemon.xlsx')
print(type(df.iloc[0:]))
data=df.iloc[0:].values  #读取指定多行  values不包含表头
print(type(data))
print("读取指定行的数据：\n{0}".format(data))
print("----------------------------------------")


df=pd.read_excel('lemon.xlsx')
data=df.iloc[0:2,0:2]
print(type(data))
print("读取指定行指定列的数据：\n{0}".format(data))
print("----------------------------------------")

df=pd.read_excel('lemon.xlsx')
data=df.iloc[[0,2],[0,2]]
print(type(data))
print("读取指定行指定列的数据：\n{0}".format(data))
print("----------------------------------------")

df=pd.read_excel('lemon.xlsx')
print(type(df.index))
print(type(df.index.values))
print("输出行号列表",df.index.values)
print("----------------------------------------")

df=pd.read_excel('lemon.xlsx')
print(type(df.columns.values))
print("输出列标题",df.columns.values)
print("----------------------------------------")

df=pd.read_excel('lemon.xlsx')
#这个方法类似于head()方法以及df.values方法  随机读取几行
print("随机读取几行 输出值 \n",df.sample(2).values)
print("----------------------------------------")

df=pd.read_excel('lemon.xlsx')
print(type(df['data'].values))
print(df['data'])
print(df.iloc[lambda x:x.index % 2 == 0])
print(df['title'][df['title'] == '正常登陆'])
# print("获取指定列 输出值\n",df.iloc[df['title'] == '正常登陆', 0:2])
print("----------------------------------------")


#处理成列表嵌套字典，且字典的key为表头名。
df=pd.read_excel('lemon.xlsx')
test_data=[]
for i in df.index.values:#获取行号的索引，并对其进行遍历：
    #根据i来获取每一行指定的数据 并利用to_dict转成字典
    row_data=df.iloc[i,1:3].to_dict()
    test_data.append(row_data)
print("最终获取到的数据是：{0}".format(test_data))
