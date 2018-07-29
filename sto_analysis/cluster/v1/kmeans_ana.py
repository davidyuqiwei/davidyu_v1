#print type(x1)
import matplotlib.pyplot as plt
from get_kmeans_data import *

data_raw,data_norm,stock_index_match=get_kmeans_data(0,50)
# print data_raw
print stock_index_match

cluster_num=5
kmeans_model = KMeans(n_clusters=cluster_num, random_state=1).fit(data_norm)
labels = kmeans_model.labels_
cnt=Counter(labels)
print cnt

for lab1 in range(0,cluster_num):
    n1=np.where(labels==lab1)[0]
    #print n1
    a1=[stock_index_match[i] for i in n1]
    #print stock_index_match[n1]
    print lab1,'   ',a1

#print labels
for lab1 in range(0,cluster_num):
    n1=np.where(labels==lab1)[0]
    #print np.where(labels==1)
    len_n1=len(n1)
    # print n1
    # print len(n1)
    fig=plt.figure()
    for idx in xrange(len_n1):
        #plt.figure(2,2)
        if idx<30:
            ax=fig.add_subplot(5,6, idx+1)
            nn1=n1[idx]
            plt.plot(xrange(0,82),data_raw[nn1])
#plt.show()
