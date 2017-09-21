# 'def' to define a function and its body
def basic(): 
    print("This is a basic function")

basic()   # call a function by it's name followed by parenthesis

# Function with parameters
def add(num1,num2):
    print(num1+num2)

add(1,6)  # Function call

# function with default parameters
def plus(num1,num2=2,num3=3):
    print(num1+num2+num3)

plus(3) # num2 = 2 by default

plus(3,num3=1) # Assigning values to specific variable when multiple default parameters are defined


