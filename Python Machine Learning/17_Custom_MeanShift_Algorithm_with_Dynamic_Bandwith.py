import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

X = np.array([
    [1, 2],
    [1.5, 1.8],
    [5, 8],
    [8, 8],
    [1, 0.6],
    [9, 11],
    [8, 2],
    [10, 2],
    [9, 3],
])

colors = 10 * ["g", "r", "c", "b", "k"]
print(colors)


class Mean_Shift():

    def __init__(self, radius=None, radius_norm_step = 100):
        self.radius = radius
        self.radius_norm_step = radius_norm_step

    def fit(self, data):

        if self.radius == None:
            all_data_centroid = np.average(data, axis=0)
            all_data_norm = np.linalg.norm(all_data_centroid)
            self.radius =all_data_norm / self.radius_norm_step

        centroids = {}
        weights = [for i in range(self.radius_norm_step)][::-1] # -1 to -99

        for i in range(len(data)):
            centroids[i] = data[i]  # choose data samples as sample centroids

        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                centroid = centroids[i]

                for featureset in data:
                    # if the distance between feature set and centroid is less than the radius
                    # then feature set is inside the bandwidth of the centroid
                    #if np.linalg.norm(featureset - centroid) < self.radius:
                    #    in_bandwidth.append(featureset)

                    distance = np.linalg.norm(featureset-centroid)
                    if distance == 0:
                        distance = 0.000000001

                    weight_index = int(distance/self.radius)
                    

                # new centroid is avg. of all the items in features send that are in radius
                new_centroid = np.average(in_bandwidth, axis=0)
                new_centroids.append(tuple(new_centroid))

            uniques = sorted(list(set(new_centroids)))

            prev_centroids = dict(
                centroids)  # storing the centroids dictionary in a variable

            centroids = {}  # empty assignment
            for i in range(len(uniques)):
                centroids[i] = np.array(uniques[i])

            optimized = True

            for i in centroids:
                if not np.array_equal(centroids[i], prev_centroids[i]):
                    optimized = False
                if not optimized:
                    break

            if optimized:
                break

        self.centroids = centroids

    def predict(self, data):
        pass


clf = Mean_Shift()
clf.fit(X)

centroids = clf.centroids

plt.scatter(X[:, 0], X[:, 1], s=150)

for c in centroids:
    plt.scatter(centroids[c][0], centroids[c][1], color='k', marker='*', s=150)

plt.show()
