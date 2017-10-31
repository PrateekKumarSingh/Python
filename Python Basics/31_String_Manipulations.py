string = 'Hello my name is Prateek Singh\nI\'m a 27 year young'
print("Original String: ",string)


print(string[:5]) # slicing the string upto 'n' index value from the first index
print(string[6:]) # slicing the string from 'n' index value upto the last index
print(string[6:25]) # slicing the string from a specific index to another

print('hello world'.capitalize()) # capitalize 1st char of the string
print('hello world'.title()) # all words to title case

# .split() and .join()
print(string.split(' ')) # splitting the string by white space
print(string.split('my')) # splitting the string by a word, eq. 'my'
print(string.split('\n')) # splitting by newline character

print(' '.join('Prateek')) # Joining each char with a space
print('*'.join('Prateek')) # Joining each char with a '*'

# reversed()
print(list(reversed('python')) ) # reversing a string
print(''.join(reversed('python'))) # reversing a string
print(list('abcdefgehi')[::-1]) # reversing a string

# .strip() , .lstrip() , .rstrip()
print(['   Hey there      '.strip()]) # stripping white spaces from both ends of the string
print(['   Hey there      '.lstrip()]) # stripping white spaces from left end of the string
print(['   Hey there      '.rstrip()]) # stripping white spaces from right end of the string

# .rjust() .ljust(), .center()
print('Hello'.rjust(30))
print('Hello'.ljust(30,'-'))
print('Hello'.rjust(30,'*'))
print('Hello'.center(30,'_'))

# USECASE - printing a table using .center()
age = {'prateek':27,'mayank':25,'utkarsh':22} # ame-age dictionary
header = '| '+'Name'.center(20,)+' | '+'Age'.center(20)+' |'

print(len(header)*'-')
print(header)
print(len(header)*'-')

for key, value in age.items():
    print('|',str(key).center(20),'|',str(value).center(20),'|')
print(len(header)*'-')
