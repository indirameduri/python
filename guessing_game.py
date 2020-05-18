'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types 'exit'
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random


c=0
num=1
while(num!=0):
    num=int(input('\nI have a number in mind(1,10). Can you guess? or\n press 0 to exit: '))
    computer= random.randint(1,11)
    c += 1
    if(num == computer):
        print('\nWow you guessed it! You took {} turns to guess {}'.format(c,computer))
        computer=""
    else:
        print('\nTry again! I chose {}'.format(computer))
print("You took {} turns but couldn\'t guess".format(c))   