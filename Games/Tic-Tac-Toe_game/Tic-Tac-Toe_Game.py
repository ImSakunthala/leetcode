"""
Tic-tac-toe is played on a three-by-three grid by two players, who alternately place the marks X and O in one of
the nine spaces in the grid.

Here, in this Game played between two players [Player_1, Player_2] Player_1 is always 'X' and Player_2 is always
'Y'.Since, there is no universally-agreed rule as to who plays first, but in this game the convention that X plays
first is used.

Win Condition:  The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is
the winner.
Draw Condition: It is a solved game, with a forced draw assuming best play from both players.

Create Board -> Create a game board [Why? -> Tic Tac Toe is totally based on X and O, we can represent them in arrays
like 'X' -> [1,0], 'O' -> [1,1] but it will be easier if we represent this in as a actual game for better understanding]
Properties of Board:
1) At first, empty game board with columns and rows named from 1 to 9

2) Display the board

3) Update cells -> To enter X choice and O choice [Note: if already X choice or choice in updated cells, it should ask
another input from person who entered wrong input]

4) Check Win -> There are 8 win conditions:
    Condition 1 to 3 -> All rows with same player, that is Cells[1, 2, 3] == 'X'|'O' -> X|O Wins
    Cells[4, 5, 6] == 'X'|'O' -> X|O Wins, Cells[7, 8, 9] == 'X'|'O' -> X|O Wins
    Condition 4 to 6 -> All columns with same player, that is Cells[1, 4, 7] == 'X'|'O' -> X|O Wins
    Cells[2, 5, 8] == 'X'|'O' -> X|O Wins, Cells[3, 6, 9] == 'X'|'O' -> X|O Wins
    Condition  7 and 8 -> Two diagonals with same player, that is Cells[1, 5, 9] == 'X'|'O' -> X|O Wins
    Cells[3, 5, 7] == 'X'|'O' -> X|O Wins.

5) Check Tie -> if all the cells are filled and there is no way to continue the game then it is a Tie Game.

**************************** Very Simple Game for basic OOP concept ****************************************
"""


class TicTacToe:
    players = ['X', 'O']

    def __init__(self, matrix: int = 3):
        print('\n*******Welcome to Tic-Tac-Toe game!*******\n')
        self.matrix = matrix

        # Populate cell with values from 1 to matrix square.
        self.cells = [[row + col for col in range(1, matrix + 1)] for row in range(0, matrix ** 2, matrix)]

    def display_board(self):
        for row in self.cells:
            for col in row:
                print(f'{col}', end=' | ')
            print('\n--|---|---|')

    def __update_cells(self, cell_no, player):
        row_idx = (cell_no - 1) // self.matrix
        col_idx = (cell_no - 1) % self.matrix

        if self.cells[row_idx][col_idx] == cell_no:
            self.cells[row_idx][col_idx] = player
        else:
            raise ValueError('Invalid position')

    def make_choice(self, player: str):
        while True:
            try:
                x_choice = int(input(f'\n {player} choice between 1 to 9:'))
                self.__update_cells(x_choice, player)
                break
            except ValueError as e:
                print(e)

    def player_choice(self, player: str):
        self.make_choice(player)
        self.display_board()

    def __is_row_same(self, player: str) -> bool:
        for row in self.cells:
            if row == [player] * 3:
                return True
        return False

    def __is_columns_same(self, player: str) -> bool:
        for column in zip(*self.cells):
            if list(column) == [player] * 3:
                return True
        return False

    def __is_forward_diagonal_same(self, player: str) -> bool:
        for i in range(self.matrix):
            if self.cells[i][i] == player:
                continue
            else:
                return False
        return True

    def __is_reverse_diagonals_same(self, player: str) -> bool:
        for i in range(self.matrix):
            if self.cells[i][self.matrix - i - 1] == player:
                continue
            else:
                return False
        return True

    def __is_diagonals_same(self, player: str) -> bool:
        return self.__is_forward_diagonal_same(player) or self.__is_reverse_diagonals_same(player)

    def is_game_over(self):
        for row in self.cells:
            for col in row:
                if str(col).isdigit():
                    return False
        return True

    def check_win(self, player: str):
        return self.__is_row_same(player) \
               or self.__is_columns_same(player) \
               or self.__is_diagonals_same(player)

    def start(self):
        self.display_board()

        while not self.is_game_over():
            for player in self.players:

                if self.is_game_over():
                    print('Game Tie!')
                    break

                self.player_choice(player)
                if self.check_win(player):
                    print(f'{player} wins!')
                    break

# TODO: overlapping of X and O choice, specify separate forward and backward diagonal check, define tie conditon
#  while checking win condition. Refactor as much as we can



game = TicTacToe()
game.start()
