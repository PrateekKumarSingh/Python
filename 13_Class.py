class calc:
    def add(x,y):
        print(x+y)
    def sub(x,y):
        print(x-y)
    def mul(x,y):
        print(x*y)
    def div(x,y):
        print(x/y)


calc.add(3,2)        
calc.sub(3,2)        
calc.mul(3,2)        
calc.div(3,2)        


class dog:
    def __init__(self, legs, color):
        self.legs = legs
        self.color = color

beagle = dog(4, 'brown')
print(beagle.color)