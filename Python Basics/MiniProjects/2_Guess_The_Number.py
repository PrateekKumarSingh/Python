# Python implementation of the 'guess the number' game
import random, sys
num = random.randint(0,100)
negativeRange = num - random.randint(0,10)
positiveRange = num + random.randint(0,10)

while True:
    guess = int(input('Guess the number in range: [{0}-{1}]'.format(negativeRange,positiveRange)))
    if num==guess:
        print("You guessed it right! The correct number is {0}".format(num))
        sys.exit()
    elif num!=guess and (positiveRange-guess)>=10 :
        print("Wrong! your guess is too low")
    elif num!=guess and guess-negativeRange>=10 :        
        print("Wrong! your guess is too high")
    elif num-guess<3 or guess-num<3 :
        print("you are very close to the number, keep guessing")
