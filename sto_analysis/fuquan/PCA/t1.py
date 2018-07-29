import numpy as np
from matplotlib.mlab import PCA

data = np.array(np.random.randint(10,size=(10,3)))
print data
results = PCA(data)
print results






