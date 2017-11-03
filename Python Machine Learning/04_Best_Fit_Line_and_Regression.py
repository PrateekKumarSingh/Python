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

# step 3 - train the classifier by passing training data set
m,b = best_fit_slope_and_intercept(x,y)
regression_line = [ (m*item)+b for item in x ] # y = mx + b

# step 4 - predict
predict_x = 12 # feature
predict_y = (m*predict_x)+b # label

# step 5 - represent
plt.scatter(x,y, c = 'red')
plt.scatter(predict_x, predict_y, c = 'green')
plt.plot(x,regression_line)
plt.show()



