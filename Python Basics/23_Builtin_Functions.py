import time
import calendar
import math
print('Absolute value of -5:',abs(-5))
print('DateTime:',time.asctime())
print('Here is the calendar of September\n',calendar.month(2017,9))

isleap = calendar.isleap(2017)
if isleap==True:
    print('2017 is a leap year')
else:    
    print('2017 is a not a leap year')

numList = [1,3,5,6,84,2,1,23,43,8,9]
print('Max of list {0} :'.format(numList),max(numList))

# Mathmatical operations using built-in functions
x= 5.898
print('Round of {0}:'.format(x),round(x)) # Round() will always convert the number to the nearest integer
print('Floor of {0}:'.format(x),math.floor(x)) # floor() always convert the number to the nearest integer of smaller value
print('Ceiling of {0}:'.format(x),math.ceil(x)) # ceil() always convert the number to the nearest integer of bigger value


NumberInString = '123'
IntToAdd = 5
print('{0}+{1} ='.format(NumberInString,IntToAdd),int(NumberInString)+IntToAdd,'when using int()')
print('{0}+{1} ='.format(NumberInString,IntToAdd),float(NumberInString)+IntToAdd,'when using float()')





