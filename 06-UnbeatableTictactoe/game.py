'''
import time
import math
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = self.make_board #use 3x3 board
        self.current_winner = None #Keep track of winner


    @staticmethod
    def make_board():
        return[' ' for _ in range(9)]
   
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row)+ ' |')

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
        #moves = []
        #for( i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            # if spot == ' ':
            #   moves.append(i)
        #return moves

    
    def make_move(self, square, letter):
        #if valid make the move,
        #assign square to letter, them return true
        #if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #winner if 3 in a row anywahere.
        #first check row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagnols
        #only if the square is an even number
        #these are the only moves possible to win a diagnol
        if square % 2 == 0:
            diagnol1 = [self.board[i] for i in [0, 4, 8]] #left to right diagnoal
            if all([spot == letter for spot in diagnol1]):
                return True

            diagnol2 = [self.board[i] for i in [2, 4, 6]] #right to left
            if all([spot == letter for spot in diagnol2]):
               return True
        #if all these dail
        return False
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]



def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X' #start letter
    #iterate through while game has empty squares
    #we dont have to worry abt Winner

    while game.empty_squares():
        #get the move from approiate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

            #define function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + " Makes a move to square {}".format(square))
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(letter+ " wins!!")
                return letter
            #after move is made, alternate letters
            letter = 'O' if letter == 'X' else 'X' #switch player

        #tiny break/pause
        time.sleep(.8)

        if print_game:
            print("It\'s a tie ")


if __name__ == '__main__':
    x_player = RandomComputerPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
'''

import math
import time
import string
from player import GeniusComputerPlayer, HumanPlayer, RandomComputerPlayer

class TicTacToe(): 
    def __init__(self): 
        self.board = self.make_board() 
        self.current_winner = None 
        
    @staticmethod 
    def make_board(): 
        return [' ' for _ in range(9)] 
        
    def print_board(self): 
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]: 
            print('| ' + ' | '.join(row) + ' |') 
            
    @staticmethod 
    def print_board_nums(): # 0 | 1 | 2 
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] 
        for row in number_board: 
            print('| ' + ' | '.join(row) + ' |') 
            
    def make_move(self, square, letter): 
        if self.board[square] == ' ': 
            self.board[square] = letter 
            if self.winner(square, letter): 
                self.current_winner = letter 
            return True 
        return False 
        
    def winner(self, square, letter): # check the row 
        row_ind = math.floor(square / 3) 
        row = self.board[row_ind*3:(row_ind+1)*3] # 
        #print('row', row) 
        if all([s == letter for s in row]): 
            return True 
        col_ind = square % 3 
        column = [self.board[col_ind+i*3] for i in range(3)] # print('col', column) 
        
        if all([s == letter for s in column]): 
            return True 
        if square % 2 == 0: 
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # print('diag1', diagonal1) 
            if all([s == letter for s in diagonal1]): 
                return True 
        
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # print('diag2', diagonal2) 
            if all([s == letter for s in diagonal2]):
                return True 
        
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]    


def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' make a move to square {}'.format(square))
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!!')
                return letter
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)
    
    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = GeniusComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)