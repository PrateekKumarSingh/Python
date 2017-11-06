import numpy as np
from math import sqrt
#import matplotlib.pyplot as plt
#from matplotlib import style
import warnings
from collections import Counter
import pandas as pd
import random

#style.use('fivethirtyeight')
#plot1 = [2,4]
#plot2 = [2,7]
#euclidean_distance = sqrt( (plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2 )
#print('Euclidean Distance:',euclidean_distance)
#[[plt.scatter(ii[0],ii[1], s=100, color =i) for ii in dataset[i]] for i in dataset]
#plt.scatter(new_features[0],new_features[1])
#plt.show()

dataset = {'A': [ [1,2],[2,3],[3,1] ], 'B': [ [6,5],[7,7],[8,6] ]} # dataset with data divided in 2 classes
new_features = [1,7] # data point to be classified

# function to classify the class of 'predict' using k-NN algorithm on 'data'
def k_nearest_neighbors(data, predict, k=5):
    if len(data) >= k: # deciding number of votes required to classify a feature, usually k = Number of classes in data + 1
        warnings.warn('K is set to a value less than total voting group!')

    distances = [] # list to store distances of prediction point to other datapoints

    for group in data:
        for features in data[group]: 
            euclidean_distance = sqrt( (features[0]-predict[0])**2 + (features[1]-predict[1])**2 )
            # you can also use below line instead of one above
            #euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            print("Euclidean Distance froom point {2} to point {1} in class {3} = {0:.2f}".format(euclidean_distance,features,predict,group))
            distances.append([euclidean_distance, group])
    votes = [i[1] for i in sorted(distances)[:k]]
    print('Shortest distances when k={1} are: {0}'.format(sorted(distances)[:k],k) )
    vote_result = Counter(votes).most_common(1)[0][0] # groups and counts votes and finds the most common 
    print('Majority class in votes:',vote_result)
    return vote_result

result = k_nearest_neighbors(dataset,new_features, k=3)
print("Result: {0} falls in class \'{1}\'".format(new_features , result))
