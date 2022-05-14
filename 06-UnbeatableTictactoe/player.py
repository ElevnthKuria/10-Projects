import math
import random
import string 

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            #we check the correct value by trying to cast,
            #it to an integer, and if its not, then we say its invalid
            #if that spot is not available on the board, still invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val 

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) 

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #random choose one
        else:
                #get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X' #other player

        #1. check previous move is a winner, this is our base class
        #2. t
        if state.current_winner == other_player:
            return {'position' : None, 'score': 1 * (state.num_empty_squares() +1 ) if other_player == max_player else -1 * (
                state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return{'position': None, 'score': 0}
            
        if player == max_player:
            best = {'position':None, 'score': -math.inf} # each score to be max
        else:
            best = {'position':None, 'score':math.inf}               

        for possible_move in state.available_moves():
            #step1: make move, try taht spot
            state.make_move(possible_move, player)
            #step2: recurse using miniimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)
            #step3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['postion'] = possible_move
            #step4: update the dict if necessary
            if player == max_player:#max the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score #replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score #replace best
        return best
















