import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2018/12/18',
   periods=10), columns=list('ABCD'))
print(df)
df.plot()

# df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
# df.plot.bar()

plt.show()





