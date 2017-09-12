import matplotlib.pyplot as p
from random import shuffle 

num = [1,2,3,4,5,6,7,8,9]
print("Max: ",max(num))

shuffle(num)
p.plot(num,'miter')
p.ylabel('Numbers')
p.show()



