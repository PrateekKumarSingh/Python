import pandas as pd
import quandl, math, datetime, pickle
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style


style.use('ggplot')

# gather data from Quandl for Google stocks
df = quandl.get('WIKI/GOOGL')

# use a dataframe data stucture to hold features
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HighLow Percent'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['Percent Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HighLow Percent', 'Percent Change', 'Adj. Volume']]

df.fillna(-99999, inplace=True) # replacing missing data = NaN with -99999

forecast_out = int(math.ceil(0.01 * len(df))) # number of 'Labels' to be predicted about, i.e 10% of total data set in our case
df['Label'] = df['Adj. Close'].shift(-forecast_out) # add some values to Label, except the Labels that needs to be forecasted/predicted

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

# [1.1] Preparing the Training Data or Training set
X = np.array(df.drop(['Label'],1))  # separates the 'Features' from 'Label' and store it in X = Features (uppercase X)
X = preprocessing.scale(X)  # Converts 'features' in machine learning to be in a range of -1 to 1
X_latestfeatures = X[-forecast_out:] # selects latest 'features'
X = X[:-forecast_out] # excludes the latest 'features'
df.dropna(inplace=True) # drop any data set with missing data

y = np.array(df['Label'])  # only selects the Label

# [1.2] Split the training data into two parts [75% to train and 25% to test]
X_trainset, X_testset, y_trainset, y_testset = model_selection.train_test_split(X, y, test_size=0.2)

# [2] define and train the clasifier with the training data
# What is regression?
#   Linear regression calculates an equation that minimizes the distance between the fitted line and all of the data points. 
#   Technically, ordinary least squares (OLS) regression minimizes the sum of the squared residuals.

clf = LinearRegression(n_jobs=-1) # define the classifier, support vector machine (SVM) or linear regression in this example

# clf = svm.SVR() # https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
clf.fit(X_trainset, y_trainset)  # .fit() is anonymous to training, like you get fit when you train.

# saving the trained classifier into a file,
# it can save a lot of time by avoid retraining the classifier with same data
with open('.\samplefiles\linearregression.pickle','wb') as f:
    pickle.dump(clf, f)
# loading the trained classifier from the file
pickle_in = open('.\samplefiles\linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)

# [3] test the training data
# that is, comparing the classifier with the trained data against the test data
# to get the confidence/correctness/accuracy of the classifier
accuracy = clf.score(X_testset, y_testset)

# [4] predict
forecast_set = clf.predict(X_latestfeatures)

# [5] represent data
df['Forecast'] = np.nan # creating a column with empty data
lastdate = df.iloc[-1].name
lastunix = lastdate.timestamp()
oneday = 86400
nextunix = lastunix + oneday

# iterating through the forecast set, taking each forecast and day,
# and then setting those values in the dataframe (making the future "features" NaNs).
# The last line's code just simply takes all of the first columns, setting them to NaNs,
# and then the final column is whatever i is (the forecast in this case).

for i in forecast_set:
    nextdate = datetime.datetime.fromtimestamp(nextunix)
    nextunix += oneday
    df.loc[nextdate] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
