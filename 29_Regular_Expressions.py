'''
Identifiers
-----------------
\d any number
\D anything but number
\s space
\S anything but a space
\w any char
\W anything but char
.  any char, except new line
\b the white space around words
\. a period
\\ literal backslash

Modifiers
-----------------
{1,3} we're expecting 1-3
+ match 1 or more
? match 0 or 1
* match 0 or more
$ match end of the string
^ match begining of a string
| either or
[] range or "variance"              [1-5a-zA-O]
{x} expecting "x" amount


White space chars
-----------------
\n new line
\s space
\t tab
\e escape
\f form feed
\r return

ESCAPE THEM
-----------------
. + * ? [ ] $ ^ ( ) { } | \

'''


import re

stringdata = '''
Prateek is 27 years old, and Mayank is 25 years old
Utkarsh is 22, and their father, Rakesh is 60 year old
'''

# .findall() function to get all the data
ages = re.findall(r'\d{1,3}',stringdata)
names = re.findall(r'[A-Z][a-z]*', stringdata)
print('Ages:',ages)
print('Names:', names)


words = re.split(r'\s',stringdata) #.split(pattern, string) to slplit th 'string' by the 'pattern'
print('All words:',words)

threeletterwords=[] # empty list
for each in words:
    match = re.search(r'[a-z]{3}', each) # search for 3 letter words
    if match:
        threeletterwords.append(match.group(0)) # adding items that are 3 lettered to the list

print('Three letter words:',threeletterwords)


dictionary = {}
i=0
for item in names:
    dictionary[item] = ages[i] 
    i+=1
print('Name-Age dictionary:',dictionary)

search = re.search(r'\d{1,2}',stringdata)  
print('position:', search.span()) # to find the posiyion of match
