#Rock-Paper-Scissors is a game, lets you play 1v1 against the computer letting you choose between rock, paper and scissors.


'''
Game Instuctions;
    1. User gets the first chance/pick, between Rock, paper and scissors.
    2. The computer then chooses the remaining two choices left.

    3. To win game, the following are the compulsory rules;
        a.  Scissors beats Paper
        b.  Rock beats Scissors
        c.  Paper beats Rock
    4. If the game ties, you replay against the computer.
'''        

import random

def play():
    user = input("What is your choice?? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if is_win(user, computer):
        return 'You won!'          
            
    return 'You lost!'

#r>s, s>p, p>r
def is_win(player, opponent):
    #return true of player wins
    #r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

def is_tie(user, computer):
    if user == computer:
             
             ans = input()
        
    else:
        ans == 'n' or ans == 'N'
            

print(play())