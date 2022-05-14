import time
from player import HumanPlayer, RandomComputerPlayer 

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #use 3x3 board
        self.current_winner = None #Keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row)+ ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        #moves = []
        #for( i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            # if spot == ' ':
            #   moves.append(i)
        #return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

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
        row_ind = square // 3
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
                print(letter + f"Makes a move to square {square}")
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(letter+ " wins!!")
                return letter
            #after move is made, alternate letters
            letter = 'O' if letter == 'X' else 'X' #switch player

        #tiny break/pause
        time.sleep(0.8)

        if print_game:
            print("It\'s a tie ")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)