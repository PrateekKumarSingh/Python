'''
This clustering algorithm seems to automatically categorize these people into who might survive or not on the ship's sinking. 
We don't have much in the way of determining exactly what the machine is thinking about why these are the groups chosen, 
but they appear to have a high degree of correlation with survivability.
'''

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import MeanShift
from sklearn import preprocessing
import pandas as pd
'''
Pclass Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
survival Survival (0 = No; 1 = Yes)
name Name
sex Sex
age Age
sibsp Number of Siblings/Spouses Aboard
parch Number of Parents/Children Aboard
ticket Ticket Number
fare Passenger Fare (British pound)
cabin Cabin
embarked Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
boat Lifeboat
body Body Identification Number
home.dest Home/Destination
'''

df = pd.read_excel('./samplefiles/titanic.xls')
original_df = pd.DataFrame.copy(df)

df.drop(['body', 'name'], 1, inplace=True)
df.convert_objects(convert_numeric=True)
df.fillna(0, inplace=True)

#print(df.head(10))


# function to convert non-numerical data like Sex, Cabin, Home into numerical values
# sex = male/female becomes 0/1
def handle_non_numerical_data(df):
    columns = df.columns.values

    for column in columns:
        text_digit_vals = {}

        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x += 1

            df[column] = list(map(convert_to_int, df[column]))

    return df


df = handle_non_numerical_data(df)
#print(df.head(10))

df.drop(['sex', 'boat'], 1, inplace=True)

X = np.array(df.drop(['survived'], 1).astype(float))
X = preprocessing.scale(X)
y = np.array(df['survived'])

clf = MeanShift()  # defining the classifier
clf.fit(X)  # training the classifier with 'feature' set X

labels = clf.labels_
cluster_centers = clf.cluster_centers_

#print(labels)
#print(cluster_centers)

original_df['cluster_group'] = np.nan

#print(original_df.head())

for i in range(len(X)):
    original_df['cluster_group'].iloc[i] = labels[i]

n_clusters_ = len(np.unique(labels))  # number of clusters
print('Labels', np.unique(labels))
print("No. of clusters:", n_clusters_)

survival_rates = {}
for i in range(n_clusters_):
    temp_df = original_df[(original_df['cluster_group'] == float(i))]
    survival_cluster = temp_df[(temp_df['survived'] == 1)]
    survival_rate = len(survival_cluster) / len(temp_df)
    survival_rates[i] = survival_rate

print("Survival Rates:", survival_rates)
