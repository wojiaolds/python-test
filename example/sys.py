import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

print ('参数个数为:', len(sys.argv), '个参数。')
print ('参数列表:', str(sys.argv))
