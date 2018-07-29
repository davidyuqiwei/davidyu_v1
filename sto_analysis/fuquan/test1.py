import numpy as np
import pandas as pd
df = pd.DataFrame(np.arange(0,60,2).reshape(10,3),columns=list('abc'))

print df
print df.iloc[::-1]
