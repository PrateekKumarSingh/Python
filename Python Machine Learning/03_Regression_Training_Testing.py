import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')

# use a dataframe data stucture to hold features
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HighLow Percent'] = (
    df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['Percent Change'] = (
    df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HighLow Percent', 'Percent Change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

# performing a simple shift operation to forecast resultsface
forecast_out = int(math.ceil(0.01 * len(df)))
df['Forecast'] = df[forecast_col].shift(-forecast_out)

# What are 'features' and 'Label' in machine learning ?
# -------------------------------------------------------
# The label is the name of some category. If you're building a machine learning system
# to distinguish fruits coming down a conveyor belt, labels for training samples might be "apple", " orange", "banana".
# The features are any kind of information you can extract about each sample.
# In our example, you might have one feature for colour, another for weight,
# another for length, and another for width. Maybe you would have some measure of concavity or linearity or ball-ness.
#
# Machine Learning tries to learn how to guess a label when all we have are some features.
# Usually it does this by looking at a bunch of training samples where we know the labels ahead of time,
# so we can learn what the features for each category look like and how the categories' features differ from one another.
# If all you know about a fruit is it's colour, then a red fruit is likely an apple, and a yellow one is probably a banana.
#
# SOURCE : https://www.reddit.com/r/MachineLearning/comments/48tmo1/quick_question_what_does_label_and_feature_of/

df.dropna(inplace=True)

# [1.1] Preparing the Training Data or Training set
X = np.array(df.drop(['Forecast'],1))  # separates the 'Features' from 'Label' and store it in X (uppercase X)
#y = np.array(df['Forecast']) # only selects the label
X = preprocessing.scale(X)  # Converts 'features' in machine learning to be in a range of -1 to 1
y = np.array(df['Forecast'])  # only selects the label

# [1.2] Split the training data into two parts [75% to train and 25% to test]
X_trainset, X_testset, y_trainset, y_testset = model_selection.train_test_split(
    X, y, test_size=0.2)

# define the classifier, support vector machine (SVM) or linear regression in this example
# clf = svm.SVR() # https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
clf = LinearRegression(n_jobs=-1)

# [2] train the clasifier with the training data
clf.fit(X_trainset, y_trainset)  # .fit() is anonymous to training, like you get fit when you train.

# [3] test the training data
# that is, comparing the classifier with the trained data against the test data
# to get the confidence/correctness/accuracy of the classifier
print("Accuracy =", clf.score(X_testset, y_testset))
