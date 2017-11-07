#create a game where user has 10 chances to guess a number between 1 and 20
import random

x=random.randint(1, 20)


#ask user to input guess
guess=int(raw_input('please input your guess:\n'))
#to specify the number of tries they have
for i in range(1, 11):
    #if guess is too low
    if guess<x:
        print 'This guess is too low try again'
        guess = int(raw_input('please input your guess:\n'))
    #if guess is too high
    elif guess>x:
        print 'This guess is too high try again'
        guess = int(raw_input('please input your guess:\n'))
    else:
        break #this condition would be the correct answer


if guess==x:
    print 'you are correct!'
else:
    print 'you have run out of guesses'
