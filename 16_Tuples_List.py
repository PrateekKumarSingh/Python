# to understand the difference run the below code in python, to take you to a webpage with some explaination

#import webbrowser; webbrowser.open('https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples')

# use () parenthesis to define a tuple, Tuples are immutable (Constant) data structure,
# which are heterogeneous in comparatively faster than list
tuple = (5, 6, 7, 8)
print('Tuple:',tuple)
print("Tuple index 1:",tuple[1]) # number in square bracket is index = 1

# [] square brackets to define a list, lists can be modified, sorted and has homogoneous elements
list = [1,2,8,3,12,23,21,98,2,3,2,4]
print('List:',list)

print('4th index value of list:',list[4])
print('Last index of list:',list[-1])
print('List from index 0-4:',list[0:5]) # To get the specific list indices
print('List from 3rd to Last index:',list[3:len(list)])

list.append(5) #.append() to add an item at the end
print('List after append:',list) 
list.insert(2,34)
print('List after inserting at index 2:',list) 
print('Value at the last index of the list:',list[-1])

list.remove(2) # Remove() function removes the the first occurenece of the value in the parenthesis, i.e. .remove(value)
print('List after removing at value(2):',list) 

list.remove(list[-2]) # If you don't specifically provide a index or a value to the Remove() it will remove the first occurrence of the value
print('List after removing the last second index of the list:',list) 

print('Number of occurence of value=3 : in the list',list.count(3) )

print('Index of 2 in the list:',list.index(2,0,11) )

list.sort() # sorting list in ascending order
print('Sorted list in ascending order:',list)

list.sort(reverse=True) # sorting list in descending order
print('Sorted list in descending order:',list)

print('Sorting list using the sorted():',sorted(list, reverse=False)) # Sorting using the in built function sorted()
string = 'KJSDnkSRnfdNKJNfd'
print('Sorted string:',sorted(string)) # you can sort strings as well with sorted() function
print('Sorted string:',"".join(sorted(string)) ) # use the .join() function to join the characters of the string

print('List:',list)
print('Index of 23:',list.index(23))
