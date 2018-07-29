from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2], [1, 4], [1, 0],
    [4, 2], [4, 4], [4, 0]])
print X
kmeans=KMeans(n_clusters=3,random_state=0).fit(X)
print kmeans
print kmeans.labels_
