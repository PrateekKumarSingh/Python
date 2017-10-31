from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

# print(plt.style.available)
# ['bmh', 'classic', 'dark_background', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn
# -dark-palette', 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seabo
# rn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', '_classic_test'

style.use('dark_background') # change the style (theme) of the chart

# coordinates
#x1 = [1,2,3,2]
#y1 = [9,2,7,4]
#x2 = [1,3,6,9]
#y2 = [7,3,4,8]

# load coordinates from CSV files
x1,y1 = np.loadtxt('.\\samplefiles\\coordinates1.csv',
                 unpack= True,
                 delimiter=',')
x2,y2 = np.loadtxt('.\\samplefiles\\coordinates2.csv',
                 unpack= True,
                 delimiter=',')

# plot the coordinates on the graph
plt.plot(x2,y2,'red',linewidth=4, label = 'CompanyTrend2')
plt.plot(x1,y1,'yellow',linewidth=2, label = 'CompanyTrend1')  # .plot(xcoordinate, ycoordinate, linecolor, linewidth, label)
  
#plt.scatter(x1,y1,color='yellow',label = 'yellow')  # .plot(xcoordinate, ycoordinate, linecolor, linewidth, label)
#plt.scatter(x2,y2,color ='red', label = 'red')

plt.bar(x2,y2,color='blue', label = 'Company2')#', align='center')
plt.bar(x1,y1,color='cyan',label = 'Company1')#, align='center')  # .plot(xcoordinate, ycoordinate, linecolor, linewidth, label)

plt.title('Company Trend') # define the title using .title('your title goes here')
plt.ylabel('Revenue Growth') # Label on X-Axis
plt.xlabel('Year') # Label on Y-Axis
plt.legend() # Label in .plot() function doesn't work until .legend() function is called

plt.grid(True,color='gray') # defining graph grid properties
plt.show() # graph doesn't apears unless this function is invoked.
