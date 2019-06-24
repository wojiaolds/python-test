import pandas as pd
import numpy as np


s = pd.Series(np.random.randn(4))
print ("The axes are:")
print(s.axes)

print('-----'*10)
s = pd.Series(np.random.randn(4))
print ("Is the Object empty?")
print(s.empty)

print('-----'*10)
s = pd.Series(np.random.randn(4))
print(s)
print ("The dimensions of the object:")
print(s.ndim)

print('-----'*10)
s = pd.Series(np.random.randn(2))
print(s)
print ("The size of the object:")
print(s.size)

print('-----'*10)
s = pd.Series(np.random.randn(4))
print(s)
print ("The actual data series is:")
print(s.values)
print(s.dtype)









