
import pandas as pd
import numpy as np

N = 20

df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
    'x': np.linspace(0, stop=N - 1, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
})
print(df)
# reindex the DataFrame
df_reindexed = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'])
print(type(df_reindexed))
print(df_reindexed)

print('-----'*10)
df1 = pd.DataFrame(np.random.randn(3,3),columns=['col1','col2','col4'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
print(df1)
print(df2)
df1 = df1.reindex_like(df2)
print(df1)

print('-----'*10)
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print(df1)
print(df2)
# Padding NAN's
print(df2.reindex_like(df1))
# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill:")
print(df2.reindex_like(df1,method='ffill'))
print ("Data Frame with Forward Fill limiting to 1:")
print(df2.reindex_like(df1,method='ffill',limit=1))
print ("Data Frame with nearest Fill:")
print(df2.reindex_like(df1,method='nearest'))

print('-----'*10)
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df1)
print ("After renaming the rows and columns:")
df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
                 index = {0 : 'apple', 1 : 'banana', 2 : 'durian'},inplace=False)
print(df1)
print(df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
                 index = {0 : 'apple', 1 : 'banana', 2 : 'durian'},inplace=False))
df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
                 index = {0 : 'apple', 1 : 'banana', 2 : 'durian'},inplace=True)
print(df1)








