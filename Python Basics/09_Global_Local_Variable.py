x = 5

def test():
    print(x)
    print(x+1)

test()    


x = 5

def test():
    global x #defining the global scope of a variable
    print(x)
    print(x+1)
    x+=1    # this statement will give error because assignment operation won't work on variable defined out of scope of Test()
    print(x)

test()    


