# a dice rolling simulator
import random, sys
while True:
    choice = input("Do you want roll the dice? [Y/N] ")
    if choice=='Y' or choice=='y':
        print(random.randint(1,6))
    else:
        print('You chose to exit!')    
        sys.exit() # to exit the script
        
        
# Double Dice Game---Monopoly

import random
import sys
import randint
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
while True:
    basic_condition = input("Would you like to play Monopoly? {YES/NO}")
    if basic_condition == "Yes".capitalize:
        print("Lets GO!")
        print('''Dice 1 : {0} Dice 2 : {1}  '''.format(dice1)(dice2)
    elif basic_condition == "no".capitalize :
    print('Bye')
    sys.exit()
    else:
        print("Invalid Command! RESTART THE GAME!")
