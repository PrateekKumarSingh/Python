# Regular approach
cubes = [] # empty dictionary
for x in range(1,10):
    cubes.append(x**3)
print("Cubes",cubes)

# List Comprehension approach, which works exactly like the regular approach
cubes = [x**3 for x in range(1,10)] # List comprehensions provide a concise way to create lists
print("Cubes using List comprehension",cubes)

# Usecase 1 - Performing operations on each element of a list.
import math
print([abs(x) for x in [1,3,6,7,-2, 3, 23,51,0,1]])
print([math.ceil(x) for x in [1.234,3.3,6,7,-2, 3.6, 2.3,51.1,0,1]])
print([x+1 for x in [100,200,300,400]])
print([x.strip() for x in [' apple',' banana    ','  orange  ']]) # triming white spaces

# Usecase 2 - Filtering the list
print([x for x in [-1,2,3,4-5,0,8] if x>=0]) # Removing negetive numbers from the list
print([x for x in ['My',None,'name','is','','Prateek'] if x!='' and x!= None]) # Removing empty strings and null values

# Usecase 3 - Flatten a list
list2d = [[1,2,3],[4,1],[5,6,7],[8,9]] # Two-dimensional list
print('Flattened 1D list',[num for element in list2d for num in element])




