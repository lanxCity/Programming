import random
import time


# =====> Creating functions
# Centralizing displayed message function
def centre_msg():
    return '{:^30}'.format('')


# Random and delay function
def comp_rand_and_delay(delay):
    time.sleep(delay)
    return random.randint(0, 2)


# Displaying board function
def display_board(board):
    board_chars = ['--', 'X', 'O']

    for row in board:
        new_row = ''
        for col in row:
            new_row += f'{board_chars[col]}\t\t'

        print(new_row)

    print()
    return


#  ========> Starting classes
class Board:
    def __init__(self):
        spaces = [[0 for j in range(3)] for i in range(3)]
        self.spaces = spaces

    def space_filled(self, row, col):
        space_occupied = self.spaces[row][col]
        if space_occupied:
            return True
        return False

    def fill_space(self, row, col, player):
        self.spaces[row][col] = player
        return

    @property
    def get_open_spots(self):
        return [j for i in self.spaces for j in i if j == 0]


class Player:
    def __init__(self, num):
        self.num = num

    def make_move(self, spot):

        if ',' in spot:
            joined_spot = spot.replace(' ', '').replace(',', '', 1)

            if joined_spot.isdigit() and len(joined_spot) == 2:
                spot = spot.replace(' ', '').split(",")
                row = int(spot[0])
                col = int(spot[1])

                if 0 <= row <= 2 and 0 <= col <= 2:
                    spot = [row, col]
                    return spot
                else:
                    print(f'{centre_msg()}Out of boundary! Try again.', '\n')
                    return

        print(f'{centre_msg()}Invalid!', '\n')
        return


class Computer(Player):
    def __str__(self):
        return f'(Player {self.num}) Computer'

    def make_move(self, spot=''):
        new_spot = ''

        for i in range(3):

            if i == 1:
                new_spot += ','
            else:
                new_spot += str(comp_rand_and_delay(0))

        return super().make_move(new_spot)

    def display_spot(self, row, col):
        delay = random.randint(2, 5)
        print(f"{self}'s spot: ", end='')

        for i in range(3):
            comp_rand_and_delay(delay)
            if i == 1:
                print(",", end='')
            elif i == 2:
                print(f"{col}")
            else:
                print(f"{row}", end='')

            delay /= 2

        return


class Human(Player):
    def __str__(self):
        return f'Player {self.num}'

    def make_move(self, spot=""):
        spot = input(f'Enter spot, {self}: ')
        return super().make_move(spot)


class Tic_tac_toe:
    def __init__(self):
        self.board = Board()
        self.play_num = 1

    def is_valid_move(self, row, col):
        if self.board.space_filled(row, col):
            return False
        return True

    def play(self, team):
        comp = ''

        if team == 1:
            if self.play_num == 1:
                comp = Computer(self.play_num)
                ply_spot = comp.make_move()
            else:
                ply_spot = Human(self.play_num).make_move()
        else:
            ply_spot = Human(self.play_num).make_move()

        if ply_spot:
            row, col = ply_spot

            if self.is_valid_move(row, col):

                # Displaying computer's choice
                if team == 1 and self.play_num == 1:
                    comp.display_spot(row, col)

                # Filling the space
                self.board.fill_space(row, col, self.play_num)
                self.play_num = (self.play_num + 2) % 2 + 1
                return
            else:
                if team == 1 and self.play_num == 1:
                    pass
                else:
                    print(f'{centre_msg()}Error! space filled.\n')

        return self.play(team)

    def check_for_winner(self):
        # for same player card on the same row
        for row in range(3):
            if self.board.spaces[row][0] == \
                    self.board.spaces[row][1] == \
                    self.board.spaces[row][2] != 0:

                return self.board.spaces[row][0]

        # for same player card on the same col of diff row
        for col in range(3):
            if self.board.spaces[0][col] == \
                    self.board.spaces[1][col] == \
                    self.board.spaces[2][col] != 0:

                return self.board.spaces[0][col]

        # for diagonal
        if self.board.spaces[0][0] == \
                self.board.spaces[1][1] == \
                self.board.spaces[2][2] != 0:

            return self.board.spaces[0][0]

        # for diagonal
        if self.board.spaces[0][2] == \
                self.board.spaces[1][1] == \
                self.board.spaces[2][0] != 0:

            return self.board.spaces[0][2]

        # if nobody wins and all spaces are filled
        if not self.board.get_open_spots:
            return 0

        # If the game should continue; nobody won yet and there are still spaces
        return -1

    def reset(self):
        self.board.spaces = [[0 for j in range(3)] for i in range(3)]
        return


# =====> Initialising game
game = Tic_tac_toe()

start = True

msg = '''Welcome to "Tic_tac_toe" game. Where each player places his/her token in a cell; one at 
a time. If 3 of a player's tokens are aligned (vertically, horizontally, or diagonally), 
then, such player is the winner.
NOTE: 
    * You choose a cell by entering the row and col you want; "row,col" e.g 1,2; 
    * Two (2) players is involved.
'''

print(msg)

while start:
    player_help = '''
=> "1" You and Computer
=> "2" You and opponent
    '''
    print(player_help)

    team = input('Enter your choice: ')

    if team.isdigit() and 0 < int(team) <= 2:

        # Playing game
        print(f'{centre_msg()}Game start...')
        team = int(team)
        while game.check_for_winner() == -1:
            display_board(game.board.spaces)
            game.play(team)

        # Game finished and announcing winner
        display_board(game.board.spaces)
        winner = game.check_for_winner()

        if winner:

            if team == 1 and winner == 1:
                print(f'{centre_msg()}Computer (Player {winner}) is the winner!')
            else:
                print(f'{centre_msg()}Player {winner} is the winner!')
        else:
            print(f'{centre_msg()}It\'s a draw!')

        cont = input('Would You like to go again?(Yes/No) ').capitalize()

        if cont == 'Yes':
            game.reset()
            continue
        else:
            start = False
    else:
        print(f'{centre_msg()}Error! Waiting for your response.')













