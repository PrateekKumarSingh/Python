import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn.cluster import KMeans

style.use('ggplot')

# feature set
X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8],
              [8, 8],
              [1, 0.6],
              [9, 11]])

clf = KMeans(n_clusters=2) # define the classifier with the 'feature' set
clf.fit(X) # train the classifier

centroids = clf.cluster_centers_
# Labels of each point, i.e for n_clusters = 2 Label can be 0 or 1 
# and for n_clusters = 3 Label can be 0, 1 or 2
labels = clf.labels_  
#print(labels)
colors = ["g.", "r.", "c.", "y."]
for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="x",
    s=150,
    linewidths=5,
    zorder=10)
plt.show()
