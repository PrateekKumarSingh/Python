# to understand the difference run the below code in python, to take you to a webpage with some explaination

#import webbrowser; webbrowser.open('https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples')

# use () parenthesis to define a tuple, Tuples are immutable (Constant) data structure,
# which are heterogeneous in comparatively faster than list

tuple = (5, 6, 7, 8)

# [] square brackets to define a list, lists can be modified, sorted and has homogoneous elements
list = [1,2,3,4]
print('List: ',list)
list.append(5) #.append() to add an item at the end
print('List after append:  ',list) 
list.insert(2,34)
print('List after inserting at index 2:  ',list) 


print("Tuple index = 1 is ",tuple[1]) # nuber in square bracket is index = 1

