import sys
import os
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

print ('参数个数为:', len(sys.argv), '个参数。')
print ('参数列表:', str(sys.argv))


print('----------------')
print(os.name)
# print(os.uname()) # uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
print(list(os.environ.keys()))


