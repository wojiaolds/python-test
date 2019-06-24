import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],
                         columns=['col2','col1'])
print(unsorted_df)
print('-----'*10)
sorted_df=unsorted_df.sort_index() # 默认情况下，按照升序对行标签进行排序。
print(sorted_df)
print('-----'*10)
sorted_df = unsorted_df.sort_index(ascending=False)
print (sorted_df)
print('-----'*10)
sorted_df=unsorted_df.sort_index(axis=1) # 按列排序
print (sorted_df)
print('-----'*10)
unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
print(unsorted_df)
sorted_df = unsorted_df.sort_values(by='col1')
print (sorted_df)
print('-----'*10)
unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by=['col1','col2'])
print (sorted_df)
print('-----'*10)
unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort') # heapsort  quicksort
print (sorted_df)












