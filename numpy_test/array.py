import numpy as np




# ndarray.shape 这一数组属性返回一个包含数组维度的元组，它也可以用于调整数组大小。
a = np.array([[1, 2, 3], [4, 5, 6]])
print(type(a))
print(a.shape)

a = np.array([[1, 2 ,3],[4, 5, 6]])
a.shape = (3, 2)
print(a)

print(a.ndim) # 这一数组属性返回数组的维数。

a = np.arange(24)
print(a)

b = a.reshape(2,4,3)
print(b)
# b 现在拥有三个维度

l = [1,2,3,4,5]
x = np.array(l, dtype=np.int8)
print(x.itemsize) #这一数组属性返回数组中每个元素的字节单位长度。


x = np.array([1,2,3,4,5], dtype=np.float32)
print(x.itemsize)


x = np.empty([3,2], dtype=int)
print(x)

x = np.zeros(2)
x = np.zeros((2, 5))  # 默认类型为 float
print(x)

x = np.zeros(5, dtype=np.int)
print(x)

x = np.zeros((2, 2), dtype=[('x',  'i4'),  ('y',  'i4')])
print(x)

x = np.zeros((2, 2), dtype=[('x',  'i4'),  ('y',  'i4'), ('z', 'i4')])
print(x)

x = np.ones(5)  # 默认类型为 float
print(x)

x = np.ones([2, 2], dtype=int)
print(x)



x =  [(1,2,3),(4,5)]
a = np.asarray(x)
print(a)

try:

    s = 'Hello World'
    a = np.frombuffer(s, dtype='S1')
    print(a)
except Exception as ex:
    print(ex)

# 从列表中获得迭代器
l = range(5)
print(list(l))
it = iter(l)
# 使用迭代器创建 ndarray
x = np.fromiter(it, dtype=float)
print(x)

x = np.arange(1,5)
print(x)

x = np.arange(5, dtype=float)
print(x)

x = np.arange(10,20,2)
print(x)

x = np.linspace(10,20,5)
print(x)

import numpy as np
x = np.linspace(10,20,  5, endpoint=False)
print(x)
print(type(x))


x = np.linspace(1,2,5, retstep =  True)
print(x)
print(type(x[0]))
print(x[0])
# 这里的 retstep 为 0.25


# 默认底数是 10
a = np.logspace(1.0,  2.0, num=10)
print(a)


a = np.logspace(1,10,num=10,  base=2)
print(a)


a = np.arange(10)
print(a)
s = slice(2, 9, 2)
print(type(s))
print(a[s])
print(a[2:9:2])


a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
# 对始于索引的元素进行切片
print('现在我们从索引 a[1:] 开始对数组切片' )
print(a[1:])
print(a[0:2,2])

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print('我们的数组是：' )
print(a)
print('\n')
# 这会返回第二列元素的数组：
print('第二列的元素是：')
print(a[..., 1])
print(a[:, 1])
print('\n')
# 现在我们从第二行切片所有元素：
print('第二行的元素是：')
print(a[1, ...])
print(a[1, :])
print(a[1, 0:])
print(a[1, ])
print('\n')
# 现在我们从第二列向后切片所有元素：
print('第二列及其剩余元素是：')
print(a[..., 1:])


x = np.array([[1,  2],  [3,  4],  [5,  6]])
y = x[[0, 1, 2],  [0, 1, 0]]
print(y)


x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0,0],[3,3]])
print(rows)
cols = np.array([[0,2],[0,2]])
print(cols)
y = x[rows,cols]
print('这个数组的每个角处的元素是：')
print(y)
print(x[[0,0,3,3],[0,2,0,2]])



x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print('我们的数组是：')
print(x)
print('\n')
# 切片
z = x[1:4,1:3]
print('切片之后，我们的数组变为：')
print(z)
print('\n')
# 对列使用高级索引
y = x[1:4,[1,2]]
print('对列使用高级索引来切片：')
print(y)


x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：' )
print (x)
print ('\n' )
# 现在我们会打印出大于 5 的元素
print ('大于 5 的元素是：' )
print(x[x > 5])
print(x[~(x > 5)])


a = np.array([np.nan,  1,2,np.nan,3,4,5])
print(a.dtype)
print(a[~np.isnan(a)])
print(a[np.isnan(a)])

a = np.array([1,  2+6j,  5,  3.5+5j])
print(a.dtype)
print(a[np.iscomplex(a)])
print(a[~np.iscomplex(a)])


a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print(c)


a = np.arange(0,60,5)
a = a.reshape(3,4)
print('原始数组是：')
print(a)
print('\n')
print ('原始数组的转置是：')
b = a.T
print (b)
print('修改后的数组是：')
print(type(np.nditer(a)))
for x in np.nditer(a):
    print(x)

print('------------------------------------')
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    print(x)
    print(type(x))
    x[...] = 2 * x
print('修改后的数组是：')
print(a)
a = np.array([1,2,3])
print(2*a)


a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：' )
print (a)
print  ('\n')
print  ('修改后的数组是：')
for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):
    print(type(x))
    print (x)


a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('第一个数组：')
print (a)
print  ('\n')
print  ('第二个数组：')
b = np.array([1,  2,  3,  4], dtype = int)
print (b)
print  ('\n'  )
print  ('修改后的数组是：' )
for x,y in np.nditer([a,b]):
    print(type(x),type(y))
    print  ("%d:%d"  %  (x,y))










