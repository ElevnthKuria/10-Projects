
#This ia a game that defs two types of functions that guess a number correctly and prompts user to retry if the input is wrong(using loops).
#it uses the random.randint function to return an integer number selected frlm a specified range.

#The first function performs according to the user's ability to guess a number until the 
#input number is correct. Giving clues whether the input (if wrong) is too low or too high.
# If correct the output is the number itself.

import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low. ")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    return print(f"You have guesssed the number {guess}.")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random .randint(low, high)
        else:
            guess = low
        feedback = input("Is {guess} too (h), too  low (l), or correct (C)??")
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess+1
    print (f"The computer guessed your number, {guess}, correctly!!")
guess(10)
