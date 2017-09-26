import random, sys
while True:
    choice = input("Do you want roll the dice? [Y/N] ")
    if choice=='Y' or choice=='y':
        print(random.randint(1,6))
    else:
        print('You chose to exit!')    
        sys.exit() # to exit the script
