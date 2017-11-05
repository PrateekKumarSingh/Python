from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

# step 1 - prepare training data
x = np.array([1,2,3,5,7,9], dtype=np.float64)
y = np.array([4,5,6,7,8,10], dtype=np.float64)

# step 2 - define a classifier/model = linear regression
def best_fit_slope_and_intercept(x,y):
    m = ( ( mean(x) * mean(y) ) - ( mean(x*y) ) ) / ( mean(x)**2 - mean(x**2) ) # slope
    b = mean(y) - m*mean(x) # intercept
    return m,b


# What is Squared error?
#   https://www.youtube.com/watch?v=6OvhLPS7rj4
# Why Squared error?
#   Say you define your error as,
#   Error = PredictedValue − ActualValue.
#
#   Then the error in estimation can be of two kinds,
#       a) You underestimate the value, in which case your error will be negative.
#       b) You overestimate the value, in which case your error will be positive.
#
#   When you average these out, you might get a very low error if you are underestimating
#   and overestimating equally as they will cancel each other out.
#
#   To get rid of the effect of the negative value while taking the mean, we square them.
#
#   A better question would be why not use the absolute difference instead of squaring the errors.
#   This has no definite answer as it is very application specific.
#   In cases where you want to emphasize the spread of your errors,
#   basically you want to penalize the errors that are farther away from the mean (usually 0 in machine learning, a user parameter in statistics). In small scales where your errors are less than 1 because the values themselves are small,
#   taking just the absolute might not give the best feedback mechanism to the algorithm.
#


def squared_error(y_original, y_line):
    return sum((y_line-y_original)**2)


# Whats is R squared or Coeffcient of determination?
#   R-squared is a statistical measure of how close the data are to the fitted regression line.
#   It is also known as the coefficient of determination
#
# R-squared = Explained variation / Total variation
#
# R-squared is always between 0 and 100%-
#         0% indicates that the model explains none of the variability of the response data around its mean.
#       100% indicates that the model explains all the variability of the response data around its mean.
#
# In general, the higher the R-squared, the better the model fits your data

def coefficient_of_determination(y_original, y_line):
    y_mean_line = [mean(y_original) for item in y_original]
    squared_error_regression = squared_error(y_original, y_line)
    squared_error_y_mean = squared_error(y_original, y_mean_line)

    return 1 - (squared_error_regression / squared_error_y_mean)

# step 3 - train the classifier by passing training data set
m,b = best_fit_slope_and_intercept(x,y)
regression_line = [ (m*item)+b for item in x ] # y = mx + b

# step 4 - predict
predict_x = 12 # feature
predict_y = (m*predict_x)+b # label

r_squared = coefficient_of_determination(y, regression_line)
print('R-Squared',r_squared)

# step 5 - represent
plt.scatter(x,y, c = 'red')
plt.scatter(predict_x, predict_y, c = 'green')
plt.plot(x,regression_line)
plt.show()
