import numpy as np
from math import sqrt
#import matplotlib.pyplot as plt
#from matplotlib import style
import warnings
from collections import Counter
import pandas as pd
import random

accuracies = []

for i in range(25):
    # function to classify the class of 'predict' using k-NN algorithm on 'data'
    def k_nearest_neighbors(data, predict, k=5):
        if len(
                data
        ) >= k:  # deciding number of votes required to classify a feature, usually k = Number of classes in data + 1
            warnings.warn('K is set to a value less than total voting group!')

        distances = []  # list to store distances of prediction point to other datapoints

        for group in data:
            for features in data[group]:
                euclidean_distance = sqrt((features[0] - predict[0])**2 +(features[1] - predict[1])**2)
                # you can also use below line instead of one above
                #euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
                distances.append([euclidean_distance, group])
        votes = [i[1] for i in sorted(distances)[:k]]
        vote_result = Counter(votes).most_common(1)[0][0]  # groups and counts votes and finds the most common
        confidence = (Counter(votes).most_common(1)[0][1] / k)*100  # percentage of votes in favor of result
        return vote_result, confidence

    df = pd.read_csv('./samplefiles/breast-cancer-wisconsin.txt') # read the csv file as data frame
    df.replace('?',-9999,inplace=True) # inplace=True to replace the data but don't return the copy of object
    df.drop(['id'], 1, inplace=True) # drop the ID column of the data frame because it reduces the accuracy, comment this line to see the difference
    full_data = df.astype(float).values.tolist()
    random.shuffle(full_data) # randomize you data

    test_size = 0.4 # i.e 20% for total data set is for testing
    train_data = full_data[:-int(test_size*len(full_data))] # Index to slice 80% from full data = (test_size*len(full_data))
    test_data = full_data[-int(test_size*len(full_data)):] # slice remaining 20% from full data for testing

    train_set = {2: [],4: []} # placeholder dictionaries to store training data set in dictionary
    test_set = {2: [], 4: []}  # placeholder dictionaries to store testing data set in dictionary

    # convert training and test data into dictionaries
    for i in train_data:
        train_set[i[-1]].append(i[:-1])

    for i in test_data:
        test_set[i[-1]].append(i[:-1])

    # check the correctness of KNN algorithm when training data set is passed to it
    # against the testing data and calculate the overall accuracy of the algorithm
    correct = 0
    total = 0

    for group in test_set:  # group = 2 (benign) or group = 4 (malign)
        for data in test_set[group]:  # this step is like test_set[2] or test_set[4]
            vote, confidence = k_nearest_neighbors(train_set, data, k=5) # k=5 is default
            if group == vote:
                correct += 1 # success when KNN algorithm with training data classifies the test data correctly
            #else:
            #print('Incorrect Test result:',vote,'Confidence:{0}%'.format(confidence))
            total += 1 # total data tested
    
    accuracy = correct / total
    accuracies.append(accuracy)
    #print('Accuracy:',accuracy)

print('Avg. Accuracy:',sum(accuracies)/len(accuracies))
