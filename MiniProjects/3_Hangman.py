import random, sys
winmsg = ["You're the Saviour!", "Thanks for saving my Life Human!", "You're my hero! you saved me." , "Your smartness saved my life." , "Sigh! I'm safe now." ,"Phew! Finally I'm down, Thanks!", "Awesome! Smarty."]
Lossmsg = ["You've Killed me stupid human !!", "Next time atleast use some brain.", "I wish I was a cat they have 9 lives :(" , "I had faith in you, but your IQ is less than Zero", "You Kill people, You're a criminal!", "My Death is on you! Looser!!"]
guesswords = 'ELEPHANT', 'CZECHOSLOVAKIA','HANKERCHIEF','MILLENNIUM','KLEPTOMANIA','AVACADO','TARANTULA'

winner = '''
________________
   |         |
   |         |
   |
   |
   |        
   |        \o/
   |         |
___|____    //  ** {0}
'''.format(random.choice(winmsg))


start = '''
________________
   |         |
   |         |
   |
   |
   |         
   |        
   |        
___|____
'''
attempt1= '''
________________
   |         |
   |         |
   |         o
   |
   |
   |        
   |        
___|____
'''

attempt2= '''
________________
   |         |
   |         |
   |         o
   |        /|\\
   |
   |
   |         
___|____
'''
attempt3= '''
________________
   |         |
   |         |
   |         o
   |        /|\\
   |        // 
   |
   |         
___|____        ** {0} 
'''.format(random.choice(Lossmsg))

attempt = [attempt1,attempt2,attempt3]

word = list(random.choice(guesswords))
maxcharstohide = int(len(word)/2)

morphedWord=word
morphedchars=[]

def getCharToMorph(n):
    char = word[random.choice(range(1,n))]
    return char

for i in range(int(maxcharstohide)):
    charToReplace = getCharToMorph(maxcharstohide)
    morphedchars.append(charToReplace)
    morphedWord = ''.join(morphedWord).replace(charToReplace,'*')

print(morphedWord)
print(str((word))
for i in range(0,3):
    answer = input("Guess the above {0} Letter word, this is your {1}/3 attempt : ".format(len(word),i+1))
    if answer==str((word):
        print(winner)
    else:
        print(attempt[i])
