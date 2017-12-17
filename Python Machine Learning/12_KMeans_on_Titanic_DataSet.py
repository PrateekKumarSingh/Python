'''
This clustering algorithm seems to automatically categorize these people into who might survive or not on the ship's sinking. 
We don't have much in the way of determining exactly what the machine is thinking about why these are the groups chosen, 
but they appear to have a high degree of correlation with survivability.
'''

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
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
#print(df.head(10))
df.drop(['body','name'], 1, inplace=True)
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
                    x+=1

            df[column] = list(map(convert_to_int, df[column]))

    return df

df = handle_non_numerical_data(df)
#print(df.head(10))

df.drop(['sex','boat'], 1, inplace=True)

X = np.array(df.drop(['survived'], 1).astype(float)) 
X = preprocessing.scale(X)
y = np.array(df['survived'])

clf = KMeans(n_clusters=2) # choosing the KMeans classifier
clf.fit(X) # training the classifier with 'feature' set X

correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = clf.predict(predict_me)
    #print("Data: {0} Prediction: {1}".format(predict_me, prediction))

    if prediction[0] == y[i]:
        correct += 1

print("Accuracy: {0}%".format(round((correct/len(X))*100,2) ))

